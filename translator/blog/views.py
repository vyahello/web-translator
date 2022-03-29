from django.views import generic

from .models import Post


class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'
