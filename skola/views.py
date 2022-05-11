from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
#from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    print(request.user)
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

#def about(request):
  #  template = loader.get_template('about.html')
 #   return HttpResponse(template.render({}, request))

#def contact(request):
   # template = loader.get_template('contact.html')
  #  return HttpResponse(template.render({}, request))

#class ProfileView(LoginRequiredMixin,TemplateView):
 #   template_name = 'accounts/profile.html'
