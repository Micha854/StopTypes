#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser

class Config():
  host = ""
  database = ""
  user = ""
  password = ""
  min_latitude = ""
  max_latitude = ""
  min_longitude = ""
  max_longitude = ""
  token = ""
  chatId = ""
  verlinkung = ""

  def readConfig(self,cfgFile):  
    parser = ConfigParser()
    parser.read(cfgFile, encoding='utf-8')

    self.host = parser.get('Mysql', 'host')
    self.database = parser.get('Mysql', 'database')
    self.user = parser.get('Mysql', 'user')
    self.password = parser.get('Mysql', 'password')

    self.token = parser.get('Bot Settings', 'token')
    self.chatId = parser.get('Bot Settings', 'chat_id')
    self.verlinkung = parser.get('Bot Settings', 'verlinkung')

    self.min_latitude = parser.get('Statements', 'min_latitude')
    self.max_latitude = parser.get('Statements', 'max_latitude')
    self.min_longitude = parser.get('Statements', 'min_longitude')
    self.max_longitude = parser.get('Statements', 'max_longitude')