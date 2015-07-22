__author__ = 'dheerendra'

from django.utils.decorators import method_decorator
from stronghold.decorators import public
from django.http import HttpResponse
from django.conf import settings
import os
from django.shortcuts import render

class StrongholdPublicMixin(object):

    @method_decorator(public)
    def dispatch(self, *args, **kwargs):
        return super(StrongholdPublicMixin, self).dispatch(*args, **kwargs)


def index(request):

    return render(request, 'iitbapp/index.html', {})


def logs(request):
    response = HttpResponse(content_type="text/plain")

    file = os.path.join(settings.BASE_DIR, 'logs/application.log')

    with open(file) as f:
        content = f.read()
        response.write(content)
    return response
