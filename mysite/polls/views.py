from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


def view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You are looking at the results of question id %s"
    return HttpResponse(response %question_id)


def vote(request, question_id):
    response = "You are voting on question %s"
    return HttpResponse(response %question_id)