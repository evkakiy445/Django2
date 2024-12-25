from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomRegistrationForm, CustomLoginForm, WeightTrackingForm
from workout.models import WorkoutProgram, WorkoutResult, WeightTracking, UserWeightHistory, FavoriteProgram, Exercise
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import decimal

def register(request):
    # Проверяем, если пользователь уже авторизован, перенаправляем его на страницу профиля
    if request.user.is_authenticated:
        return redirect('profile')  # Перенаправляем на страницу профиля

    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # После успешной регистрации сразу переходим на страницу профиля
    else:
        form = CustomRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        # Если пользователь уже авторизован, перенаправляем его на страницу профиля
        if self.request.user.is_authenticated:
            return 'profile'  # Правильный URL для профиля
        return super().get_redirect_url()  # Возвращаем стандартное перенаправление, если пользователь не авторизован


@login_required
def profile(request):
    user = request.user

    favorite_programs = FavoriteProgram.objects.filter(user=request.user)

    workout_results = WorkoutResult.objects.filter(user=request.user).order_by('-workout_date')

    weight_tracking = WeightTracking.objects.filter(user=request.user).order_by('-date')

    return render(request, 'accounts/profile.html', {
        'user': user,
        'favorite_programs': favorite_programs,
        'workout_results': workout_results,
        'weight_tracking': weight_tracking,
    })


@login_required
def add_workout_result(request, program_pk, exercise_pk):
    program = get_object_or_404(WorkoutProgram, pk=program_pk)
    exercise = get_object_or_404(Exercise, pk=exercise_pk)

    if request.method == 'POST':
        repetitions = request.POST.get('repetitions')
        weight = request.POST.get('weight')

        if weight in (None, '', '0'):  # Проверка на пустую строку или '0'
            weight = decimal.Decimal('0')  # Преобразуем 0 в Decimal
        else:
            try:
                weight = decimal.Decimal(weight)  # Преобразуем в Decimal, если возможно
            except decimal.InvalidOperation:
                weight = decimal.Decimal('0')

        WorkoutResult.objects.create(
            user=request.user,
            program=program,
            exercise=exercise,
            repetitions=repetitions,
            weight=weight,
        )

        return redirect('profile')

    return render(request, 'accounts/add_workout_result.html', {'program': program, 'exercise': exercise})


@login_required
def add_weight_tracking(request):
    if request.method == 'POST':
        weight = request.POST.get('weight')

        WeightTracking.objects.create(
            user=request.user,
            weight=weight,
        )

        return redirect('profile')

    return render(request, 'accounts/add_weight_tracking.html')


@login_required
def delete_workout_result(request, result_pk):
    result = get_object_or_404(WorkoutResult, pk=result_pk, user=request.user)
    result.delete()
    return redirect('profile')

@login_required
def delete_weight_tracking(request, pk):
    weight_entry = get_object_or_404(WeightTracking, pk=pk, user=request.user)
    weight_entry.delete()
    return redirect('profile')