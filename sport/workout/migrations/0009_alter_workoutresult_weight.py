# Generated by Django 5.1.3 on 2024-12-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0008_alter_weighttracking_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutresult',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Вес (кг)'),
        ),
    ]
