from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ai_index/', views.ai_index, name='ai_index'),
]
