# Generated by Django 5.0.6 on 2024-08-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="caption",
            field=models.CharField(default=1, max_length=300, verbose_name="توضیحات"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.CharField(max_length=30, verbose_name="نویسنده"),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="زمان انتشار"),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to="post_images/", verbose_name="عکس"),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=60, verbose_name="عنوان"),
        ),
    ]
