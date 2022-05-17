from django.shortcuts import render
from rest_framework import viewsets
from crawled_data.serializers import  UserInputSerializer
from crawled_data.models import UserInput


# class BoardDataViewSet(viewsets.ModelViewSet):
#     serializer_class = BoardDataSerializer
#     queryset = BoardData.objects.all()

class UserInputViewSet(viewsets.ModelViewSet):
    serializer_class = UserInputSerializer
    queryset = UserInput.objects.all()

# class WordCloudViewSet(viewsets.ModelViewSet):
#     serializer_class = WordCloud
#     queryset = WordCloud.objects.all()