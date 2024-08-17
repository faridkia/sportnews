from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=60, verbose_name='عنوان')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')
    author = models.CharField(max_length=30, verbose_name='نویسنده')
    image = models.ImageField(upload_to='post_images/', verbose_name='عکس')
    caption = models.CharField(max_length=300, verbose_name='توضیحات', null=True, blank=True)


    def __str__(self):
        return f'{self.id}-{self.author}-{self.title}'

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

