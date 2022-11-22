#Tracker that tracks the price of an stock and send an email notification about that specific stock 

#I am using financial model input for extracting data as from API  


from http import server
from dotenv import load_dotenv
import requests, smtplib, time, os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('api_key')
password = os.environ.get('password')
email = os.environ.get('email')

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
    server.login(email,password)
    msg = """Subject : """ + str(name) + """ Stock Excusive

The price of """ + str(name) + """ (""" + symbol + """) """+ """has reached: """ + str(stock_price)

    server.sendmail(
        email,
        email,
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


