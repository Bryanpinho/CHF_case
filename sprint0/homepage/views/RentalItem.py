
__author__ = 'brock'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params['users'] = hmod.User.objects.all()

    try:
        rental = hmod.Rental.objects.get(id=5)
    except hmod.Rental.DoesNotExist:
        print("There is something terribly wrong!!!")

    return templater.render_to_response(request, 'RentalItem.html', params)