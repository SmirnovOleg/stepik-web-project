from .models import Session
from datetime import datetime


def CheckSessionMiddleware(get_response):

    def middleware(request):
        sessid = ''
        try:
            sessid = request.COOKIES.get('sessid')
            session = Session.objects.get(
                key=sessid, expires__gt=datetime.now())
            request._session = session
            request._user = session.user
        except:
            request._session = None
            request._user = None
        response = get_response(request)
        return response

    return middleware
