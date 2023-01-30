import requests
from decouple import config


class HomeBridgeController():

    def __init__(self):
        username = config('HB_USER')
        password = config('HB_PASS')
        self.base_url = config('HB_URL')
        res = requests.post(self.base_url+'/auth/login', json={
            "username": username,
            "password": password,
            "otp": ""
        })
        self.token = res.json()['access_token']
        print(self.token)

    def toggle_entrance_light(self, On=False):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        # print(headers)
        res = requests.put(
            self.base_url+'/accessories/5519af812b4fd0c97cbfd6a47c6637d374a4309669c5ad49a44aeaf39ff709d8',
            json={
                "characteristicType": "On",
                "value": 1 if On else 0
            },
            headers=headers
        )
        print(f'Light {"On" if On else "Off"}')
        # print(res.content)
