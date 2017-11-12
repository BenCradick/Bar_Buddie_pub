from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
 
from . import views
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Charges API', description='RESTful API for Charges')),
 
    url(r'^$', views.api_root),
    url(r'^', include('./users.urls', namespace='users')),
    url(r'^', include('./charges.urls', namespace='charges')),
]