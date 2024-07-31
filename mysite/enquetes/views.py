from django.http import HttpResponse, Http404
from django.template import loader
from .models import Pergunta
from django.shortcuts import render

def index(request):
    ultimas_perguntas = Pergunta.objects.order_by('-data_publicacao')[:5]
    template = loader.get_template('enquetes/index.html')
    contexto = {
        'ultimas_perguntas': ultimas_perguntas
    }
    return HttpResponse(template.render(contexto, request))

def detalhes(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(pk=pergunta_id)
    except:
        raise Http404("A pergunta não existe!")
    return render(request, 'enquetes/detalhes.html',{'pergunta': pergunta})

def resultados(request, pergunta_id):
    return HttpResponse(f"Você está vendo os resultados da pergunta {pergunta_id}")
def votos(request, pergunta_id):
    return HttpResponse(f"Você está votando na questão {pergunta_id}")