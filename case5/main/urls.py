from django.urls import path, include
from .views import index


urlpatterns = [
	path('', index),
    path('administrator/', include('administrator.urls')),
    path('user/', include('user.urls'))
]
