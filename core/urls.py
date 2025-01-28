from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', views.home, name='home'),
    path("", index, name="index"),
    path('demanda/<int:pk>/', views.demanda_detail, name='demanda_detail'),
    path('demanda/create/', views.demanda_create, name='demanda_create'),
    path('demanda/<int:pk>/update/', views.demanda_update, name='demanda_update'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('demanda/<int:pk>/concluir/', views.concluir_demanda, name='concluir_demanda'),  # Nova URL para concluir demanda
    path('api/events/', views.get_events, name='get_events'),  # Adicione esta linha
]
