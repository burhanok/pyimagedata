from django.urls import path
from . import views

urlpatterns = [
    path("opencv/",views.opencv, name="opencv"),
    path("yolo/",views.yolo, name="yolo"),
    path("objectdetection/",views.objectdetection, name="objectdetection"),
]
