from django.db import models


class User(models.Model):
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.login


class Session(models.Model):
    key = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    expires = models.DateTimeField()

    def __str__(self):
        return self.key


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
