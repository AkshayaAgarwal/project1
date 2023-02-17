from django.contrib import admin
from django.urls import include,path
from .import views

urlpatterns = [
    path('',include('Users.urls')),
    path("admin/", admin.site.urls),
    path('',views.Gather)
    
]