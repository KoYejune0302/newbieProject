from rest_framework import serializers
from crawled_data.models import  UserInput

# class BoardDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BoardData
#         fields = '__all__'
    
class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = ['startdate', 'finishdate']

# class WordCloudSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WordCloud
#         fields = '__all__'