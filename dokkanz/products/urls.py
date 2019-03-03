from django.conf.urls import url, include
from rest_framework import routers

from products.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls), name='products')

]
