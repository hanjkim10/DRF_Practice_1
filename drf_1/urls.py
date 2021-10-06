from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',
    include('accounts.urls')),
    re_path(r'^rest-auth/',
    include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/',
    include('rest_auth.registration.urls'))]

