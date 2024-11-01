from django.urls import path, include
from . import views

urlpatterns = [
    path('parks',views.getParks.as_view(), name='parks'),
    path('book/',views.bookPark.as_view(), name='book'),
    path('free/', views.freePark.as_view(), name='free'),
]