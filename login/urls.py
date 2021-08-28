from django.urls import path

from django.conf.urls import include, url

from .import views


urlpatterns = [


    path('login/', views.login, name='login'),
    # url(r"^accounts/", include("django.contrib.auth.urls")),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutUser, name="logout"),


]
