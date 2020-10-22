from django.urls import path
from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

appname = 'csp'
urlpatterns = [
    path('csp/', views.csp, name='csp'),
]
urlpatterns += staticfiles_urlpatterns()