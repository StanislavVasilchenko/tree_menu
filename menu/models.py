from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField()

    def __str__(self):
        return f'{self.title} - {self.parent}'

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'MENU'
