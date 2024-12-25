from django.db import models
from django.contrib.auth.models import User

# Модель для записи рекордов
class Record(models.Model):
    CATEGORY_CHOICES = [
        ('bench_press', 'Жим лежа'),
        ('squat', 'Приседание со штангой'),
        ('deadlift', 'Становая тяга'),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Категория")
    weight = models.FloatField(verbose_name="Вес (кг)")
    video = models.URLField(verbose_name="Ссылка на видео")
    is_approved = models.BooleanField(default=False, verbose_name="Одобрено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Рекорд"
        verbose_name_plural = "Рекорды"
        ordering = ['-weight']

    def __str__(self):
        return f"{self.user.username} - {self.get_category_display()} - {self.weight} кг"