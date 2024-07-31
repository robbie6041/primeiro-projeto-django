from. import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"), 
    path("<int:pergunta_id>/",views.detalhes,name="resultados"),
    path("<int:pergunta_id>/resultados/",views.resultados, name="resultados"),
    path("<int:pergunta_id>/votos/",views.votos,name="votos"),
]