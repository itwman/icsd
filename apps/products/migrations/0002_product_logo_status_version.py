# Handwritten to match apps/products/models.py — لوگوی استاندارد، وضعیت، نسخه، مجوز

import apps.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='logo',
            field=models.FileField(blank=True, help_text='مربع، PNG یا WebP با پس\u200cزمینه\u200cی شفاف (پیشنهاد ۵۱۲×۵۱۲ پیکسل، حداقل ۲۵۶) یا SVG مربع. حداکثر ۸۰۰ کیلوبایت.', upload_to='products/logos/', validators=[apps.common.validators.LogoValidator(max_kb=800, min_side=256, square=True)], verbose_name='لوگوی محصول'),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('stable', 'پایدار'), ('beta', 'بتا'), ('alpha', 'آلفا'), ('dev', 'در حال توسعه')], default='stable', max_length=10, verbose_name='وضعیت'),
        ),
        migrations.AddField(
            model_name='product',
            name='version',
            field=models.CharField(blank=True, help_text='مثل 3.5 (بدون v)', max_length=20, verbose_name='نسخه'),
        ),
        migrations.AddField(
            model_name='product',
            name='license_label',
            field=models.CharField(blank=True, help_text='مثل: تجاری، رایگان، متن\u200cباز', max_length=40, verbose_name='مجوز'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False, help_text='محصولات علامت\u200cخورده در بخش «محصولات» صفحه\u200cی اصلی می\u200cآیند (به ترتیب).', verbose_name='نمایش در صفحه اصلی'),
        ),
    ]
