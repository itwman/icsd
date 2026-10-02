from django.conf import settings
from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from apps.seo.models import SEOFields


class Category(models.Model):
    title = models.CharField("عنوان", max_length=80, unique=True)
    slug = models.SlugField("نامک", unique=True, allow_unicode=True)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    icon = models.CharField("آیکن (نام Material)", max_length=40, blank=True, default="school")

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "دسته‌بندی دوره"
        verbose_name_plural = "دسته‌بندی دوره‌ها"

    def __str__(self):
        return self.title


class Course(SEOFields, models.Model):
    LEVELS = [("beginner", "مقدماتی"), ("intermediate", "متوسط"), ("advanced", "پیشرفته")]

    title = models.CharField("عنوان", max_length=150)
    slug = models.SlugField("نامک (در آدرس)", unique=True, allow_unicode=True)
    category = models.ForeignKey(Category, verbose_name="دسته‌بندی", on_delete=models.PROTECT, related_name="courses")
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="مدرس", null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name="courses",
                                   limit_choices_to={"is_instructor": True})
    level = models.CharField("سطح", max_length=12, choices=LEVELS, default="beginner")
    summary = models.CharField("خلاصه‌ی یک‌خطی", max_length=250)
    description = CKEditor5Field("شرح کامل", config_name="default", blank=True)
    cover = models.ImageField("تصویر", upload_to="courses/", blank=True)
    price = models.PositiveIntegerField("قیمت (تومان)", default=0, help_text="۰ یعنی رایگان")
    duration_minutes = models.PositiveIntegerField("مدت کل (دقیقه)", default=0)
    tags = models.ManyToManyField("blog.Tag", verbose_name="برچسب‌ها", blank=True, related_name="courses")
    is_published = models.BooleanField("منتشر شده", default=True)
    is_featured = models.BooleanField("ویژه (نمایش در صفحه اصلی)", default=False)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    created_at = models.DateTimeField("ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("به‌روزرسانی", auto_now=True)
    published_at = models.DateField("تاریخ انتشار", null=True, blank=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "دوره"
        verbose_name_plural = "دوره‌ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("academy:course_detail", args=[self.slug])

    @property
    def is_free(self):
        return self.price == 0

    @property
    def lesson_count(self):
        return Lesson.objects.filter(module__course=self).count()

    def first_lesson(self):
        return Lesson.objects.filter(module__course=self).order_by("module__order", "order").first()


class Module(models.Model):
    course = models.ForeignKey(Course, verbose_name="دوره", on_delete=models.CASCADE, related_name="modules")
    title = models.CharField("عنوان فصل", max_length=150)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "فصل"
        verbose_name_plural = "فصل‌ها"

    def __str__(self):
        return f"{self.course.title} › {self.title}"


class Lesson(models.Model):
    KINDS = [("text", "متنی"), ("video", "ویدیویی")]
    SOURCES = [("none", "بدون ویدیو"), ("arvan", "آروان VOD"), ("aparat", "آپارات / کد جاسازی"), ("upload", "فایل آپلودشده")]

    module = models.ForeignKey(Module, verbose_name="فصل", on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField("عنوان درس", max_length=150)
    slug = models.SlugField("نامک", allow_unicode=True, blank=True)
    kind = models.CharField("نوع", max_length=8, choices=KINDS, default="text")
    minutes = models.PositiveSmallIntegerField("مدت (دقیقه)", default=10)
    is_preview = models.BooleanField("پیش‌نمایش رایگان", default=False)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    body = CKEditor5Field("متن درس", config_name="default", blank=True)

    video_source = models.CharField("منبع ویدیو", max_length=8, choices=SOURCES, default="none")
    arvan_video_id = models.CharField("آدرس پلیر آروان", max_length=300, blank=True, help_text="آدرس کامل Player URL از پنل آروان VOD")
    embed_html = models.TextField("کد جاسازی (آپارات و ...)", blank=True)
    video_file = models.FileField("فایل ویدیو", upload_to="lessons/videos/", blank=True)
    attachment = models.FileField("فایل پیوست (کد، اسلاید)", upload_to="lessons/files/", blank=True)

    class Meta:
        ordering = ["module__order", "order", "id"]
        verbose_name = "درس"
        verbose_name_plural = "درس‌ها"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title, allow_unicode=True)[:50] or f"lesson-{self.pk or ''}"
        super().save(*args, **kwargs)

    @property
    def course(self):
        return self.module.course

    def get_absolute_url(self):
        return reverse("academy:learn", args=[self.module.course.slug, self.pk])


class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="کاربر", on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, verbose_name="دوره", on_delete=models.CASCADE, related_name="enrollments")
    created_at = models.DateTimeField("تاریخ ثبت‌نام", auto_now_add=True)
    expires_at = models.DateField("انقضا", null=True, blank=True)
    is_active = models.BooleanField("فعال", default=True)

    class Meta:
        unique_together = [("user", "course")]
        verbose_name = "ثبت‌نام"
        verbose_name_plural = "ثبت‌نام‌ها"

    def __str__(self):
        return f"{self.user} → {self.course}"

    @property
    def completed_count(self):
        return self.progress.count()

    @property
    def percent(self):
        total = self.course.lesson_count
        return int(self.completed_count * 100 / total) if total else 0


class LessonProgress(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("enrollment", "lesson")]
        verbose_name = "پیشرفت درس"
        verbose_name_plural = "پیشرفت درس‌ها"


# ═══════════════════════════ آزمون و گواهینامه ═══════════════════════════
import uuid


class Quiz(models.Model):
    course = models.OneToOneField(Course, verbose_name="دوره", on_delete=models.CASCADE, related_name="quiz")
    title = models.CharField("عنوان آزمون", max_length=150)
    description = models.TextField("توضیح", blank=True)
    pass_percent = models.PositiveSmallIntegerField("درصد قبولی", default=70)
    time_limit_minutes = models.PositiveSmallIntegerField("مهلت (دقیقه)", default=20)
    questions_per_attempt = models.PositiveSmallIntegerField("تعداد سؤال هر نوبت", default=0, help_text="۰ یعنی همه‌ی سؤال‌ها")
    max_attempts = models.PositiveSmallIntegerField("حداکثر نوبت", default=0, help_text="۰ یعنی نامحدود")
    is_active = models.BooleanField("فعال", default=True)
    show_explanations = models.BooleanField("نمایش توضیح پاسخ‌ها بعد از آزمون", default=True)

    class Meta:
        verbose_name = "آزمون"
        verbose_name_plural = "آزمون‌ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("academy:quiz_start", args=[self.course.slug])


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField("متن سؤال")
    explanation = models.TextField("توضیح پاسخ", blank=True)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    is_active = models.BooleanField("فعال", default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "سؤال"
        verbose_name_plural = "سؤال‌ها"

    def __str__(self):
        return self.text[:70]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField("گزینه", max_length=300)
    is_correct = models.BooleanField("درست", default=False)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "گزینه"
        verbose_name_plural = "گزینه‌ها"

    def __str__(self):
        return self.text


class Attempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="کاربر", on_delete=models.CASCADE, related_name="attempts")
    quiz = models.ForeignKey(Quiz, verbose_name="آزمون", on_delete=models.CASCADE, related_name="attempts")
    started_at = models.DateTimeField("شروع", auto_now_add=True)
    finished_at = models.DateTimeField("پایان", null=True, blank=True)
    question_ids = models.JSONField("سؤال‌های این نوبت", default=list)
    answers = models.JSONField("پاسخ‌ها", default=dict)        # {question_id: choice_id}
    score = models.PositiveSmallIntegerField("نمره (درصد)", default=0)
    passed = models.BooleanField("قبول", default=False)

    class Meta:
        ordering = ["-started_at"]
        verbose_name = "نوبت آزمون"
        verbose_name_plural = "نوبت‌های آزمون"

    def __str__(self):
        return f"{self.user} — {self.quiz} — {self.score}٪"

    @property
    def is_open(self):
        if self.finished_at:
            return False
        from django.utils import timezone
        from datetime import timedelta
        return timezone.now() <= self.started_at + timedelta(minutes=self.quiz.time_limit_minutes)

    def grade(self):
        qs = Question.objects.filter(pk__in=self.question_ids).prefetch_related("choices")
        total = qs.count()
        correct = 0
        for q in qs:
            chosen = self.answers.get(str(q.pk))
            if chosen and q.choices.filter(pk=chosen, is_correct=True).exists():
                correct += 1
        self.score = int(correct * 100 / total) if total else 0
        self.passed = self.score >= self.quiz.pass_percent
        return self.score


class Certificate(models.Model):
    code = models.UUIDField("کد", default=uuid.uuid4, unique=True, editable=False)
    serial = models.CharField("شماره", max_length=20, unique=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="کاربر", on_delete=models.CASCADE, related_name="certificates")
    course = models.ForeignKey(Course, verbose_name="دوره", on_delete=models.CASCADE, related_name="certificates")
    attempt = models.OneToOneField(Attempt, verbose_name="نوبت آزمون", on_delete=models.CASCADE, related_name="certificate")
    full_name = models.CharField("نام روی گواهی", max_length=160)
    score = models.PositiveSmallIntegerField("نمره")
    issued_at = models.DateTimeField("تاریخ صدور", auto_now_add=True)
    is_revoked = models.BooleanField("ابطال شده", default=False)

    class Meta:
        ordering = ["-issued_at"]
        verbose_name = "گواهینامه"
        verbose_name_plural = "گواهینامه‌ها"

    def __str__(self):
        return f"{self.serial} — {self.full_name} — {self.course}"

    def save(self, *args, **kwargs):
        if not self.serial:
            import jdatetime
            y = jdatetime.date.today().year
            n = Certificate.objects.filter(serial__startswith=f"ICSD-{y}-").count() + 1
            self.serial = f"ICSD-{y}-{n:05d}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("academy:certificate", args=[self.code])

    def verify_url(self):
        return reverse("verify", args=[self.code])
