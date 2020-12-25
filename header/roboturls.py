from django.urls import path
from . import views

urlpatterns = [
    path("ros/",views.ros, name="ros"),
    path("raspberrypi/",views.raspberrypi, name="raspberrypi"),
    path("arduino/",views.arduino, name="arduino"),
]
