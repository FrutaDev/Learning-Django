from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:month>', views.monnth_handler_by_number),
    path('<str:month>', views.month_handler, name="month-challenge"),
]