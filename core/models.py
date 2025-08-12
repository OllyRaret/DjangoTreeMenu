from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название меню')
    url = models.CharField(
        max_length=200,
        blank=True,
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', verbose_name='Меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                              related_name='children', verbose_name='Родительский пункт')
    title = models.CharField(max_length=100, verbose_name='Текст пункта')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_url(self):
        return f'/{self.menu.url}/{self.id}/'

    def has_children(self):
        return self.children.exists()
