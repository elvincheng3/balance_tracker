from app import get_purchases
import requests
import json

s = requests.Session()

add_purchase_url = "http://127.0.0.1:5000/new/purchase/"
get_purchases_url = "http://127.0.0.1:5000/data/purchases/"
data = {
    "date": "2021-06-02",
    "sku": "CP9652",
    "size": "M 10",
    "location": "Footlocker",
    "price": 102.93
}

post_purchase = s.post(add_purchase_url, json=data)
# get_purchases = s.get(get_purchases_url)
# print(get_purchases.text)