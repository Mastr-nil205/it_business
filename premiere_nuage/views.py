from django.http import HttpResponse
from django.template import loader, Context, Template

# Create your views here.
def home(request):
    template = loader.get_template('premiere_nuage/index.html')
    context = {
        "name": "Premiere Nuage",
        }
    return HttpResponse(template.render(context, request))