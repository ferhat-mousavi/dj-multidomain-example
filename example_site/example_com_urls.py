from django.urls import path, include

urlpatterns = [
    path('', include('example_com.urls')),
]