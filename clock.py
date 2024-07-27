import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tanxfi_task_project.settings')
import django
django.setup()
from django.core.mail import send_mail
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import json

#sched = BlockingScheduler()

#@sched.scheduled_job('interval', minutes = 1)
coingeko_api = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
coindesk_api = "https://api.coindesk.com/v1/bpi/currentprice.json"

user_alert_Price = 30000
def bitcoin_price_alert():
    get_bitcoin_price = requests.get(coindesk_api)
    result = json.loads(get_bitcoin_price.text)
    current_price = result['bpi']['USD']['rate_float']
    #print(current_price)

    #Check if the price is beneth User price
    if current_price < user_alert_Price:
        send_mail(
            "Drop in BTC Price",
            "Current BTC price is {}".format(current_price),
            "akshaypadamwar12@gmail.com",
            ["aclark.amelia@gmail.com"],
            fail_silently=False,
            )


    if current_price > user_alert_Price:
        send_mail(
            "Rise in BTC Price",
            "Current BTC price is {}".format(current_price),
            "akshaypadamwar12@gmail.com",
            ["aclark.amelia@gmail.com"],
            fail_silently=False,
            )
        


bitcoin_price_alert()
#sched.start()