from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', views.create),
    path('space/', views.gotospace),
    path('space/<custom_url>', views.space),
    path('delete_space/', views.delete_space),
    path('space/run_python/', views.run_python),
    path('space/pull_python/', views.pull_python),
    path('space/update_python/', views.update_python),
    path('space/submit_python/', views.submit_python),
    path('space/fetch_submission/', views.fetch_submission),
]
urlpatterns += static('space'+settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
