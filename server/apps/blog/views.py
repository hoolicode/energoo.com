from django.shortcuts import render
from django.views import generic


class PostListView(generic.TemplateView):
    template_name = 'blog/post-list.j2'


class PostDetailView(generic.TemplateView):
    template_name = 'blog/post-detail.j2'