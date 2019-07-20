# -*- coding: utf-8 -*-
import os
import telebot
# import some_api_lib
# import ...
from urllib import request
import json
from time import sleep

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
yt_id = os.environ['YT_ID']
yt_KEY = os.environ['API_KEY']
#             ...

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...

bot = telebot.TeleBot(token)

data = request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + yt_id + "&key=" + yt_key).read()
oldSubs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

# @bot.message_handler(commands=['acorde', 'help'])
# def send_message(message):
# 	bot.reply_to(message, 'Bom dia!')
	
# @bot.message_handler(command=['subs'])
# def send_message(message):
# 	
# 	bot.reply_to(message, 'oldSubs')

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

# bot.polling()

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            bot.send_message(chatid, text)


bot.set_update_listener(listener) #register listener
bot.polling()
#Use none_stop flag let polling will not stop when get new message occur error.
bot.polling(none_stop=True)
# Interval setup. Sleep 3 secs between request new message.
bot.polling(interval=3)

while True: # Don't let the main Thread end.
    pass
