from django.db import models
from django.contrib.auth.models import User
from workout.models import WorkoutProgram

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE, related_name='reviews', null=True)
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Оценка от 1 до 5")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания отзыва")

    def __str__(self):
        return f"Отзыв от {self.user.username} для {self.program.title}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
