from django.db import models
from accounts.models import User
from post.models import Post

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='پست', related_name='likes')

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'

class Saved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='saved')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='پست', related_name='saved')

    class Meta:
        verbose_name = 'سیو'
        verbose_name_plural = 'سیو ها'
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='پست', related_name='comments')
    text = models.TextField(max_length=75, verbose_name='متن')
    date = models.DateTimeField(auto_now_add=True)
    is_ok = models.BooleanField(verbose_name='اجازه انتشار', default=False)
    # is_reply = models.ForeignKey('Comment', on)

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
    def __str__(self):
        return f'{self.user}-{self.post}'