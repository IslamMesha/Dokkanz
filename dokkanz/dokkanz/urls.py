"""dokkanz URL Configuration"""

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin_panel'),
    url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),
    url(r'^products/', include('products.urls'), name='products'),
    url(r'^docs$', get_swagger_view(title='Dokkanz API'))
]
