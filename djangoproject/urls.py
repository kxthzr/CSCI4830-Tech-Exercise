from django.contrib import admin
from django.urls import path
from hello_world_app.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
]
