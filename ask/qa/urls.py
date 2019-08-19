from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.index, name='login'),
    path('signup/', views.index, name='signup'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.index, name='new'),
    path('', views.index, name='index')
]
