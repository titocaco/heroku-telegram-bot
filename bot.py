# -*- coding: utf-8 -*-
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
ID = os.envirin['YT_ID']
KEY = os.envirin['API_KEY']
#             ...

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...

bot = telebot.TeleBot(token)

data = request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + ID + "&key=" + KEY).read()
oldSubs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

@bot.message_handler(commands=['acorde', 'help'])
def send_message(message):
	bot.reply_to(message, 'Bom dia!')
	
@bot.message_handler(command=['subs'])
def send_message(message):
	bot.reply_to(message, 'Subs: ' + oldSubs)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
