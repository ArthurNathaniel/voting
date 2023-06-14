from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('nomination', views.nomination, name='nomination'),
    path('contestants/<str:slug>', views.contestants, name='contestants_page'),

]
