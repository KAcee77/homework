from celery import shared_task
from django.utils.timezone import pytz
from .models import Btc
import requests
import dateutil.parser


@shared_task
def get_btc():
    headers = {
        'X-CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd',
        'Accept': 'application/json',
    }

    params = (
        ('id', '1'),
    )

    response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest',
                            headers=headers, params=params)

    price = response.json()['data']['1']['quote']['USD']['price']

    timestamp = response.json()['status']['timestamp']
    date = dateutil.parser.parse(timestamp)
    user_timezone = pytz.timezone('Europe/Moscow')
    date_in_moscow_tz = date.astimezone(user_timezone)

    Btc.objects.create(price=price, timestamp=date_in_moscow_tz)
