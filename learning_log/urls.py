from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('learning_logs.urls', namespace='learning_logs')),
]
urlpatterns += static(static.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
urlpatterns += static(static.STATIC_URL, document_root = settings.STATIC_ROOT) 

