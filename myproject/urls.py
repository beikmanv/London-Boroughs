from django.contrib import admin
from django.urls import path, include
from newapp import views  # Make sure to import the views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Add this line to include the root URL
    path('ai/', include('newapp.urls')),  # Include the URLs from your app
]
