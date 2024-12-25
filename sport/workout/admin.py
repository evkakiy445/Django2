from django.contrib import admin
from .models import WorkoutProgram, MuscleGroup, Exercise, FavoriteProgram, UserWeightHistory, WeightTracking, WorkoutResult

admin.site.register(WorkoutProgram)
admin.site.register(MuscleGroup)
admin.site.register(Exercise)
admin.site.register(FavoriteProgram)
admin.site.register(UserWeightHistory)
admin.site.register(WeightTracking)
admin.site.register(WorkoutResult)