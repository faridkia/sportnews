from django.db import models
from accounts.models import User

class Post(models.Model):
    title = models.CharField(max_length=60, verbose_name='عنوان')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='posts')
    image = models.ImageField(upload_to='post_images/', verbose_name='عکس')
    caption = models.TextField(max_length=3000, verbose_name='توضیحات', null=True, blank=True)


    def __str__(self):
        return f'{self.id}-{self.author}-{self.title}'

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

