from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import WorkoutProgram, FavoriteProgram, Exercise, WorkoutResult
from django.contrib.auth.decorators import login_required


def workout_list(request):
    # Извлекаем параметры фильтров из запроса
    difficulty = request.GET.get('difficulty')
    workout_type = request.GET.get('workout_type')
    training_place = request.GET.get('training_place')

    # Фильтрация программ тренировки
    programs = WorkoutProgram.objects.all()

    if difficulty:
        programs = programs.filter(difficulty_level=difficulty)
    if workout_type:
        programs = programs.filter(workout_type=workout_type)
    if training_place:
        programs = programs.filter(training_place=training_place)

    if request.user.is_authenticated:
        user = request.user
        # Добавляем информацию о том, понравилась ли программа текущему пользователю
        for program in programs:
            program.is_favorited = program.favorited_by.filter(id=user.id).exists()
    else:
        for program in programs:
            program.is_favorited = False

    return render(request, 'workout/workout_list.html', {'programs': programs})


def workout_detail(request, pk):
    # Получаем программу по первичному ключу
    program = get_object_or_404(WorkoutProgram, pk=pk)
    return render(request, 'workout/workout_detail.html', {'program': program})


@login_required
def add_to_favorites(request, pk):
    program = WorkoutProgram.objects.get(pk=pk)

    # Проверяем, добавлена ли уже программа в избранное
    if FavoriteProgram.objects.filter(user=request.user).exists():
        # Если программа уже в избранном, выводим сообщение
        messages.error(request, "Вы можете добавить только одну программу в избранное.")
    else:
        # Если нет, добавляем программу в избранное
        FavoriteProgram.objects.create(user=request.user, program=program)
        messages.success(request, f"Программа добавлена в избранное!")

    return redirect('workout_list')  # Перенаправляем на список программ


@login_required
def remove_from_favorites(request, pk):
    program = WorkoutProgram.objects.get(pk=pk)
    # Удаляем программу из избранного
    FavoriteProgram.objects.filter(user=request.user, program=program).delete()
    messages.success(request, f"Программа удалена из избранного.")
    return redirect('profile')  # Перенаправляем на профиль


@login_required
def add_workout_result(request, program_pk, exercise_pk):
    program = get_object_or_404(WorkoutProgram, pk=program_pk)
    exercise = get_object_or_404(Exercise, pk=exercise_pk)

    if request.method == 'POST':
        repetitions = request.POST.get('repetitions')
        weight = request.POST.get('weight')

        # Создаем запись о результате тренировки
        WorkoutResult.objects.create(
            user=request.user,
            program=program,
            exercise=exercise,
            repetitions=repetitions,
            weight=weight
        )
        return redirect('profile')  # Перенаправление на профиль

    return render(request, 'workout/add_result.html', {'program': program, 'exercise': exercise})
