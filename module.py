#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sql
import createMessage
import sendMessage

class Module():
  def full(self,cfg):
    send = sendMessage.sendMessage()
    send.setConfig(cfg.token,cfg.chatId,cfg.sleepTime,cfg.newMessageAfter)
    while 1 == 1:
      Sql = sql.Sql()
      create = createMessage.createMessage()
      Sql.startSQL(cfg,"rocket","incident_expiration") 
      create.create(Sql,"rocket",cfg.hours)
      Sql.startSQL(cfg,"lockmodul","lure_expiration")
      create.create(Sql,"lockmodul",cfg.hours)
      send.sendMessageFull(create)

  def rocketStopsOnly(self,cfg):
    send = sendMessage.sendMessage()
    send.setConfig(cfg.token,cfg.chatId,cfg.sleepTime,cfg.newMessageAfter)
    while 1 == 1:
      Sql = sql.Sql()
      create = createMessage.createMessage()
      Sql.startSQL(cfg,"rocket","incident_expiration")
      create.create(Sql,"rocket",cfg.hours)
      send.sendMessageRocket(create.message)
    
  def LockModulOnly(self,cfg):
    send = sendMessage.sendMessage()
    send.setConfig(cfg.token,cfg.chatId,cfg.sleepTime,cfg.newMessageAfter)
    while 1 == 1:
      Sql = sql.Sql()
      create = createMessage.createMessage()
      Sql.startSQL(cfg,"lockmodul","lure_expiration")
      create.create(Sql,"lockmodul",cfg.hours)
      send.sendMessageLockmodul(create.message)