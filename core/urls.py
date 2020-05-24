from django.contrib import admin
from django.urls import path, include
from game import views


urlpatterns = [
    path('players', views.PlayerList.as_view()),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
