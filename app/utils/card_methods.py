import requests
from utils import header
from utils import signature
import logging

# client_request_id
#brand
#face value (amount, currencty)
#amount

data = {
   "client_request_id": str(signature.client_request_id),
   "brand": "tesco",
   "face_value": {
       "amount": 10,
       "currency": "GBP"
   },
   "delivery_method": "code",
   "fulfilment_by": "rewardcloud",
   "fulfilment_parameters": {
       "to_name": "Receiver",
       "to_email": "vlad@reward.cloud",
       "from_name": "Reward Cloud",
       "from_email": "noreply@reward.cloud",
       "subject": "[TestCode] Here is your gift card!"
   },
   "personalisation": {
       "to_name": "Recipient",
       "from_name": "Sender",
       "message": "Here is your gift",
       "template": "standard"
   },
   "sector": "voluntary-benefits"
}

base_url = "https://app.sandbox.reward.cloud/api/v2"
def issue_card(brand, value):
    url = base_url + "/digital/issue"
    print()
    print()
    print(url)
    headers = header.generate_branded_header("POST", brand, value)
    response = requests.request("POST", url, data = data, headers = headers)
    return response.text

def get_brand_info():
    url = base_url + "/brands"
    headers = header.generate_branded_header("POST", "nike", 12)
    response = requests.get(url, headers = headers)
    return response.content

print(issue_card("tesco", 10))