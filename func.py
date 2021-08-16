import clipboard as cb
from time import sleep  
from datetime import datetime    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os   
from PIL import Image       
import sys
import asyncio



from flask import Flask, request
import telebot
import os
now=datetime.now()


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--window-size=1200,800")
chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 2,
     "profile.default_content_setting_values.notifications": 2
  })







token = os.environ.get("TOKEN")
bot = telebot.TeleBot(token)


poll='/html/body/div/main/div[2]/div/div[2]/div[1]/button'

login=0


def login(message,classno,mail,password):
   flag_login=0 
   global driver
   driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
   driver.maximize_window()  
   #path='E:/selenium/chromedriver.exe'
   #driver = webdriver.Chrome(executable_path=path,options=chrome_options)
   link=os.environ.get("LINK")
   driver.get(link)    
   sleep(2)        
   l=driver.find_element_by_link_text("Log in")    
   l.click()   
   sleep(2)    
   try:
      m_btn= driver.find_element_by_name('loginId')   
      m_btn.clear()   
      m_btn.send_keys(mail)   
      sleep(2)   
      p_btn=driver.find_element_by_name('password')   
      p_btn.clear()   
      p_btn.send_keys(password)  
      sleep(2)   
      sub=driver.find_element_by_xpath('//button[text()="Submit"]')   
      sub.click() 
      sleep(2)
      meet_path='/html/body/div[9]/div/div[1]/div/div/div[1]/div/div[2]/a'
      flag_login=1    
      meet = driver.find_element_by_xpath(meet_path)  
      meet.click()    
      image(message)
      bot.send_message(message.chat.id, f" login success please wait joining class  ")
      # mail=password=" " 
      bot.send_message(message.chat.id, f" after completion of class try /logout :( else :) ")
      x=1 #login success goto next step
      login=1
      flag_login=1
      if x:
         y=str(classno) 
         x=y   
         y='//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[{0}]/div'.format(x)
         
         try:
            sleep(1)
            cl= driver.find_element_by_xpath(y)  
            cl.click()
            class_link_available=1
         except:
           image(message)
           current_time=now.strftime("%H:%M:%S")
           bot.send_message(message.chat.id, f"  class :(( not available time {current_time} ")
         if class_link_available:
            try:
               j=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/a')    
               j.click()   
               sleep(3)
               class_joined=1
            except:
               bot.send_message(message.chat.id, f"  class cannot be joined   ")
               current_time=now.strftime("%H:%M:%S")
               bot.send_message(message.chat.id, f"  may be not started or completed time {current_time}  ")
               image(message)
            
         if class_joined:
            try: #always possible true
               iframe = driver.find_element_by_xpath("//iframe[@id='frame']")  
               driver.switch_to.frame(iframe)  
               sleep(5)
               listen = driver.find_elements_by_tag_name("button") 
               for item in listen: 
                  attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)    
                  if 'aria-label' in attrs:   
                      if attrs['aria-label'] == 'Listen only':   
                          sleep(3) 
                          item.click()     
                          #sleep(3600)
                          #break 
                          image(message)
                          bot.send_message(message.chat.id, f"sound on..........  ")
                          
                          chat=1
            except:
               current_time=now.strftime("%H:%M:%S")
               bot.send_message(message.chat.id, f"problem in sound on lite.......... time {current_time} ")
               image(message)
            
         if chat:
            schat(message)
            
   except:
      if flag_login==0:
         current_time=now.strftime("%H:%M:%S")
         bot.send_message(message.chat.id, f"  login error !.......... do /help time {current_time}  ")
         image(message)


def schat(message):
   try:
      print("ok get chat1")
      cliq='/html/body/div/main/section/div/header/div/div[1]/div[1]/button'
      print("ok get chat2")
      x=driver.find_element_by_xpath(cliq)
      print("ok get chat3")
      sleep(1)
      print("ok get chat4")
      x.click()
      print("ok get chat5")
      public_chat='/html/body/div/main/section/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div'
      x=driver.find_element_by_xpath(public_chat)
      print("ok get chat6")
      sleep(1)
      x.click()
      print("ok get chat7")
      z='/html/body/div/main/section/div[5]/section/div/header/div[2]'
      text=driver.find_element_by_xpath(z)
      sleep(1)
      text.click()
      print("ok get chat8")
      copy = '/html/body/div/main/section/div[5]/section/div/header/div[2]/div/div/ul/li[2]/span[1]'

      copy = driver.find_element_by_xpath(copy)
      print("ok get chat9")
      sleep(3)
      print(91)
      copy.click()
      print(92)
      sleep(3)
      chat=cb.paste()
      print(93)
      print(f"printing chat {chat}")
      print(94)
      print("ok get chat10")
      bot.send_message(message.chat.id, f"{chat}")
      print(101)
      del chat
      print("ok get chat11")
      cliq='/html/body/div/main/section/div/header/div/div[1]/div[1]/button'
      x=driver.find_element_by_xpath(cliq)
      sleep(3)
      x.click()
      print("ok get chat12")
   except:
      image(message)
      current_time=now.strftime("%H:%M:%S")
      bot.send_message(message.chat.id, f"chat not available  try /help time {current_time}")
      print("chat option not available")
      print("success fail")

def image(message):
   try:
      sleep(2)
      #bot.send_chat_action(message.chat.id=userId, action=ChatAction.UPLOAD_PHOTO)
      driver.save_screenshot("ss.png")
      X = bot.send_photo(message.chat.id, open('ss.png','rb'))
      os.remove('ss.png')
      
   except:
       current_time=now.strftime("%H:%M:%S")
       bot.send_message(message.chat.id, f"make sure login to class or try /help time {current_time} ")
 

def s(message,rno):
   try:
     driver.get("https://rvrjcce.ac.in/examcell/results/regnoresultsR.php?")
     l=driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr/td[3]/input")
     l.click()
     l.send_keys(rno)
     image(message)
   except:
     bot.send_message(message.chat.id, f"format")

      
   










def log(message):
   try:
      print("logging out")
      sleep(2)
      #bot.send_chat_action(message.chat.id=userId, action=ChatAction.UPLOAD_PHOTO)
      current_time=now.strftime("%H:%M:%S")
      bot.send_message(message.chat.id, f" logging out {current_time} ")
      link=os.environ.get("LINK")
      driver.get(link)   
      image(message)
      driver.quit()
      print("success logout")
      #image(message)
      print('images sent')

        

   except:
      current_time=now.strftime("%H:%M:%S")
      bot.send_message(message.chat.id, f"make sure login to class or try /help time {current_time} ")
      print("success logout failed")


