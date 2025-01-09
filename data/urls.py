from django.urls import path, include
from . import views

urlpatterns = [
    path('upload/',views.UploadData.as_view(), name='data'),
    path('edit/', views.EditData.as_view(), name="Edit")
]