from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('chat/', include('chat.urls')),
]