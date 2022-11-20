#Tracker that tracks the price of an stock and send an email notification about that specific stock 

#I am using financial model input for extracting data as from API  


from http import server
from mydata import password, api_key
import requests
import smtplib
import time

stock_name= 'GOOG'

data_set = requests.get(f'https://financialmodelingprep.com/api/v3/quote/' + stock_name + f'?apikey={api_key}').json()
#print(data_set)

symbol = data_set[0]['symbol']

name = data_set[0]['name']

stock_price = data_set[0]['price']
#print(stock_price)

def send_email(password):
    server = smtplib.SMTP('smtp-mail.outlook.com',587)
    server.ehlo()
    server.starttls()
    server.login('niraulashashwot1990@outlook.com',password)
    msg = """Subject : """ + str(name) + """ Stock Excusive

The price of """ + str(name) + """ (""" + symbol + """) """+ """has reached: """ + str(stock_price)

    server.sendmail(
        'niraulashashwot1990@outlook.com',
        'niraulashashwot1990@outlook.com',
        msg
    )
    print('email is sent')
    server.quit()

def check_stock():
    if stock_price < 100:
        send_email(password)    #send an email
    
while(True): #run for every 1 minute
    check_stock()
    time.sleep(60)


