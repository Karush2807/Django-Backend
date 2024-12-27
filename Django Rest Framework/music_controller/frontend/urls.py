#jo bhi hmare urls call hote views se, vo initialyy yhn aate then yhn se apni respective application pr jaate 
from django.urls import path
from .views import index

urlpatterns = [
    path('', index)
]
