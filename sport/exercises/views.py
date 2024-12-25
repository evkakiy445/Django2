from django.shortcuts import render
from workout.models import Exercise

def exercise_list(request):
    query = request.GET.get('q', '')  # Получаем поисковый запрос из параметров GET
    if query:
        exercises = Exercise.objects.filter(name__icontains=query)  # Фильтрация по названию упражнения
    else:
        exercises = Exercise.objects.all()  # Если поисковый запрос пустой, выводим все упражнения

    return render(request, 'exercises/exercise_list.html', {'exercises': exercises, 'query': query})
