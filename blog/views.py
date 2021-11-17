from django.http.response import HttpResponse
from django.shortcuts import render

posts = [
    {
        'author': 'DangiV',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 19, 2021'
    }, 
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 20, 2021'
    }, 
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})
