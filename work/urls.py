from django.urls import path
from work import views

urlpatterns = [
    path("", views.index, name='signup'),
    path("login/", views.login, name='login'),
    path("home/", views.home, name='home'),
    path("chatbot/", views.chatbot, name='chatbot'),
    path("document/", views.document, name='document'),
]