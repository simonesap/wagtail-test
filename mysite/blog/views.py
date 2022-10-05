from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

from .forms import AuthorForm

from .models import Author

def get_name(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            obj = Author(name=form.data['name'],surname=form.data['surname'],date_of_birthday=form.data['date_of_birthday'])
            obj.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = AuthorForm()

    return render(request, 'blog/form.html', {'form': form})


def get_thanks(request):
    return render(request, 'blog/thanks.html')

