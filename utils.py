
import requests
def send_top_code(phone_number,code):

        data = {'from': '50002710017796', 'to': phone_number, 'text': f'{code}کاربر گرامی کد تایید شما: '}
        response = requests.post('https://console.melipayamak.com/api/send/simple/e97f2fd3453d4717bd528e07a8210f0d', json=data)





