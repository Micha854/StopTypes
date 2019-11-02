#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser

####Hier wird die Config aus dem Configfile geladen und den einzelen
####Werten zugewiesen

class Config():
  host = ""
  database = ""
  user = ""
  password = ""
  sleepTime = ""
  newMessageAfter = ""
  rocketStops = ""
  lureModule = ""
  hours = ""
  min_latitude = ""
  max_latitude = ""
  min_longitude = ""
  max_longitude = ""
  token = ""
  chatId = ""

  def readConfig(self):  
    parser = ConfigParser()
    parser.read('config.ini', encoding='utf-8')

    self.host = parser.get('Mysql', 'host')
    self.database = parser.get('Mysql', 'database')
    self.user = parser.get('Mysql', 'user')
    self.password = parser.get('Mysql', 'password')

    self.sleepTime = parser.get('Message', 'sleep_time')
    self.newMessageAfter = parser.get('Message', 'newMessageAfter')

    self.rocketStops = parser.get('Options', 'rocketStops')
    self.lureModule = parser.get('Options', 'lureModule')
    self.hours = parser.get('Options', 'defineHours')
    
    self.min_latitude = parser.get('Statements', 'min_latitude')
    self.max_latitude = parser.get('Statements', 'max_latitude')
    self.min_longitude = parser.get('Statements', 'min_longitude')
    self.max_longitude = parser.get('Statements', 'max_longitude')

    self.token = parser.get('Bot Settings', 'token')
    self.chatId = parser.get('Bot Settings', 'chat_id')