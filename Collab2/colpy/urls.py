from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),
    path('space/<custom_url>', views.space),
    path('delete_space/', views.delete_space),
    path('space/run_python/', views.run_python),
    path('space/pull_python/', views.pull_python),
    path('space/update_python/', views.update_python),
    path('space/submit_python/', views.submit_python),
    path('space/fetch_submission/', views.fetch_submission),
]
