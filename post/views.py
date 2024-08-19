from django.shortcuts import render
from django.views.generic import ListView, CreateView

from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

# view to allow user to upload images/comments  'forms.py'
class CreatePostView(CreateView):
    model = Post
    template_name = 'post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
