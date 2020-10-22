from django.urls import path
from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

appname = 'home'
urlpatterns = [
    path('', views.home, name='home'),
]
urlpatterns += staticfiles_urlpatterns()