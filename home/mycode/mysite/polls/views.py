from django.shortcuts import get_object_or_404, render

from .models import Question
# ...


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = 'Você está procurando o resultado da questão %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('Você está votando na questão %s.' % question_id)
