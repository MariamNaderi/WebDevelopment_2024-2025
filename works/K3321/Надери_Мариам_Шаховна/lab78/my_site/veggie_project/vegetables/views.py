from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Vegetable

def home(request):
    vegetables = Vegetable.objects.all()
    return render(request, 'index.html', {'vegetables': vegetables})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = FeedbackForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')