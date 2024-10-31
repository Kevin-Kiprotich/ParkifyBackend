from django.urls import path, include
from . import views

urlpatterns = [
    path('parks',views.getParks.as_view(), name='parks'),
]