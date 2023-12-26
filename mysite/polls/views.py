from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question, Banner
from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404
from django.db.models import Q
from django.conf import settings


def entry_list(request, template='polls/index.html', page_template='polls/index_page.html'):
    context = {
        'entry_list': Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date'),
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    # 防止未来的问题url被猜到显示
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


@login_required(login_url='/login.html')
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def set_cookie(request):
    if request.GET.get('id', ''):
        raise Http404
    return render(request, 'polls/cookie.html')


def search(request):
    if request.method == 'GET':
        kword = request.session.get('kword', '')
        if kword:
            question_list = Question.objects.filter(Q(question_text__icontains=kword)).order_by('-pub_date').all()
            choice_list = Choice.objects.filter(Q(choice_text__icontains=kword)).order_by('-votes').all()
        else:
            question_list = Question.objects.order_by('-pub_date').all()[:20]
            choice_list = []
        return render(request, 'polls/search.html', {'question_list': question_list, 'choice_list': choice_list})
    else:
        request.session['kword'] = request.POST.get('kword', '')
        return redirect(reverse('polls:search'))


def show_banner(request):
    banner_list = Banner.objects.all().filter(is_delete=False, is_show=True).order_by('-orders')[:settings.BANNER_COUNT]
    return render(request, 'polls/banner.html', {'banner_list': banner_list})
