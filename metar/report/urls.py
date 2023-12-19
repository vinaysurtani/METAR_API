from django.urls import path
from . import views

urlpatterns = [
    path("ping",views.ping,name="ping"),
    path("info/",views.info,name="info")
]