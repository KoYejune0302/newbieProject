from django.urls import path
from crawled_data import views
from crawled_data.views import UserInputViewSet

user_list = UserInputViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

user_detail = UserInputViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    path('user/', user_list, name='user-list'),
    path('user/<int:pk>/', user_detail, name='user-detail'),
]
