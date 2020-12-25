from django.shortcuts import render
from posts.models import DeepLearningPost

# Create your views here.

DeepLearningPost.objects.all()