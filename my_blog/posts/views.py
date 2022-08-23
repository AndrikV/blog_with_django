import os

from django.views import generic, View
from django.db.models import Avg
from django.http import (
    HttpResponse, HttpResponseRedirect,
    HttpResponseBadRequest
)
from django.shortcuts import render

from .models import Posts, PostsAssessments, PostsComments, PostsMedia
from .forms import CommentForm


class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_5_posts'

    def get_queryset(self):
        """Return the last five published posts."""
        latest_5_posts = Posts.objects.order_by('-datetime_of_publication')[:5]
        return latest_5_posts


class DetailView(generic.DetailView):
    model = Posts
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = PostsComments.objects.filter(
            post=context['object'].pk)
        context['avg_assessment'] = PostsAssessments.objects.filter(
            post=context['object'].pk).aggregate(Avg('assessment'))['assessment__avg']
        context['avg_assessment'] = round(
            context['avg_assessment'], 2) if context['avg_assessment'] != None else ''

        return context


def create_new_comment(request, pk: int):
    if request.method == 'GET':
        form = CommentForm()
        return render(request, 'posts/new_comment.html', {'form': form})
    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = PostsComments(
                post=Posts.objects.filter(pk=pk)[0],
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text']
            )
            new_comment.save()
            return HttpResponseRedirect(f'/posts/{pk}')
    return HttpResponseBadRequest('Bad request')


def get_media(request, post_pk: int, media_name: str):
    if request.method == 'GET':
        queryset = PostsMedia.objects.filter(
            post=Posts.objects.filter(pk=post_pk)[0]
        )
        queryset.filter(media_name=media_name)
        if queryset.exists():
            django_file = queryset[0].media_file
            with django_file.open(mode='rb') as f:
                return HttpResponse(
                    f.read(),
                    headers={
                        'Content-Type': 'application/vnd.ms-excel',
                        'Content-Disposition': f'attachment; filename="{django_file.name}"',
                    }
                )
    return HttpResponseBadRequest('Bad request')


class Item:
    def __init__(self, post_pk: int, media_name: str):
        self.post_pk = post_pk
        self.media_name = media_name


class ShowMedia(View):
    def get_extension(self, path: str) -> str:
        *_, extension = os.path.splitext(path)
        return extension

    def get(self, request, media_name: str):
        if request.method == 'GET':
            search_results = PostsMedia.objects.filter(media_name=media_name)
            context = {'images': []}
            for result in search_results:
                django_file = result.media_file
                if self.get_extension(django_file.path) in ['.png', '.jpg']:
                    context['images'].append(Item(
                        result.post.pk,
                        result.media_name
                    ))
                    print(context['images'])
            return render(request, 'posts/show_files.html', context)

        return HttpResponseBadRequest('Bad request')
