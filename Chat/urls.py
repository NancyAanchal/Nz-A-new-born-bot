from . import views
from django.urls import path

urlpatterns = [
    path('',  views.index, name="index"),
    path('chat-with-nz', views.getResponse, name='getResponse')
]