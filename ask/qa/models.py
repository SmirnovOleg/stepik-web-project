from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def new(self):
        return self.get_queryset().order_by('-added_at')

    def popular(self):
        return self.get_queryset().order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes_set', blank=True)
    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.CharField(max_length=300)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(
        Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text
