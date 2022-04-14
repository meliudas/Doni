from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return self.title

