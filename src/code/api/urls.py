from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('queries/', views.queries, name='queries'),
    path('search/', views.search, name='search'),
]
