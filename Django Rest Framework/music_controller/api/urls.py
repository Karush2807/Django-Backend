from django.urls import path
from .views import main #will call main fucntion from views file

urlpatterns=[
    path('', main)
]