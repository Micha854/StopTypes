#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import telebot
message_rocket = ""
message_lockmodul = ""
class sendMessage():
  counter = 0
  lastMessage = ""
  messageID = 0
  chatID = 0
  sleepTime = 0
  maxCounter = 0
  bot = ""
  def sendMessageFull(self,create):
    message = create.message
    if len(self.lastMessage) == len(message):
      time.sleep(self.sleepTime)
    else:
      if (len(self.lastMessage) <= len(create.message_lockmodul)) or (self.counter >= self.maxCounter):
        try:
          self.bot.delete_message(self.chatID,self.messageID)
          id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
          self.messageID = id.message_id
          self.counter = 0
        except:
          print("Nachricht konnte nicht entfernt werden")
          try:
            id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
            self.messageID = id.message_id
            self.counter = 0
          except:
            print("Nachricht konnte weder entfernt noch neu versendet werden")
        self.lastMessage = message	
        time.sleep(self.sleepTime)
      else:
        try:
          id = self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.messageID, parse_mode='HTML',disable_web_page_preview=True) ##Nachricht traunstein quests
          self.messageID = id.message_id
          self.lastMessage = message
        except:
          try:
            self.bot.delete_message(self.chatId,self.messageID) 
            id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
            self.counter = 0
            self.messageID = id.message_id
            self.lastMessage = message
          except:
            print("Nachricht konnte weder editiert noch entfernt werden, versuche zu senden")
            try:
              id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
              self.counter = 0
              self.messageID= id.message_id
              self.lastMessage = message
            except:
              print("Nachricht konnte weder editiert,entfernt oder gesendet werden")
      self.counter +=1	
      time.sleep(self.sleepTime)

  def sendMessageRocket(self,message):
    if len(self.lastMessage) == len(message):
      time.sleep(self.sleepTime)
    else:
      if self.counter >= self.maxCounter:
        try:
          self.bot.delete_message(self.chatID,self.messageID)
          id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
          self.counter = 0
          self.messageID = id.message_id
          self.lastMessage = message
        except:
          print("Nachricht konnte nicht entfernt werden, versuche zu senden")
          try:
            id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
            self.counter = 0
            self.messageID = id.message_id
            self.lastMessage = message
          except:
            print("Nachricht konnte weder editiert,entfernt oder gesendet werden")
      else:
        try:
          id = self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.messageID, parse_mode='HTML',disable_web_page_preview=True) ##Nachricht traunstein quests
          self.messageID = id.message_id
          self.lastMessage = message
        except:
          try:
            self.bot.delete_message(self.chatId,self.messageID) 
            id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
            self.counter = 0
            self.messageID = id.message_id
            self.lastMessage = message
          except:
            print("Nachricht konnte weder editiert noch entfernt werden, versuche zu senden")
            try:
              id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
              self.counter = 0
              self.messageID= id.message_id
              self.lastMessage = message
            except:
              print("Nachricht konnte weder editiert,entfernt oder gesendet werden")
      self.counter +=1	
      time.sleep(self.sleepTime)

  def sendMessageLockmodul(self,message):

    if len(self.lastMessage) == len(message):
      time.sleep(self.sleepTime)
    elif len(self.lastMessage) >= len(message):
      try:
        id = self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.messageID, parse_mode='HTML',disable_web_page_preview=True) ##Nachricht traunstein quests
        self.messageID = id.message_id
        self.lastMessage = message
      except:
        try:
          self.bot.delete_message(self.chatId,self.messageID) 
          id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
          self.messageID = id.message_id
          self.lastMessage = message
        except:
          print("Nachricht konnte weder editiert noch entfernt werden, versuche zu senden")
          try:
            id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
            self.messageID= id.message_id
            self.lastMessage = message
          except:
            print("Nachricht konnte weder editiert,entfernt oder gesendet werden")
      time.sleep(self.sleepTime)
    else:
      try:
        self.bot.delete_message(self.chatID,self.messageID)
        id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
        self.messageID = id.message_id
      except:
        print("Nachricht konnte nicht entfernt werden")
        try:
          id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
          self.messageID = id.message_id
        except:
          print("Nachricht konnte weder entfernt noch neu versendet werden")
      self.lastMessage = message	
      time.sleep(self.sleepTime)

  def setConfig(self,token,chatID,sleepTime,maxCounter):
    self.chatID = chatID
    self.sleepTime = int(sleepTime)
    self.maxCounter = int(maxCounter)
    self.bot = telebot.TeleBot(token)
