from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('count/', views.count, name='Xcount'),
    path('aboutus/',views.aboutus, name='aboutus'),
]
