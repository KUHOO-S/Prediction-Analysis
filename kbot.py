import telebot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import random

bot = telebot.TeleBot("BOT TOKEN", parse_mode=None)




def verify_temp():
    now = datetime.now()
    dateof=str(now)
    finalls=dateof.split(':')
    data=str(finalls[0])+':00:00'
    datalist=[]
    datalist[:0]=data
    data=''.join(datalist[0:])
    print(data)

    # TAKING DATA FROM RESULT
    dataset = pd.read_csv('temp_result.csv')
    temp=dataset.iloc[:, 2].values
    y = dataset.iloc[:, 1].values

    
    for i in range(len(y)):
        #turn to today's date
        change=list(y[i])
        change[2]='2'
        change[3]='0'
        y_result=''.join(change)

        if(data==y_result):
            print("yaa")
            fl=1
            print(temp[i])
            return round(temp[i],2)
    
def verify_aqi():
    now = datetime.now()
    dateof=str(now)
    finalls=dateof.split(':')
    data=str(finalls[0])+':00:00'
    datalist=[]
    datalist[:0]=data
    data=''.join(datalist[0:])
    print(data)

    # TAKING DATA FROM RESULT
    dataset = pd.read_csv('air_result.csv')
    aqi=dataset.iloc[:, 2].values
    y = dataset.iloc[:, 1].values

    
    for i in range(len(y)):
        #turn to aaj ka date
        change=list(y[i])
        change[2]='2'
        change[3]='0'
        y_result=''.join(change)

        if(data==y_result):
            print("yaa")
            fl=1
            print(aqi[i])
            return round(aqi[i], 2)
    i
def verify_water():
    dataset = pd.read_csv('water_result.csv')
    bod=dataset.iloc[:, 2].values
    y = dataset.iloc[:, 1].values

    x=random.randint(0,len(y))
    print(y[x])
    print(bod[x])
    return [y[x],round(bod[x],2)]

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,"Good day sir,\nSo here are the rules: \n/temp for Temperature\n/AQI for Air Quality Index\n/water for BOD levels of water\nHappy Botting!")


@bot.message_handler(commands=['temp','Temp'])
def send_temp(message):
    bot.reply_to(message, str(verify_temp())+" degrees celcius")

@bot.message_handler(commands=['aqi','AQI'])
def send_aqi(message):
    print(verify_aqi())
    m = str(verify_aqi())+" AQI\n"
    bot.reply_to(message, m)


@bot.message_handler(commands=['water','Water'])
def send_water(message):
    bot.reply_to(message, str(verify_water()[1])+" mg/l in "+ str(verify_water()[0]))

@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "About us\nPredii Bot is here to help :)")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Ahh seems like I'm not familiar with what you're saying .Try these :\n/temp for Temperature\n/AQI for Air Quality Index\n/water for BOD levels of water\nHappy Botting!")

bot.polling()