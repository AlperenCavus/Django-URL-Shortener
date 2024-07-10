from django.urls import path
from .views import index, go, CreateShortURL

urlpatterns = [
    path('', index, name='index'),
    path('create/', CreateShortURL.as_view(), name='create'),
    path('<str:pk>/', go, name='go'),
]
