from django.contrib import admin
from django.urls import path
from app.views import home, search, info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('search/',search),
    path("info/<int:id>/",info), 
]
