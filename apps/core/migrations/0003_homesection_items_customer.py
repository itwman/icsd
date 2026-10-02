# Handwritten to match apps/core/models.py — بخش‌های جدید صفحه‌ی اصلی و مدل مشتری

import apps.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sitesettings_hero_particles_sitesettings_hero_words_and_more'),
        ('products', '0002_product_logo_status_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homesection',
            name='key',
            field=models.CharField(choices=[('sialk', 'منظره\u200cی تپه سیلک (نوار تمام\u200cعرض)'), ('band', 'نوار نقش سفال'), ('products', 'محصولات'), ('customers', 'مشتریان'), ('timeline', 'خط زمان کاشان'), ('academy', 'آکادمی'), ('blog', 'مقالات'), ('cta', 'فراخوان'), ('custom', 'بخش سفارشی (متن آزاد)')], max_length=20, verbose_name='نوع بخش'),
        ),
        migrations.AddField(
            model_name='homesection',
            name='items_limit',
            field=models.PositiveSmallIntegerField(default=8, help_text='برای محصولات، مشتریان، دوره\u200cها و مقالات. ۰ یعنی همه.', verbose_name='حداکثر تعداد آیتم'),
        ),
        migrations.AddField(
            model_name='homesection',
            name='button_text',
            field=models.CharField(blank=True, help_text='خالی = دکمه\u200cی پیش\u200cفرض بخش', max_length=40, verbose_name='متن دکمه'),
        ),
        migrations.AddField(
            model_name='homesection',
            name='button_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='آدرس دکمه'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='نام مشتری')),
                ('logo', models.FileField(blank=True, help_text='PNG یا WebP با پس\u200cزمینه\u200cی شفاف (ارتفاع پیشنهادی ۲۰۰ پیکسل؛ لوگوی افقی هم مناسب است) یا SVG. حداکثر ۸۰۰ کیلوبایت.', upload_to='customers/', validators=[apps.common.validators.LogoValidator(max_kb=800, min_side=120, square=False)], verbose_name='لوگو')),
                ('website', models.URLField(blank=True, verbose_name='وب\u200cسایت')),
                ('city', models.CharField(blank=True, max_length=60, verbose_name='شهر')),
                ('industry', models.CharField(blank=True, help_text='مثل: ریسندگی، فرش ماشینی، بازرگانی', max_length=80, verbose_name='حوزه\u200cی فعالیت')),
                ('description', models.TextField(blank=True, help_text='یک یا دو جمله؛ در صفحه\u200cی مشتریان نمایش داده می\u200cشود.', verbose_name='توضیح کوتاه همکاری')),
                ('since', models.CharField(blank=True, help_text='مثل ۱۴۰۲', max_length=20, verbose_name='شروع همکاری')),
                ('show_on_home', models.BooleanField(default=True, verbose_name='نمایش در صفحه اصلی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='ترتیب')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(blank=True, related_name='customers', to='products.product', verbose_name='محصولات استفاده\u200cشده')),
            ],
            options={
                'verbose_name': 'مشتری',
                'verbose_name_plural': 'مشتریان',
                'ordering': ['order', 'name'],
            },
        ),
    ]
