#!usr/bin/python
#Track phone  umber from Buitenzorg Syndicate
#The owner of Api key is the Buitenzorg Syndicate

import requests
import os,sys

API_KEY = '3af2c73feb3f7b16c35ec42866b00932'

os.system('clear')
os.system('xdg-open https://youtube.com/@buitenzorgsyndicate')
print("-------------------------------")
print(" Buitenzorg Track Phone Number\n    Author by Prakasa_Jr644")
print("-------------------------------")
print("[•] Example: 62895xxxxxxxxx\n")
PHONE_NUMBER = input('[•] Input your number: ')

url = f'http://apilayer.net/api/validate?access_key={API_KEY}&number={PHONE_NUMBER}&country_code=&format=1'

response = requests.get(url)
data = response.json()

if data['valid']:
    os.system('clear')
    os.system('xdg-open https://youtube.com/@buitenzorgsyndicate')
    print("-------------------------------")
    print(" Buitenzorg Track Phone Number\n    Author by Prakasa_Jr644")
    print("-------------------------------")
    print('[•] The result of the phone number: '  + PHONE_NUMBER)
    print('\nType:', data['line_type'])
    print('Local Number:', data['local_format'])
    print('Country: ', data['country_name'])
    print('Carrier:', data['carrier'])
    print('Location:', data['location'])
    print('\n\n')
else:
    os.system('clear')
    os.system('xdg-open https://youtube.com/@buitenzorgsyndicate')
    print("-------------------------------")
    print(" Buitenzorg Track Phone Number\n    Author by Prakasa_Jr644")
    print("-------------------------------")
    print('[×] Invalid phone number.')
