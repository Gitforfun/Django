from django.shortcuts import render
from django.template import Template, Context
from django.utils.html import mark_safe
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse

# Create your views here.
def index(request):
    #CONST = True
    #template = Template('<h1>{{ variable }}</h1>')

    #if CONST:
    #    context_value = {'variable':'Hello'}
    #else:
    #    context_value = {'variable':'World'}
    #context = Context(context_value)
    #return HttpResponse(
    #    template.render(context)
    #)
    # return render(request, 'index.html')
    # template = get_template('index.html')
    # context ={'description': 'Главная страница Интернет магазина'}
    # return HttpResponse(
    #     template.render(context)
    return render(
        request,
        'index.html',
        {
            'contacts': [
                'Контакт1', 'Контакт1','Контакт1','Контакт1',
            ]
        }
    )


def catalog(request):
    return HttpResponse(
        render_to_string(
            'catalog.html',
            {'description': 'Информационная страницы'}
        )
    )
        #render(request, 'catalog.html')


def contacts(request):
    return render(request, 'contacts.html')
