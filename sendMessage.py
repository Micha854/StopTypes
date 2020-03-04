import telebot
import time

class sendMessage():
  areaName = ""
  areaNumber = ""
  oldBossMessage = ""
  oldoverviewMessage = ""
  oldLockmodulMessage = ""
  oldMessage = ""
  chatID = 0
  singlechatID = 0
  bossid = 0
  overviewid = 0
  lockmodulid = 0
  bot = ""
  messageID = 0
  list_output = []
  list_message_ID = []
  list_boss_output = []
  list_boss_message_ID = []
  list_lockmodul_output = []
  list_lockmodul_message_ID = []

  
  try:
    newOverviewSend = newOverviewSend
  except:
    newOverviewSend = 0
  
  def setConfig(self,token,singlechatID,chatID,areaName,areaNumber):
    self.areaName = areaName
    self.areaNumber = areaNumber
    self.singlechatID = singlechatID
    self.chatID = chatID
    self.bot = telebot.TeleBot(token)

  def singleStops(self,bolt_line,name,latitude,longitude,typ):
    if typ > 500 and typ < 505:
      try:
        id = self.bot.send_venue(self.singlechatID,latitude,longitude,bolt_line,name,disable_notification=False)
      except (ConnectionAbortedError, ConnectionResetError, ConnectionRefusedError, ConnectionError):
        print ("Fehler beim senden von SingleStop ohne Ping")
        time.sleep(5)
        id = self.bot.send_venue(self.singlechatID,latitude,longitude,bolt_line,name,disable_notification=False)
      self.list_lockmodul_output.append(name)
      self.list_lockmodul_message_ID.append(id.message_id)
      outF = open(self.areaName+self.areaNumber+"lockmodul-output.txt","w")
      outF.writelines(str(self.list_lockmodul_message_ID))
      outF.close()
      return id.message_id
    try:
        id = self.bot.send_venue(self.singlechatID,latitude,longitude,bolt_line,name,disable_notification=True)
    except (ConnectionAbortedError, ConnectionResetError, ConnectionRefusedError, ConnectionError):
        print ("Fehler beim senden von SingleStop mit Ping")
        time.sleep(5)
        id = self.bot.send_venue(self.singlechatID,latitude,longitude,bolt_line,name,disable_notification=True)
    if typ > 40 and typ < 45:
      self.list_boss_output.append(name)
      self.list_boss_message_ID.append(id.message_id)
      outF = open(self.areaName+self.areaNumber+"boss-output.txt","w")
      outF.writelines(str(self.list_boss_message_ID))
      outF.close()
      return id.message_id
    self.list_output.append(name)
    self.list_message_ID.append(id.message_id)
    outF = open(self.areaName+self.areaNumber+"output.txt","w")
    outF.writelines(str(self.list_message_ID))
    outF.close()
    return id.message_id

  def sendBoss(self,message):
    if self.oldBossMessage == message:
      return self.bossid
    if len(message) > 5:
      try:
        id = self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.bossid, parse_mode='HTML',disable_web_page_preview=True)
        self.oldBossMessage = message
        self.bossid = id.message_id
        return self.bossid
      except:
        print("Boss Single-Message nicht gefunden")
    try:
      self.bot.delete_message(self.singlechatID,self.bossid)
    except:
      print("Boss Single-Message konnte nicht entfernt werden !!")
    if message == "":
      message = "Arlo, Cliff, Sierra und Giovanni gehen um 22 Uhr schlafen\nAb 6 Uhr machen Sie Deine Stadt wieder unsicher"
      self.oldBossMessage = ""
      id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True)
      self.bossid = id.message_id 
      return self.bossid
    id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) 
    self.oldBossMessage = message
    self.bossid = id.message_id
    return self.bossid

  def sendOverview(self,message,newk,j,k,lockmodul_message):
    print("rupel: " + str(newk-j))
    print("old R: " + str(k))
    if self.oldoverviewMessage == message:
      self.newOverviewSend = 0
      self.sendLockmodul(True,lockmodul_message)
      return message, self.newOverviewSend
    if len(self.oldoverviewMessage) > len(message) and newk-j == k and self.newOverviewSend == 0 or self.chatID != self.singlechatID and len(self.oldoverviewMessage) > 1 and len(self.oldoverviewMessage) != len(message) and self.newOverviewSend == 0:
      try:
        self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.overviewid.message_id, parse_mode='HTML',disable_web_page_preview=True)
        self.oldoverviewMessage = message
        self.newOverviewSend = 0
        return message
      except:
        print("Konnte Rüpel Liste nicht editieren !!! ID: " + str(self.overviewid.message_id))
    try:
      self.bot.delete_message(self.chatID,self.overviewid.message_id)
    except:
      print("Rüpel Liste konnte nicht entfernt werden !!")
    if message == "":
      message = "Aktuell keine Rockestops vorhanden"
      self.oldoverviewMessage = ""
      self.overviewid = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) 
      self.newOverviewSend = 1
      return self.newOverviewSend
    self.overviewid = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) 
    self.oldoverviewMessage = message
    self.newOverviewSend = 1
    self.sendLockmodul(False,lockmodul_message)
    return self.newOverviewSend

  def sendLockmodul(self,bool,lockmodul_message):
    if self.oldLockmodulMessage == lockmodul_message and bool:
      return
    if len(self.oldLockmodulMessage) > len(lockmodul_message) and len(lockmodul_message) > 5 and self.chatID != self.singlechatID and self.newOverviewSend == 0:
      try:
        self.bot.edit_message_text(lockmodul_message,chat_id=self.chatID, message_id=self.lockmodulid.message_id, parse_mode='HTML',disable_web_page_preview=True)
        self.oldLockmodulMessage = lockmodul_message
        return lockmodul_message
      except:
        print("Konnte Lockmodul Liste nicht edetieren !!! ID: " + str(self.lockmodulid.message_id))
    try:
      self.bot.delete_message(self.chatID,self.lockmodulid.message_id)
      self.oldLockmodulMessage = lockmodul_message
    except:
      print("\nLockmodul Liste konnte nicht entfernt werden !!")
    if len(lockmodul_message) > 5:
      self.lockmodulid = self.bot.send_message(self.chatID, lockmodul_message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=False) 
      self.oldLockmodulMessage = lockmodul_message

  def clearOutputList(self,encounter,lockmodul):
    i = 0
    print("Checke Outputliste\n")
    for name in self.list_output:
      if not encounter.__contains__(name):
        try:
          print("Entferne Rupel Nachricht")
          self.bot.delete_message(self.singlechatID,self.list_message_ID[i])
          self.list_message_ID.__delitem__(i)
          self.list_output.__delitem__(i)
        except:
          print("Rupel Nachricht konnte nicht entfernt werden")
      i +=1
    outF = open(self.areaName+self.areaNumber+"output.txt","w")
    outF.writelines(str(self.list_message_ID))
    outF.close()
    i = 0
    for name in self.list_boss_output:
      if not encounter.__contains__(name):
        try:
          print("Entferne BOSS Nachricht")
          self.bot.delete_message(self.singlechatID,self.list_boss_message_ID[i])
          self.list_boss_message_ID.__delitem__(i)
          self.list_boss_output.__delitem__(i)
        except:
          print("BOSS Nachricht konnte nicht entfernt werden")
      i +=1
    outF = open(self.areaName+self.areaNumber+"boss-output.txt","w")
    outF.writelines(str(self.list_boss_message_ID))
    outF.close()
    i = 0
    for name in self.list_lockmodul_output:
      if not lockmodul.__contains__(name):
        try:
          print("Entferne Lockmodul Nachricht")
          self.bot.delete_message(self.singlechatID,self.list_lockmodul_message_ID[i])
          self.list_lockmodul_message_ID.__delitem__(i)
          self.list_lockmodul_output.__delitem__(i)
        except:
          print("Lockmodul Nachricht konnte nicht entfernt werden")
      i +=1
    outF = open(self.areaName+self.areaNumber+"lockmodul-output.txt","w")
    outF.writelines(str(self.list_lockmodul_message_ID))
    outF.close()

