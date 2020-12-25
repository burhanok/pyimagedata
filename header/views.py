from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

# Ai

def machinelearning(request):
    return render(request, "header/ai/machinelearning.html")

def deeplearning(request):
    return render(request, "header/ai/deeplearning.html")

def rflearning(request):
    return render(request, "header/ai/rflearning.html")

def datascience(request):
    return render(request, "header/ai/datascience.html")

def selfdrivingcar(request):
    return render(request, "header/ai/selfdrivingcar.html")

# Computer Vision

def opencv(request):
    return render(request, "header/computervision/opencv.html")

def yolo(request):
    return render(request, "header/computervision/yolo.html")

def objectdetection(request):
    return render(request, "header/computervision/objectdetection.html")

# Robotics

def ros(request):
    return render(request, "header/robotics/ros.html")

def raspberrypi(request):
    return render(request, "header/robotics/raspberrypi.html")

def arduino(request):
    return render(request, "header/robotics/arduino.html")

# Programming

def python(request):
    return render(request, "header/programming/python.html")

def cplusplus(request):
    return render(request, "header/programming/cplusplus.html")

def webdevelopment(request):
    return render(request, "header/programming/webdevelopment.html")

def golang(request):
    return render(request, "header/programming/golang.html")

def javascript(request):
    return render(request, "header/programming/javascript.html")


# engineering

def controltheory(request):
    return render(request, "header/engineering/controltheory.html")

def scipy(request):
    return render(request, "header/engineering/scipy.html")