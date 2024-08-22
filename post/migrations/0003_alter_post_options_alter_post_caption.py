# Generated by Django 5.0.6 on 2024-08-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0002_post_caption_alter_post_author_alter_post_created_at_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "پست", "verbose_name_plural": "پست ها"},
        ),
        migrations.AlterField(
            model_name="post",
            name="caption",
            field=models.CharField(
                blank=True, max_length=300, null=True, verbose_name="توضیحات"
            ),
        ),
    ]