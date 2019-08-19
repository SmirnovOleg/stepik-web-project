from django import forms
from .models import Question, Answer
from django.shortcuts import get_object_or_404


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
