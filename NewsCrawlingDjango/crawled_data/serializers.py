from rest_framework import serializers
from crawled_data.models import  UserInput, BoardData, CrawlData

class BoardDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardData
        fields = '__all__'
    
class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = '__all__'

class CrawlDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawlData
        fields = '__all__'
