
import requests
def send_top_code(phone_number,code):

        data = {'from': '50002710017796', 'to': phone_number, 'text': f'{code}کاربر گرامی کد تایید شما: '}
        response = requests.post('https://console.melipayamak.com/...', json=data)





