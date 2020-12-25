from django.urls import path
from . import views

urlpatterns = [
    path("controltheory/",views.controltheory, name="controltheory"),
    path("scipy/",views.scipy, name="scipy"),
]
