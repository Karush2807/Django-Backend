#jo bhi hmare urls call hote views se, vo initialyy yhn aate then yhn se apni respective application pr jaate 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('api.urls')), #jo url yhn aarhe unhe app ki urls.py pr dispath kroo
    path('', include('frontend.urls'))
]
