from django.urls import path

from . import views

urlpatterns = [
    path('', views.details.as_view(), name='details'),
]