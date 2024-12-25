from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecordForm
from .models import Record

@login_required
def records_view(request):
    records = [
        {
            'name': 'Жим лежа',
            'key': 'bench_press',
            'data': Record.objects.filter(category='bench_press', is_approved=True),
        },
        {
            'name': 'Приседание со штангой',
            'key': 'squat',
            'data': Record.objects.filter(category='squat', is_approved=True),
        },
        {
            'name': 'Становая тяга',
            'key': 'deadlift',
            'data': Record.objects.filter(category='deadlift', is_approved=True),
        },
    ]
    return render(request, 'records/records.html', {'records': records})


@login_required
def add_record_view(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('records:records')
    else:
        form = RecordForm()
    return render(request, 'records/add_record.html', {'form': form})