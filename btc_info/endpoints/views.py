from rest_framework import viewsets
from getter_btc.models import Btc
from getter_btc.tasks import get_btc
from .serializers import BtcSerializer


class BtcViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = BtcSerializer
    queryset = Btc.objects.all()

def update_now(request):
    get_btc()

