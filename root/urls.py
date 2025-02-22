from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
    path('accounts/', include('allauth.urls')),  # Google login uchun kerak!

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
