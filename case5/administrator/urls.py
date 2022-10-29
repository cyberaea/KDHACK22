from django.urls import path, include
from .views import admin_main


urlpatterns = [
	path('', admin_main),
]
