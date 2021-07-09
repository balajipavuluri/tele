from flask import Flask, request
import telebot
import os
import logging
import sys
import re
from datetime import datetime
"""
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1200,800")
chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 2,
     "profile.default_content_setting_values.notifications": 2
  })
"""
import func

def main():
    S=set() 
    global bot
    """
    global driver
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    """
    token = os.environ.get("TOKEN")
    bot = telebot.TeleBot(token)

    now=datetime.now()
    

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info('Starting Bot...')



    
    app = Flask(__name__)


    l= ['/help','/login','/joinclass','/start','/mail','/password','/showchat','/photo','/logout']

    @app.route('/', methods=["POST"])
    def webhook():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200

    @bot.message_handler(commands=['start'])
    def command(message):
        mail=password=classno=0
        bot.send_message(message.chat.id, 'Hi, ' + message.chat.first_name + '!')
        #login(message)



    @bot.message_handler(commands=['mail'])
    def command(message):
      try:
        global mail
        mail=message.text.split()[1]
        print(mail, S)
        chkmail=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(chkmail,mail):
            print("valid mail")
            bot.send_message(message.chat.id, f" ok got your mail => {mail} now send your password like  /password yourpasswordhere ")
            S.add('x')
        else:
            bot.send_message(message.chat.id, f" not a  mail format : /mail yourmail@mail.com  /help !")

      except:
        bot.send_message(message.chat.id, f"format : /mail yourmail@mail.com ")


    @bot.message_handler(commands=['password'])
    def command(message):
      try:
        print(78)
        global password
        print(79)
        password=str(message.text.split()[1])
        print(81)
        print(mail , password, S)
        print(83)
        bot.send_message(message.chat.id, f" ok got your password: {password} now   /joinclass number   ")
        S.add('y')
        
      except:
        bot.send_message(message.chat.id, f"format : /password yourpass |  ")


    @bot.message_handler(commands=['joinclass'])
    def command(message):
      try:
        print(93)
        global classno
        print(94)
        classno=int(message.text.split()[1])
        print(96)
        print(mail,password,classno, S)
        print(99)
        bot.send_message(message.chat.id, f" ok got your class number: {classno}  now enter /login ")
        S.add('z')
      except:
        bot.send_message(message.chat.id, f"format : /joinclass classno |  ")


    @bot.message_handler(commands=['login'])
    def command(message):
        try:
               print(f" length {S} {len(S)}") 
               if len(S)>=3 :
                  print(104)
                  current_time=now.strftime("%H:%M:%S")
                  print(105)
                  bot.send_message(message.chat.id, f" ok wait im trying logging in.......... | {current_time} ")
               
                  print(f" {mail} {password} {classno}")
                  bot.send_message(message.chat.id, f" mail = {mail} | password = {password} | classno = {classno} ")
                  print("ok logging in")
                  func.login(message,classno,mail,password)
                  S.pop()
                  print("i doubt it got login")
                  #mail = password = " " 
               else:
                  bot.send_message(message.chat.id," do /help ") 
                  print(f" may be {mail} {password} {classno} not sent  {len(S)} ") 
               
               """
               print("del all")
               print("i doubt it got login")
               print("del all1")
               del mail
               print("del all2")
               del password
               print("del all3")
               del classno
               print("del all4")
               
               
               print("del mail start ")
               del mail
               print('deleted mail') 
               """
               
        except:
               bot.send_message(message.chat.id, f" /help !! after entering /mail mail@yourmail.com /password yourpassword /joinclass numberofclassoftheday do /login  ")
            
    @bot.message_handler(commands=['logout'])
    def command(message):
        try:
            print(f"{mail} {password} {classno}")
            #mail=password=classno=0
            #print(f"{mail} {password} {classno}")
            bot.send_message(message.chat.id, f"cleared all   ")
            func.log(message)
            print("ok trying")
        
        except:
           bot.send_message(message.chat.id, f" before logout do login /help  ")
        #mail=password=classno=0
     

    @bot.message_handler(commands=['help'])
    def command(message):
      bot.send_message(message.chat.id, "  1: /mail yourmail@mail.com 2: /passw yourpassw  3: /joinclass number Finally enter /login ")

    @bot.message_handler(commands=['showchat'])
    def command(message):
      try:
        bot.send_message(message.chat.id, f" ok tring to fetch the chat..........  ")
        func.schat(message)
      except:
        current_time=now.strftime("%H:%M:%S")
        bot.send_message(message.chat.id, f"  follow steps /help or class has not started {current_time} ")


    @bot.message_handler(commands=['photo'])
    def command(message):
      try:
        func.image(message)
      except:
        bot.send_message(message.chat.id, f" follow steps /help  ")

    def random_command(message):
      try:
        request = message.text.split()
        if request[0].lower() not in l:
          bot.send_message(message.chat.id, "not a command  do /help ")
          return True
      except:
        bot.send_message(message.chat.id, f" follow steps /help  ")

    @bot.message_handler(func=random_command)
    def check(message):
      pass
if __name__ == "__main__":
    #mail=password=classno=0
    
    main()
    bot.polling()

