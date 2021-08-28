from django.contrib import admin
from django.urls import path, include
from login.views import ListUsers, CustomAuthToken

from login.views import registration_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    # path('recordandcoin/', include('mainproject.urls')),
    path('', include('login.urls')),
    path('api/users/', ListUsers.as_view()),
    path('api/token/', CustomAuthToken.as_view()),
    path('api/register/', registration_view, name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



