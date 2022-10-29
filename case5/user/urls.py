from django.urls import path, include
from .views import user_main


urlpatterns = [
	path('', user_main)
]
