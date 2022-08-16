from django.views import generic
from django.db.models import Avg

from .models import Posts, PostsAssessments, PostsComments


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
        context['comments'] = PostsComments.objects.filter(post=context['object'].pk)
        context['avg_assessment'] = PostsAssessments.objects.filter(post=context['object'].pk).aggregate(Avg('assessment'))['assessment__avg']
        if context['avg_assessment'] == None:
            context['avg_assessment'] = ''
        context['avg_assessment'] = round(context['avg_assessment'], 2)
        return context
