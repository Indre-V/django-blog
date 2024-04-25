from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) 
    # This means that we can now leave some posts in Draft while we finish them, and they will not show up on the live blog.
    template_name = "post_list.html"
