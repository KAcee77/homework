from rest_framework import routers
from django.urls import path
from .views import BtcViewSet, update_now

router = routers.SimpleRouter()
router.register(r'bitcoins', BtcViewSet)

urlpatterns = [
    path(r'update', update_now),
]

urlpatterns += router.urls