from django.contrib import admin
from django.urls import path, include
from shop_auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ecommapp.urls")),
   path('authc/', include('shop_auth.urls')),
    # Add this line
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)