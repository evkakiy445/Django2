from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Выбор уровня сложности
class DifficultyLevel(models.TextChoices):
    EASY = 'Легкая', 'Легкая'
    MEDIUM = 'Средняя', 'Средняя'
    HARD = 'Сложная', 'Сложная'


# Выбор типа тренировки
class WorkoutType(models.TextChoices):
    CARDIO = 'Кардио', 'Кардио'
    STRENGTH = 'Силовая', 'Силовая'


# Выбор места тренировки
class TrainingPlace(models.TextChoices):
    GYM = 'Тренажерный зал', 'Тренажерный зал'
    HOME = 'Дом', 'Дом'


# Модель группы мышц
class MuscleGroup(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to='muscle_groups/', verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа мышц"
        verbose_name_plural = "Группы мышц"


# Модель упражнения
class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='exercises/', verbose_name="Изображение")
    technique_description = models.TextField(verbose_name="Описание техники выполнения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Упражнение"
        verbose_name_plural = "Упражнения"


# Модель программы тренировки
class WorkoutProgram(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название программы")
    image = models.ImageField(upload_to='workout_programs/', verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание программы")
    muscle_groups = models.ManyToManyField(MuscleGroup, verbose_name="Группы мышц")
    exercises = models.ManyToManyField(Exercise, verbose_name="Упражнения")

    # Новые поля с дефолтными значениями
    difficulty_level = models.CharField(
        max_length=10,
        choices=DifficultyLevel.choices,
        verbose_name="Уровень сложности",
        default=DifficultyLevel.EASY  # Устанавливаем дефолтное значение
    )
    workout_type = models.CharField(
        max_length=10,
        choices=WorkoutType.choices,
        verbose_name="Тип тренировки",
        default=WorkoutType.CARDIO  # Устанавливаем дефолтное значение
    )
    training_place = models.CharField(
        max_length=20,
        choices=TrainingPlace.choices,
        verbose_name="Место тренировки",
        default=TrainingPlace.GYM  # Устанавливаем дефолтное значение
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Программа тренировки"
        verbose_name_plural = "Программы тренировок"

class FavoriteProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_programs')
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'program')  # Уникальное сочетание пользователь-программа

    def __str__(self):
        return f'{self.user.username} - {self.program.title}'

class WorkoutResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_results')
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE, related_name='results')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='results')
    repetitions = models.PositiveIntegerField(verbose_name="Количество повторений")
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0, verbose_name="Вес (кг)")
    workout_date = models.DateField(auto_now_add=True, verbose_name="Дата тренировки")

    class Meta:
        verbose_name = "Результат тренировки"
        verbose_name_plural = "Результаты тренировок"

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name} ({self.workout_date})"


class WeightTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weight_tracking')
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0, verbose_name="Вес (кг)")
    date = models.DateField(auto_now_add=True, verbose_name="Дата записи веса")

    class Meta:
        verbose_name = "Отслеживание веса"
        verbose_name_plural = "Отслеживание веса"

    def __str__(self):
        return f"{self.user.username} - {self.weight} кг ({self.date})"

class UserWeightHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.weight}kg on {self.date}'

@receiver(post_delete, sender=FavoriteProgram)
def delete_workout_results_on_favorite_program_delete(sender, instance, **kwargs):
    # Удаляем все результаты для этой программы и пользователя
    WorkoutResult.objects.filter(user=instance.user, program=instance.program).delete()