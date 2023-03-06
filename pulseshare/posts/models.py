from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(
        unique=True, max_length=60, verbose_name="Ссылка"
    )
    description = models.TextField(
        max_length=400, verbose_name="Описание"
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name="Текст",
        help_text='Напишите текст поста'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name="Группа",
        help_text='Тыкните на любую, из уже существующих ;)'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Автор",
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост',
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.text[:15]}'
