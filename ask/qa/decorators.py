from functools import wraps
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Session


def require_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        print(request._user)
        if (request._user is not None):
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/')

    return inner
