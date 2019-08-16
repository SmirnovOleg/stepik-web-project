from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer
from django.core.paginator import Paginator


def paginate(objects, page):
    paginator = Paginator(objects, per_page=2)
    return paginator.get_page(page)


def index(request):
    latest_question_list = Question.objects.new()
    page = request.GET.get('page')
    context = {'current_questions': paginate(latest_question_list, page)}
    return render(request, 'qa/index.html', context=context)


def popular(request):
    popular_question_list = Question.objects.popular()
    page = request.GET.get('page')
    context = {'current_questions': paginate(popular_question_list, page)}
    return render(request, 'qa/popular.html', context=context)


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'qa/question.html', {'question': question})
