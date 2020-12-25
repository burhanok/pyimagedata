from django.urls import path
from . import views

urlpatterns = [
    #path("",views.index, name="index"),
    path("machinelearning/",views.machinelearning, name="machinelearning"),
    path("deeplearning/",views.deeplearning, name="deeplearning"),
    path("rflearning/",views.rflearning, name="rflearning"),
    path("datascience/",views.datascience, name="datascience"),
    path("selfdrivingcar/",views.selfdrivingcar, name="selfdrivingcar"),
]
