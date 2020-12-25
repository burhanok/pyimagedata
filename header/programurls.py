from django.urls import path
from . import views

urlpatterns = [
    path("python/",views.python, name="python"),
    path("cplusplus/",views.cplusplus, name="cplusplus"),
    path("webdevelopment/",views.webdevelopment, name="webdevelopment"),
    path("golang/",views.golang, name="golang"),
    path("javascript/",views.javascript, name="javascript"),
]
