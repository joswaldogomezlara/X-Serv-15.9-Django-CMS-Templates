from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context


# Create your views here.

@csrf_exempt
def pages_handler(request, page_name):

    if request.method == 'GET':

        try:
            page = Pages.objects.get(name=page_name)
            respuesta = page.body
        except Pages.DoesNotExist:
            respuesta = 'No existe esa pagina'

        return HttpResponse(respuesta)

    else:

        page = Pages(name=page_name, body=request.body)
        page.save()

        return HttpResponse('Pagina ' + page_name + ' creada correctamente')

@csrf_exempt
def templates_handler(request, page_name):

    template_NewPage = get_template('template_NewPage.html')
    template_ShowPage = get_template('template_ShowPage.html')

    if request.method == 'GET':

        try:
            page = Pages.objects.get(name=page_name)
            respuesta = template_ShowPage.render(Context({'body': page.body}))
        except Pages.DoesNotExist:
            respuesta = 'No existe esa pagina'

        return HttpResponse(respuesta)

    else:

        page = Pages(name=page_name, body=request.body)
        page.save()

        return HttpResponse(template_NewPage.render(Context({'name': page.name})))

