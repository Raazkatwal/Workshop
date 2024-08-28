from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')
    output = "<br><br>".join(q.question_text for q in latest_question_list)
    return HttpResponse(output)


def view(request, question_id):
    response = "You are looking at question %s"
    return HttpResponse(response %question_id)


def results(request, question_id):
    response = "You are looking at the results of question id %s"
    return HttpResponse(response %question_id)


def vote(request, question_id):
    response = "You are voting on question %s"
    return HttpResponse(response %question_id)