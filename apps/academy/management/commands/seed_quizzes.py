"""
بارگذاری آزمون‌های پیش‌فرض از apps/academy/seed/quizzes/*.py
اجرا:  python manage.py seed_quizzes            (آزمون‌های موجود دست نمی‌خورند)
       python manage.py seed_quizzes --overwrite
"""
import importlib
import pkgutil

from django.core.management.base import BaseCommand

from apps.academy.models import Choice, Course, Question, Quiz


class Command(BaseCommand):
    help = "بارگذاری آزمون‌های پیش‌فرض دوره‌ها"

    def add_arguments(self, parser):
        parser.add_argument("--overwrite", action="store_true")

    def handle(self, *args, **opts):
        pkg = importlib.import_module("apps.academy.seed.quizzes")
        n_q = n_quiz = 0
        for info in pkgutil.iter_modules(pkg.__path__):
            mod = importlib.import_module(f"apps.academy.seed.quizzes.{info.name}")
            data = getattr(mod, "QUIZ", None)
            if not data:
                continue
            course = Course.objects.filter(slug=data["course_slug"]).first()
            if not course:
                self.stdout.write(self.style.WARNING(f"· دوره‌ی {data['course_slug']} پیدا نشد — اول seed_courses"))
                continue
            quiz, created = Quiz.objects.get_or_create(course=course, defaults={
                "title": data.get("title", f"آزمون {course.title}"),
                "description": data.get("description", ""),
                "pass_percent": data.get("pass_percent", 70),
                "time_limit_minutes": data.get("time_limit_minutes", 20),
            })
            if not created and not opts["overwrite"]:
                self.stdout.write(f"· {quiz.title} — قبلاً هست، رد شد")
                continue
            if not created:
                quiz.title = data.get("title", quiz.title)
                quiz.description = data.get("description", quiz.description)
                quiz.pass_percent = data.get("pass_percent", quiz.pass_percent)
                quiz.time_limit_minutes = data.get("time_limit_minutes", quiz.time_limit_minutes)
            quiz.questions_per_attempt = data.get("questions_per_attempt", 0)
            quiz.save()
            quiz.questions.all().delete()
            for qi, q in enumerate(data["questions"]):
                question = Question.objects.create(quiz=quiz, text=q["text"], explanation=q.get("explanation", ""), order=qi)
                for ci, c in enumerate(q["choices"]):
                    Choice.objects.create(question=question, text=c["text"], is_correct=bool(c.get("correct")), order=ci)
                n_q += 1
            n_quiz += 1
            self.stdout.write(self.style.SUCCESS(f"✓ {quiz.title}"))
        self.stdout.write(self.style.SUCCESS(f"\n{n_quiz} آزمون و {n_q} سؤال بارگذاری شد."))
