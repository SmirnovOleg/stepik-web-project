from django import forms
from django.shortcuts import get_object_or_404
from .models import Question, Answer, User
from .actions import hash


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question.pk


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, question_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._question_id = question_id

    def save(self):
        question = get_object_or_404(Question, pk=self._question_id)
        answer = Answer(text=self.cleaned_data['text'], question=question)
        answer.save()
        return answer


class SignUpForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        hashed_pass = hash(self.cleaned_data['password'])
        user = User(login=self.cleaned_data['login'], password=hashed_pass)
        user.save()
        return user


class LoginForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
