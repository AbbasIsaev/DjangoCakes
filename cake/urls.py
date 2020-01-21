from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowCakesView.as_view(), name='index'),
    path('cake/<uuid:pk>/', views.CakeDetailView.as_view(), name='cake_detail'),
    path('contact/', views.contact, name='contact'),
]
