from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from workout.models import WorkoutProgram
from django.contrib import messages
from django.db import models


@login_required
def add_review(request, program_pk):
    program = get_object_or_404(WorkoutProgram, pk=program_pk)

    if request.method == 'POST':
        text = request.POST.get('text')
        rating = request.POST.get('rating')

        Review.objects.create(
            user=request.user,
            program=program,
            text=text,
            rating=rating
        )

        return redirect('program_reviews', program_pk=program.pk)

    return render(request, 'reviews/add_review.html', {'program': program})

def program_reviews(request, program_pk):
    program = get_object_or_404(WorkoutProgram, pk=program_pk)
    reviews = program.reviews.all()

    # Вычисление средней оценки
    if reviews.exists():
        average_rating = reviews.aggregate(models.Avg('rating'))['rating__avg']
    else:
        average_rating = None  # Если нет отзывов, средняя оценка не существует

    return render(request, 'reviews/program_reviews.html', {
        'program': program,
        'reviews': reviews,
        'average_rating': average_rating,
    })

def all_reviews(request):
    reviews = Review.objects.all().order_by('-created_at')  # Извлекаем все отзывы

    selected_program_id = request.GET.get('program')  # Получаем выбранную программу из запроса

    if selected_program_id == "none":  # Если выбран "Общий отзыв"
        reviews = reviews.filter(program__isnull=True)
    elif selected_program_id:  # Если выбрана конкретная программа
        reviews = reviews.filter(program_id=selected_program_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Сохраняем новый отзыв
            review = form.save(commit=False)
            review.user = request.user  # Привязываем отзыв к текущему пользователю
            review.save()
            return redirect('all_reviews')  # Перенаправляем обратно на страницу всех отзывов
    else:
        form = ReviewForm()

    # Передаем все программы в контекст
    all_programs = WorkoutProgram.objects.all()

    return render(request, 'reviews/all_reviews.html', {
        'reviews': reviews,
        'form': form,
        'all_programs': all_programs,  # Передаем программы в контекст
        'selected_program_id': selected_program_id,
    })


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    # Проверяем, что текущий пользователь является автором отзыва
    if review.user == request.user:
        review.delete()

    # Возвращаем пользователя на страницу отзывов программы
    return redirect('program_reviews', program_pk=review.program.id)

@login_required
def delete_all_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    # Проверяем, что текущий пользователь является автором отзыва
    if review.user == request.user:
        review.delete()

    # Возвращаем пользователя на страницу отзывов программы
    return redirect('all_reviews')

