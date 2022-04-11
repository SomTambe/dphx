from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('HX/', include('HX.urls')),
    path('admin/', admin.site.urls),
]
