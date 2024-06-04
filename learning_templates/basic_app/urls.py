from django.urls import path, include
from . import views

# TEMPLATE TAGGING
app_name = 'basic_app' #  Django automatically will go to find this 

urlpatterns = [
    path('other/',views.other, name='other'),
    path('relative/',views.relative, name='relative'),
]
