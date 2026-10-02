from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_canonical_url_post_cover_alt_post_focus_keyword_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(allow_unicode=True, help_text="ترجیحاً انگلیسی — مثل tarahi-site-farsh-kashan", max_length=200, unique=True, verbose_name="نامک (در آدرس)"),
        ),
    ]
