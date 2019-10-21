from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.contrib.auth import logout

from . import views

urlpatterns = [
    # Form-based interface: server-side only
	path('rooms/', views.room_form, name="room_form"),

    path('rooms/<int:room_id>/nodes/', views.node_form, name="node_form"),
    path('rooms/<int:room_id>/nodes/<int:node_id>/<slug:capability>', views.capability_form, name="capability_form"),

	path('', views.index),
	path('', include('social_django.urls', namespace='social')),
	path('logout/', views.logout_view, name='logout'),
]
