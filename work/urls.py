from django.urls import path
from work import views

urlpatterns = [
    path("", views.index, name='signup'),
    path("login/", views.login, name='login'),
    path("home/", views.home, name='home'),
    path("chatbot/", views.chatbot, name='chatbot'),
    path("document/", views.document, name='document'),
    path("broken/", views.broken, name='broken'),
    path("authentication/", views.authentication, name='authentication'),
    path("injection/", views.injection, name='injection'),
    path("vulner/", views.vulner, name='vulner'),
    path("insecure/", views.insecure, name='insecure'),
    path("security/", views.security, name='security'),
    path("bug/", views.bug, name='bug'),
    path("pentest/", views.pentest, name='pentest'),
    path("system/", views.system, name='system'),
    path("awareness/", views.awareness, name='awareness'),
    path("article/", views.article, name='article'),
    path("podcast/", views.podcast, name='podcast'),
    path("contact/", views.contact, name='contact'),
]
