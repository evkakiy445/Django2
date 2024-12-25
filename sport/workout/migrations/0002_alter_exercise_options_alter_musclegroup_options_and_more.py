# Generated by Django 5.1.3 on 2024-11-27 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'verbose_name': 'Упражнение', 'verbose_name_plural': 'Упражнения'},
        ),
        migrations.AlterModelOptions(
            name='musclegroup',
            options={'verbose_name': 'Группа мышц', 'verbose_name_plural': 'Группы мышц'},
        ),
        migrations.AlterModelOptions(
            name='workoutprogram',
            options={'verbose_name': 'Программа тренировки', 'verbose_name_plural': 'Программы тренировок'},
        ),
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='image',
            field=models.ImageField(upload_to='exercises/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='technique_description',
            field=models.TextField(verbose_name='Описание техники выполнения'),
        ),
        migrations.AlterField(
            model_name='musclegroup',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='musclegroup',
            name='image',
            field=models.ImageField(upload_to='muscle_groups/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='musclegroup',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='workoutprogram',
            name='description',
            field=models.TextField(verbose_name='Описание программы'),
        ),
        migrations.AlterField(
            model_name='workoutprogram',
            name='exercises',
            field=models.ManyToManyField(to='workout.exercise', verbose_name='Упражнения'),
        ),
        migrations.AlterField(
            model_name='workoutprogram',
            name='image',
            field=models.ImageField(upload_to='workout_programs/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='workoutprogram',
            name='muscle_groups',
            field=models.ManyToManyField(to='workout.musclegroup', verbose_name='Группы мышц'),
        ),
        migrations.AlterField(
            model_name='workoutprogram',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название программы'),
        ),
    ]
