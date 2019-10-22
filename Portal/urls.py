from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.contrib.auth import logout

from . import views

urlpatterns = [
    path('', views.index),
	path('', include('social_django.urls', namespace='social')),
	path('logout/', views.logout_view, name='logout'),
]
