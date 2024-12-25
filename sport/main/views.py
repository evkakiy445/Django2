from django.shortcuts import render
from workout.models import WorkoutProgram
from django.db.models import Count


def index(request):
    # Извлекаем 8 популярных программ по количеству добавлений в избранное
    popular_programs = WorkoutProgram.objects.annotate(favorites_count=Count('favorited_by')).order_by(
        '-favorites_count')[:8]

    return render(request, 'main/index.html', {'popular_programs': popular_programs})

def faq(request):
    return render(request, 'main/faq.html')
