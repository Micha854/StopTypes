import telebot
import time

class sendMessage():
  areaName = ""
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

  def send(self,message):
    if len(self.oldMessage) != len(message):
      try:
        id = self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.messageID, parse_mode='HTML',disable_web_page_preview=True) ##Nachricht traunstein quests
        self.messageID = id.message_id
        self.lastMessage = message
      except:
        print("ging ned")
      id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
      self.counter = 0
      self.messageID= id.message_id
      self.lastMessage = message
      time.sleep(3600)

  def setConfig(self,token,singlechatID,chatID,areaName):
    self.areaName = areaName
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
      outF = open(self.areaName+"lockmodul-output.txt","w")
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
      outF = open(self.areaName+"boss-output.txt","w")
      outF.writelines(str(self.list_boss_message_ID))
      outF.close()
      return id.message_id
    self.list_output.append(name)
    self.list_message_ID.append(id.message_id)
    outF = open(self.areaName+"output.txt","w")
    outF.writelines(str(self.list_message_ID))
    outF.close()
    return id.message_id

  def sendBoss(self,message):
    if self.oldBossMessage == message:
      return self.bossid
    if len(message) > 5:
      try:
        id = self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.bossid, parse_mode='HTML',disable_web_page_preview=True) ##Nachricht traunstein quests
        self.oldBossMessage = message
        self.bossid = id.message_id
#test zum entfernen der message
#        message = ""
        return self.bossid
      except:
        print("ID nicht gefunden")
    try:
      self.bot.delete_message(self.singlechatID,self.bossid)
    except:
      print("1Nichts zu entfernen")
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

  def sendOverview(self,message,lockmodul_message):
    if self.oldoverviewMessage == message:
      self.sendLockmodul(True,lockmodul_message)
      return
    try:
      self.bot.delete_message(self.chatID,self.overviewid.message_id)
    except:
      print("2Nichts zu entfernen")
    if message == "":
      message = "Aktuell keine Rockestops vorhanden"
      self.oldoverviewMessage = ""
      self.overviewid = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) 
      return
    self.overviewid = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) 
    self.oldoverviewMessage = message
    self.sendLockmodul(False,lockmodul_message)

  def sendLockmodul(self,bool,lockmodul_message):
    if self.oldLockmodulMessage == lockmodul_message and bool:
      return
    try:
      self.bot.delete_message(self.chatID,self.lockmodulid.message_id)
    except:
      print("3Nichts zu entfernen")
    if len(lockmodul_message) > 5:
      #lockmodul_message = "Aktuell keine Lockmodule vorhanden"
      self.lockmodulid = self.bot.send_message(self.chatID, lockmodul_message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) 
      self.oldLockmodulMessage = lockmodul_message

  def clearOutputList(self,encounter,lockmodul):
    i = 0
    print("Checke Outputliste\n")
    for name in self.list_output:
      if not encounter.__contains__(name):
        try:
          print("1Entferne Nachricht")
          self.bot.delete_message(self.singlechatID,self.list_message_ID[i])
          self.list_message_ID.__delitem__(i)
          self.list_output.__delitem__(i)
        except:
          print("1Nachricht konnte nicht entfernt werden")
      i +=1
    outF = open(self.areaName+"output.txt","w")
    outF.writelines(str(self.list_message_ID))
    outF.close()
    i = 0
    for name in self.list_boss_output:
      if not encounter.__contains__(name):
        try:
          print("2Entferne Nachricht")
          self.bot.delete_message(self.singlechatID,self.list_boss_message_ID[i])
          self.list_boss_message_ID.__delitem__(i)
          self.list_boss_output.__delitem__(i)
        except:
          print("2Nachricht konnte nicht entfernt werden")
      i +=1
    outF = open(self.areaName+"boss-output.txt","w")
    outF.writelines(str(self.list_boss_message_ID))
    outF.close()
    i = 0
    for name in self.list_lockmodul_output:
      if not lockmodul.__contains__(name):
        try:
          print("3Entferne Nachricht")
          self.bot.delete_message(self.singlechatID,self.list_lockmodul_message_ID[i])
          self.list_lockmodul_message_ID.__delitem__(i)
          self.list_lockmodul_output.__delitem__(i)
        except:
          print("3Nachricht konnte nicht entfernt werden")
      i +=1
    outF = open(self.areaName+"lockmodul-output.txt","w")
    outF.writelines(str(self.list_lockmodul_message_ID))
    outF.close()

