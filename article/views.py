from django.shortcuts import render
from .models import Article

# Create your views here.

def deneme(request):
    articles = Article.object.create(title = "Deneme", content = "sdfgh dfghj dffghj")
    
    