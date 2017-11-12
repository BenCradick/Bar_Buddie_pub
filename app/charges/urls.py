from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from charges import views
 
urlpatterns = [
    url(r'^charges/$', views.Charges.as_view(), name='charges-list'),
    url(r'^charges/(?P<pk>[0-9]+)/$', views.ChargesDetail.as_view(), name='charges-detail'),
]