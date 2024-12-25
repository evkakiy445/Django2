from django import forms
from .models import Review
from workout.models import WorkoutProgram

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating', 'program']  # Оставляем только текст отзыва и рейтинг

    program = forms.ModelChoiceField(queryset=WorkoutProgram.objects.all(), required=False, empty_label="Без привязки к программе")
