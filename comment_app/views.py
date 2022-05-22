from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_app-predictions')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'comment_app/index.html', context)

def predictions(request):
    spam_predict = Data.objects.all()
    context = {
        'spam_predict': spam_predict
    }
    return render(request, 'comment_app/predictions.html', context)