import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Attempt, Category, Certificate, Course, Enrollment, Lesson, LessonProgress, Question, Quiz


# ─────────────────────────── دوره‌ها: همه رایگان و باز ───────────────────────────
def course_list(request):
    qs = Course.objects.filter(is_published=True).select_related("category", "instructor")
    q = request.GET.get("q", "").strip()
    cat = request.GET.get("cat")
    level = request.GET.get("level")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(summary__icontains=q) | Q(tags__name__icontains=q)).distinct()
    if cat:
        qs = qs.filter(category__slug=cat)
    if level in ("beginner", "intermediate", "advanced"):
        qs = qs.filter(level=level)
    return render(request, "academy/course_list.html", {
        "courses": qs, "categories": Category.objects.all(), "q": q, "cat": cat, "level": level,
    })


def course_detail(request, slug):
    course = get_object_or_404(Course.objects.select_related("category", "instructor"), slug=slug, is_published=True)
    modules = course.modules.prefetch_related("lessons")
    enrollment = certificate = None
    quiz = getattr(course, "quiz", None)
    if request.user.is_authenticated:
        enrollment = Enrollment.objects.filter(user=request.user, course=course, is_active=True).first()
        certificate = Certificate.objects.filter(user=request.user, course=course, is_revoked=False).first()
    return render(request, "academy/course_detail.html", {
        "course": course, "modules": modules, "enrollment": enrollment, "seo_obj": course,
        "quiz": quiz if (quiz and quiz.is_active) else None, "certificate": certificate,
        "related": Course.objects.filter(is_published=True, category=course.category).exclude(pk=course.pk)[:3],
    })


@login_required
def enroll(request, slug):
    """ثبت‌نام فقط برای پیگیری پیشرفت و آزمون — دوره خودش آزاد است."""
    course = get_object_or_404(Course, slug=slug, is_published=True)
    _, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    if created:
        messages.success(request, f"«{course.title}» به دوره‌های شما اضافه شد؛ پیشرفتتان ذخیره می‌شود.")
    return redirect("academy:learn_start", slug=slug)


def learn_start(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    lesson = course.first_lesson()
    if not lesson:
        messages.info(request, "این دوره هنوز درسی ندارد.")
        return redirect(course)
    if request.user.is_authenticated:
        enr = Enrollment.objects.filter(user=request.user, course=course, is_active=True).first()
        if enr:
            last = enr.progress.order_by("-completed_at").first()
            if last:
                nxt = (Lesson.objects.filter(module__course=course)
                       .filter(Q(module__order__gt=last.lesson.module.order) |
                               Q(module__order=last.lesson.module.order, order__gt=last.lesson.order))
                       .order_by("module__order", "order").first())
                lesson = nxt or last.lesson
    return redirect("academy:learn", slug=slug, lesson_id=lesson.pk)


def learn(request, slug, lesson_id):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    lesson = get_object_or_404(Lesson.objects.select_related("module"), pk=lesson_id, module__course=course)
    enrollment = None
    if request.user.is_authenticated:
        enrollment = Enrollment.objects.filter(user=request.user, course=course, is_active=True).first()
    modules = course.modules.prefetch_related("lessons")
    done_ids = set(enrollment.progress.values_list("lesson_id", flat=True)) if enrollment else set()
    lessons = list(Lesson.objects.filter(module__course=course).order_by("module__order", "order"))
    idx = next((i for i, l in enumerate(lessons) if l.pk == lesson.pk), 0)
    return render(request, "academy/learn.html", {
        "course": course, "lesson": lesson, "modules": modules, "enrollment": enrollment, "done_ids": done_ids,
        "prev": lessons[idx - 1] if idx > 0 else None,
        "next": lessons[idx + 1] if idx + 1 < len(lessons) else None,
        "is_done": lesson.pk in done_ids, "is_last": idx + 1 >= len(lessons),
        "quiz": getattr(course, "quiz", None),
    })


@login_required
@require_POST
def complete_lesson(request, slug, lesson_id):
    course = get_object_or_404(Course, slug=slug)
    lesson = get_object_or_404(Lesson, pk=lesson_id, module__course=course)
    enrollment, _ = Enrollment.objects.get_or_create(user=request.user, course=course)
    LessonProgress.objects.get_or_create(enrollment=enrollment, lesson=lesson)
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"ok": True, "percent": enrollment.percent})
    return redirect(request.POST.get("next") or lesson.get_absolute_url())


