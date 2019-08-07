from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    added_at = models.DateTimeField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.CharField(max_length=300)
    added_at = models.DateTimeField()
    question = models.OneToOneField(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.text
