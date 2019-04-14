from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),
    path('space/<custom_url>', views.space)
]
