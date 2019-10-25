from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.contrib.auth import logout

from . import views

urlpatterns = [
    # Form-based interface: server-side only
	path('room', views.room_form, name="room_form"),
    path('room/<int:room_id>/nodes/', views.node_form, name="node_form"),
    path('room/<int:room_id>/nodes/<int:node_id>/<slug:capability>', views.capability_form, name="capability_form"),
]
