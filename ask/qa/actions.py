from hashlib import md5
from uuid import uuid4
from datetime import datetime, timedelta
from .models import User, Session


def hash(password):
    hashed_pass = md5(password.encode()).hexdigest()
    return hashed_pass


def do_login(login, password):
    try:
        user = User.objects.get(login=login)
    except User.DoesNotExist:
        return None
    hashed_pass = hash(password)
    if (user.password != hashed_pass):
        return None
    session = Session()
    session.key = uuid4().hex
    session.user = user
    session.expires = datetime.now() + timedelta(days=1)
    session.save()
    return session.key
