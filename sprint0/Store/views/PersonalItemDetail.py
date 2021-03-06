__author__ = 'brock'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required

templater = get_renderer('Store')

@view_function
def process_request(request):
    params = {}
    params['persProduct'] = hmod.PersonalProduct.objects.get(id=request.urlparams[0])

    return templater.render_to_response(request, 'PersonalItemDetail.html', params)
