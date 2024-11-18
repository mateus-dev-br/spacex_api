
from django.urls import path
from spacex import views
urlpatterns = [
    path('', views.home, name ='home' ),
]
