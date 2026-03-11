from django.urls import path
from .views import home, store

urlpatterns = [
    path('', home, name='home'),
    path('store/', store, name='store'),
]