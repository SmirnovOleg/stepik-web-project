from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta
from django.views.decorators.http import require_POST
from .forms import AnswerForm, AskForm, SignUpForm, LoginForm
from .models import Question, Answer, Session
from .actions import do_login, paginate
from .decorators import require_login


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


@require_login
@require_POST
def write_answer(request, question_id):
    form = AnswerForm(request.POST)
    form._question_id = question_id
    form._user = request._user
    if (form.is_valid()):
        form.save()
        return HttpResponseRedirect('/question/{0}/'.format(question_id))
    else:
        return question(request, question_id)


def question(request, question_id):
    if (request.method == 'POST'):
        return write_answer(request, question_id)
    else:
        form = AnswerForm()
        form._question_id = question_id
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'qa/question.html', {'question': question, 'form': form})


@require_login
def ask(request):
    if (request.method == 'POST'):
        form = AskForm(request.POST)
        form._user = request._user
        if (form.is_valid()):
            question_id = form.save()
            return HttpResponseRedirect('/question/{0}/'.format(question_id))
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def signup(request):
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'qa/signup.html', {'form': form})


def login(request):
    error = ''
    if (request.method == 'POST'):
        form = LoginForm(request.POST)
        if (form.is_valid()):
            login = request.POST.get('login')
            password = request.POST.get('password')
            sessid = do_login(login, password)
            if (sessid):
                response = HttpResponseRedirect('/')
                response.set_cookie(
                    key='sessid',
                    value=sessid,
                    path='/',
                    httponly=True,
                    expires=datetime.now() + timedelta(days=1)
                )
                return response
            else:
                error = 'Incorrect login or password'
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', {'form': form, 'error': error})


def logout(request):
    sessid = request.COOKIES.get('sessid')
    if (sessid is not None):
        Session.objects.filter(key=sessid).delete()
    return HttpResponseRedirect('/')
