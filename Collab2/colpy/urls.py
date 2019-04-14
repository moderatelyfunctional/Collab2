from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),
    path('space/<custom_url>', views.space),
    path('space/run_python/', views.run_python),
    path('delete_space/', views.delete_space),
]
