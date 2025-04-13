from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('main/index.html')
    context = {"Prenom": "Patrick"}
    return HttpResponse(template.render(context))

