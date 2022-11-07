import requests

import json

def send_sms(number, message):
    url = 'https:fast2sms.com/dev/bulk'