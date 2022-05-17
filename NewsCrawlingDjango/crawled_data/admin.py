from django.contrib import admin

# Register your models here.
from crawled_data.models import BoardData, UserInput

admin.site.register(BoardData)
admin.site.register(UserInput)