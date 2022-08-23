from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.db.models import Sum

from .models import Polls, Choices


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_5_polls'

    def get_queryset(self):
        """Return the last five published posts."""
        latest_5_polls = Polls.objects.order_by('-datetime_of_publication')[:5]
        return latest_5_polls


def handle_detail_view(request, poll_pk: int):
    if request.method == 'GET':
        poll = Polls.objects.filter(pk=poll_pk)[0]
        choices = Choices.objects.filter(poll=poll)

        context = {
            'question': poll.question,
            'description': poll.description,
            'datetime_of_publication': poll.datetime_of_publication,
            'allow_multi_choices': poll.allow_multi_choices,
            'number_of_votes': poll.number_of_votes,
            'choices': choices
        }
        return render(request, 'polls/detail.html', context)
    elif request.method == 'POST':
        if request.POST.get('choices') != None:
            poll = Polls.objects.filter(pk=poll_pk)[0]  
            is_any_correct_choice = False
            for choice in request.POST.getlist('choices'):
                db_choice = Choices.objects.filter(poll=poll).filter(name=choice)
                if not db_choice.exists():
                    continue
                is_any_correct_choice = True
                db_choice = db_choice[0]
                db_choice.number_of_times_selected += 1
                db_choice.save()

            if is_any_correct_choice:
                poll.number_of_votes += 1
                poll.save()
                return HttpResponseRedirect(f'results/')
    return HttpResponseBadRequest('Bad request')


def handle_results_view(request, poll_pk: int):
    queryset = Choices.objects.filter(poll__pk=poll_pk)
    votes_sum = queryset.aggregate(Sum('number_of_times_selected'))
    votes_sum = votes_sum['number_of_times_selected__sum']

    context = {'choices_results': {}}
    for choice in queryset:
        choice_result = choice.number_of_times_selected / votes_sum
        choice_result = round(choice_result * 100)
        context['choices_results'][choice.name] = choice_result

    context['choices_results'] = context['choices_results'].items()
    return render(request, 'polls/result.html', context)