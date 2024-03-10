from django.urls import path
from . import views

urlpatterns = [
    path('poem/', views.poem),
    path('', views.start),

]