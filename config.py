#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser

class Config():
  host = ""
  database = ""
  user = ""
  password = ""
  fence = ""
  token = ""
  singlechatId = ""
  singlechatUrl = ""
  chatId = ""
  chatUrl = ""
  areaName = ""

  def readConfig(self,cfgFile):  
    parser = ConfigParser()
    parser.read(cfgFile, encoding='utf-8')

    self.host = parser.get('Mysql', 'host')
    self.database = parser.get('Mysql', 'database')
    self.user = parser.get('Mysql', 'user')
    self.password = parser.get('Mysql', 'password')

    self.token = parser.get('Bot Settings', 'token')
    self.singlechatId = parser.get('Bot Settings', 'singlechat_id')
    self.singlechatUrl = parser.get('Bot Settings', 'singlechat_url')
    self.chatId = parser.get('Bot Settings', 'chat_id')
    self.chatUrl = parser.get('Bot Settings', 'chat_url')

    self.areaName = parser.get('Geofence', 'areaName')
    self.fence = parser.get('Geofence', 'fence')
