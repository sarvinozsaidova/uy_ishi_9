from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'singlepost.html',{'post':post})