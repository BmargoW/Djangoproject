from django.db import models

class BlogEntry(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.CharField(max_length=150, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/images', verbose_name="Изображение")
    creation_date = models.DateTimeField(auto_now_add=True)
    publication_status = models.BooleanField(default=True)
    number_of_views =models.IntegerField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['title']