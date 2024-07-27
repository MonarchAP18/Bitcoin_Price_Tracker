import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tanxfi_task_project.settings')
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import json

#sched = BlockingScheduler()

#@sched.scheduled_job('interval', minutes = 1)
coingeko_api = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
coindesk_api = "https://api.coindesk.com/v1/bpi/currentprice.json"


def bitcoin_price_alert():
    get_bitcoin_price = requests.get(coindesk_api)
    result = json.loads(get_bitcoin_price.text)
    current_price = result['bpi']['USD']['rate_float']
    print(current_price)


bitcoin_price_alert()
#sched.start()