# ─────────────────────────── آزمون: رایگان، با ورود ───────────────────────────
def quiz_start(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    quiz = get_object_or_404(Quiz, course=course, is_active=True)
    attempts = certificate = None
    if request.user.is_authenticated:
        attempts = Attempt.objects.filter(user=request.user, quiz=quiz, finished_at__isnull=False)
        certificate = Certificate.objects.filter(user=request.user, course=course, is_revoked=False).first()
    return render(request, "academy/quiz_start.html", {
        "course": course, "quiz": quiz, "attempts": attempts, "certificate": certificate,
        "question_count": quiz.questions_per_attempt or quiz.questions.filter(is_active=True).count(),
        "can_attempt": (not quiz.max_attempts) or (attempts is not None and attempts.count() < quiz.max_attempts),
    })


@login_required
@require_POST
def quiz_begin(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    quiz = get_object_or_404(Quiz, course=course, is_active=True)
    if not (request.user.first_name and request.user.last_name):
        messages.warning(request, "برای صدور گواهی، اول نام و نام خانوادگی خود را در پروفایل کامل کنید.")
        request.session["next"] = request.path.replace("/begin/", "/")
        return redirect("accounts:profile")
    finished = Attempt.objects.filter(user=request.user, quiz=quiz, finished_at__isnull=False).count()
    if quiz.max_attempts and finished >= quiz.max_attempts:
        messages.error(request, "نوبت‌های مجاز این آزمون تمام شده است.")
        return redirect("academy:quiz_start", slug=slug)
    # نوبت باز قبلی
    open_att = Attempt.objects.filter(user=request.user, quiz=quiz, finished_at__isnull=True).first()
    if open_att and open_att.is_open:
        return redirect("academy:quiz_take", slug=slug, attempt_id=open_att.pk)
    if open_att:
        _finish(open_att)
    ids = list(quiz.questions.filter(is_active=True).values_list("id", flat=True))
    random.shuffle(ids)
    if quiz.questions_per_attempt:
        ids = ids[: quiz.questions_per_attempt]
    att = Attempt.objects.create(user=request.user, quiz=quiz, question_ids=ids)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    return redirect("academy:quiz_take", slug=slug, attempt_id=att.pk)


@login_required
def quiz_take(request, slug, attempt_id):
    course = get_object_or_404(Course, slug=slug)
    att = get_object_or_404(Attempt.objects.select_related("quiz"), pk=attempt_id, user=request.user, quiz__course=course)
    if att.finished_at:
        return redirect("academy:quiz_result", slug=slug, attempt_id=att.pk)
    if not att.is_open:
        _finish(att)
        messages.warning(request, "مهلت آزمون تمام شد؛ پاسخ‌های ثبت‌شده نمره‌گذاری شد.")
        return redirect("academy:quiz_result", slug=slug, attempt_id=att.pk)

    questions = list(Question.objects.filter(pk__in=att.question_ids).prefetch_related("choices"))
    order = {pk: i for i, pk in enumerate(att.question_ids)}
    questions.sort(key=lambda q: order.get(q.pk, 0))

    if request.method == "POST":
        answers = {}
        for q in questions:
            v = request.POST.get(f"q{q.pk}")
            if v and v.isdigit():
                answers[str(q.pk)] = int(v)
        att.answers = answers
        _finish(att)
        return redirect("academy:quiz_result", slug=slug, attempt_id=att.pk)

    from datetime import timedelta
    deadline = att.started_at + timedelta(minutes=att.quiz.time_limit_minutes)
    return render(request, "academy/quiz_take.html", {
        "course": course, "quiz": att.quiz, "attempt": att, "questions": questions,
        "seconds_left": max(0, int((deadline - timezone.now()).total_seconds())),
    })


def _finish(att):
    att.grade()
    att.finished_at = timezone.now()
    att.save()
    if att.passed and not Certificate.objects.filter(user=att.user, course=att.quiz.course, is_revoked=False).exists():
        Certificate.objects.create(
            user=att.user, course=att.quiz.course, attempt=att,
            full_name=att.user.get_full_name() or att.user.mobile, score=att.score,
        )


@login_required
def quiz_result(request, slug, attempt_id):
    course = get_object_or_404(Course, slug=slug)
    att = get_object_or_404(Attempt.objects.select_related("quiz"), pk=attempt_id, user=request.user, quiz__course=course)
    if not att.finished_at:
        return redirect("academy:quiz_take", slug=slug, attempt_id=att.pk)
    questions = list(Question.objects.filter(pk__in=att.question_ids).prefetch_related("choices"))
    order = {pk: i for i, pk in enumerate(att.question_ids)}
    questions.sort(key=lambda q: order.get(q.pk, 0))
    review = []
    for q in questions:
        chosen = att.answers.get(str(q.pk))
        correct = next((c for c in q.choices.all() if c.is_correct), None)
        review.append({"q": q, "chosen": chosen, "correct_id": correct.pk if correct else None,
                       "ok": bool(correct and chosen == correct.pk)})
    certificate = Certificate.objects.filter(attempt=att).first() or \
        Certificate.objects.filter(user=request.user, course=course, is_revoked=False).first()
    return render(request, "academy/quiz_result.html", {
        "course": course, "quiz": att.quiz, "attempt": att, "review": review, "certificate": certificate,
    })


# ─────────────────────────── گواهینامه ───────────────────────────
def certificate_view(request, code):
    cert = get_object_or_404(Certificate.objects.select_related("user", "course", "attempt"), code=code)
    return render(request, "academy/certificate.html", {"cert": cert})


def verify(request, code):
    cert = Certificate.objects.filter(code=code).select_related("user", "course").first()
    return render(request, "academy/verify.html", {"cert": cert, "code": code})
