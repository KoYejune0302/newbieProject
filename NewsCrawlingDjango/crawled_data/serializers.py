from rest_framework import serializers
from crawled_data.models import  UserInput, BoardData

class BoardDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardData
        fields = '__all__'
    
class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = '__all__'
