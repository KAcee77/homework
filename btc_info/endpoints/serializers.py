from rest_framework import serializers
from getter_btc.models import Btc


class BtcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Btc
        fields = '__all__'
