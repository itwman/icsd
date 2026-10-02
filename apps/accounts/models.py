import random
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

mobile_validator = RegexValidator(r"^09\d{9}$", "شماره موبایل باید ۱۱ رقم و با ۰۹ شروع شود.")


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create(self, mobile, password, **extra):
        if not mobile:
            raise ValueError("شماره موبایل الزامی است")
        user = self.model(mobile=mobile, **extra)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, mobile, password=None, **extra):
        extra.setdefault("is_staff", False)
        extra.setdefault("is_superuser", False)
        return self._create(mobile, password, **extra)

    def create_superuser(self, mobile, password=None, **extra):
        extra["is_staff"] = True
        extra["is_superuser"] = True
        return self._create(mobile, password, **extra)


class User(AbstractUser):
    """کاربر با موبایل به عنوان شناسه‌ی اصلی. رمز اختیاری است؛ ورود با کد پیامکی هم ممکن است."""
    username = None
    mobile = models.CharField("موبایل", max_length=11, unique=True, validators=[mobile_validator])
    email = models.EmailField("ایمیل", blank=True, null=True, unique=True)
    first_name = models.CharField("نام", max_length=80, blank=True)
    last_name = models.CharField("نام خانوادگی", max_length=80, blank=True)
    birth_date = models.DateField("تاریخ تولد", null=True, blank=True)
    avatar = models.ImageField("تصویر", upload_to="avatars/", blank=True)
    bio = models.TextField("درباره", blank=True, help_text="برای مدرسان در صفحه‌ی دوره نمایش داده می‌شود.")
    job_title = models.CharField("عنوان شغلی", max_length=100, blank=True)
    is_instructor = models.BooleanField("مدرس", default=False)
    mobile_verified = models.BooleanField("موبایل تأیید شده", default=False)

    # پروفایل کامل
    GENDERS = [("", "—"), ("m", "مرد"), ("f", "زن")]
    EDU = [("", "—"), ("diploma", "دیپلم"), ("associate", "کاردانی"), ("bachelor", "کارشناسی"),
           ("master", "کارشناسی ارشد"), ("phd", "دکتری")]
    father_name = models.CharField("نام پدر", max_length=80, blank=True)
    national_code = models.CharField("کد ملی", max_length=10, blank=True, help_text="اختیاری — فقط برای درج روی گواهینامه")
    gender = models.CharField("جنسیت", max_length=1, choices=GENDERS, blank=True)
    education = models.CharField("تحصیلات", max_length=10, choices=EDU, blank=True)
    field_of_study = models.CharField("رشته", max_length=100, blank=True)
    company = models.CharField("شرکت / سازمان", max_length=150, blank=True)
    province = models.ForeignKey("leads.Province", verbose_name="استان", null=True, blank=True, on_delete=models.SET_NULL)
    city = models.ForeignKey("leads.City", verbose_name="شهر", null=True, blank=True, on_delete=models.SET_NULL)
    website = models.URLField("وب‌سایت", blank=True)
    linkedin = models.URLField("لینکدین", blank=True)
    show_certificates_publicly = models.BooleanField("گواهینامه‌ها در تأیید عمومی با نام کامل نمایش داده شود", default=True)

    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.get_full_name() or self.mobile

    def save(self, *args, **kwargs):
        if self.email == "":
            self.email = None
        super().save(*args, **kwargs)

    @property
    def display_name(self):
        return self.get_full_name() or "کاربر " + self.mobile[-4:]


class OTP(models.Model):
    """کد یک‌بارمصرف پیامکی."""
    mobile = models.CharField(max_length=11, db_index=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    attempts = models.PositiveSmallIntegerField(default=0)
    is_used = models.BooleanField(default=False)

    class Meta:
        verbose_name = "کد یک‌بارمصرف"
        verbose_name_plural = "کدهای یک‌بارمصرف"
        ordering = ["-created_at"]

    @classmethod
    def issue(cls, mobile: str) -> "OTP":
        # حداکثر یک کد در هر ۶۰ ثانیه
        recent = cls.objects.filter(mobile=mobile, created_at__gte=timezone.now() - timedelta(seconds=60)).first()
        if recent and not recent.is_used:
            return recent
        code = f"{random.SystemRandom().randint(0, 999999):06d}"
        return cls.objects.create(mobile=mobile, code=code)

    def is_valid(self) -> bool:
        ttl = getattr(settings, "OTP_TTL_SECONDS", 180)
        return (not self.is_used and self.attempts < 5
                and self.created_at >= timezone.now() - timedelta(seconds=ttl))

    @classmethod
    def verify(cls, mobile: str, code: str) -> bool:
        otp = cls.objects.filter(mobile=mobile, is_used=False).first()
        if not otp or not otp.is_valid():
            return False
        if otp.code != code:
            otp.attempts += 1
            otp.save(update_fields=["attempts"])
            return False
        otp.is_used = True
        otp.save(update_fields=["is_used"])
        return True
