
from django.urls import path
from .views import index, success_reserv



app_name = 'cafe_app'


urlpatterns = [
    path('', index, name='index'),
    path('succes/', success_reserv, name='success'),
]
