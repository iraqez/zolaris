from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(verbose_name='Электронная почта')
    name = models.CharField(max_length=128, verbose_name='Имя')

    # def __str__(self):
    #     return "Пользователь: %s (%s)" % (self.name, self.email)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"