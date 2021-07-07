from flask import Flask, request
import telebot
import os
import logging
import sys
import re
from datetime import datetime



import func

def main():
    global mail,password,classno,bot
    mail=password=classno=''
    
    token = os.environ.get("TOKEN")
    bot = telebot.TeleBot(token)

    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info('Starting Bot...')



    
    app = Flask(__name__)


    l= ['/help','/login','/joinclass','/start','/mail','/password','/showchat','/photo']

    @app.route('/', methods=["POST"])
    def webhook():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200

    @bot.message_handler(commands=['start'])
    def command(message):
        bot.send_message(message.chat.id, 'Hi, ' + message.chat.first_name + '!')
        #login(message)



    @bot.message_handler(commands=['mail'])
    def command(message):
      try:
        mail=message.text.split()[1]
        print(mail)
        chkmail=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(chkmail,mail):
            print("valid mail")
            bot.send_message(message.chat.id, f" ok got your mail => {mail} now send your password like  /password yourpasswordhere ")
        else:
            bot.send_message(message.chat.id, f" not a  mail format : /mail yourmail@mail.com  /help !")

      except:
        bot.send_message(message.chat.id, f"format : /mail yourmail@mail.com ")


    @bot.message_handler(commands=['password'])
    def command(message):
      try:
        password=str(message.text.split()[1])

        bot.send_message(message.chat.id, f" ok got your password: {password} now   /joinclass number   ")
         #login(message)
      except:
        bot.send_message(message.chat.id, f"format : /password yourpass |  ")


    @bot.message_handler(commands=['joinclass'])
    def command(message):
      try:
        classno=int(message.text.split()[1])
        bot.send_message(message.chat.id, f" ok got your class number: {classno}  now enter /login ")
      except:
        bot.send_message(message.chat.id, f"format : /joinclass classno |  ")


    @bot.message_handler(commands=['login'])
    def command(message):
      try:
        bot.send_message(message.chat.id, f" ok wait im trying logging in.......... | {current_time} ")
        bot.send_message(message.chat.id, f" mai|l={mail} | password = {password} | classno = {classno} ")
        func.login(message,classno,mail,password)
      except:
        bot.send_message(message.chat.id, f" /help !! after entering /mail mail@yourmail.com /password yourpassword /joinclass numberofclassoftheday do /login  ")



    @bot.message_handler(commands=['help'])
    def command(message):
      bot.send_message(message.chat.id, "  1: /mail yourmail@mail.com 2: /passw yourpassw  3: /joinclass number Finally enter /login ")

    @bot.message_handler(commands=['showchat'])
    def command(message):
      try:
        bot.send_message(message.chat.id, f" ok tring to fetch the chat..........  ")
        func.schat(message)
      except:
        bot.send_message(message.chat.id, f"  follow steps /help or class has not started ")


    @bot.message_handler(commands=['photo'])
    def command(message):
      try:
        func.image(message)
      except:
        bot.send_message(message.chat.id, f" follow steps /help  ")

    def random_command(message):
      request = message.text.split()
      if request[0].lower() not in l:
        bot.send_message(message.chat.id, "not a command  do /help ")
        return True

    @bot.message_handler(func=random_command)
    def check(message):
      pass
if __name__ == "__main__":
    main()
    bot.polling()

