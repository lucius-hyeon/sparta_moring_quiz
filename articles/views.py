from django.shortcuts import render
from .models import Article
from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.serializers import ArticleSerializer



@api_view(['GET','POST'])
def index(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        print(request.data)
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)