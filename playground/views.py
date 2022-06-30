from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def say_hello(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'home.html', context)

#def for about us
def about_page(request):
    return render(request, 'about.html', {'title':'about'})
# Create your views here.
