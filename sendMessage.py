import telebot
import time

class sendMessage():
  areaName = ""
  areaNumber = ""
  oldBossMessage = ""
  oldoverviewMessage = ""
  oldLockmodulMessage = ""
  chatID = 0
  singlechatID = 0
  bossid = 0
  overviewid = 0
  lockmodulid = 0
  bot = ""
  messageID = 0
  list_lists_ID = []
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

  def singleStops(self,bolt_line,name,latitude,longitude,typ,lm_types,rb_types):
    if typ in (lm_types):
      try:
        id = self.bot.send_venue(self.singlechatID,latitude,longitude,bolt_line,name,disable_notification=False)
      except:
        print(".................... wait 30 seconds, too many messages")
        sleep = time.sleep(30)
        return sleep
      self.list_lockmodul_output.append(name)
      self.list_lockmodul_message_ID.append(id.message_id)
      outF = open(self.areaName+self.areaNumber+"/lockmodul-output.txt","w")
      outF.writelines(str(self.list_lockmodul_message_ID))
      outF.close()
      return id.message_id
    try:
      id = self.bot.send_venue(self.singlechatID,latitude,longitude,bolt_line,name,disable_notification=True)
    except:
      print(".................... wait 30 seconds, too many messages")
      sleep = time.sleep(30)
      return sleep
    if typ in (rb_types):
      self.list_boss_output.append(name)
      self.list_boss_message_ID.append(id.message_id)
      outF = open(self.areaName+self.areaNumber+"/boss-output.txt","w")
      outF.writelines(str(self.list_boss_message_ID))
      outF.close()
      return id.message_id
    else:
      self.list_output.append(name)
      self.list_message_ID.append(id.message_id)
      outF = open(self.areaName+self.areaNumber+"/output.txt","w")
      outF.writelines(str(self.list_message_ID))
      outF.close()
      return id.message_id

  def sendBoss(self,boss_message,rb):
    #print("bossMSG: " + boss_message)
    #print("oldBoss: " + self.oldBossMessage)
    if self.oldBossMessage == boss_message:
      return self.bossid
    if rb == 0:
      boss_message = "Arlo, Cliff, Sierra und Giovanni gehen um 22 Uhr schlafen\nAb 6 Uhr machen Sie Deine Stadt wieder unsicher"
      self.oldBossMessage = ""
    else:
      self.oldBossMessage = boss_message
    try:
      id = self.bot.edit_message_text(boss_message,chat_id=self.chatID, message_id=self.bossid, parse_mode='HTML',disable_web_page_preview=True)
      self.bossid = id.message_id
      return self.bossid
    except:
      print("Konnte Boss Liste nicht editieren !!! ID: " + str(self.bossid))
    try:
      self.bot.delete_message(self.chatID,self.bossid)
      self.list_lists_ID.remove(self.bossid)
    except:
      print("Boss Liste konnte nicht entfernt werden !!")
    try:
      id = self.bot.send_message(self.chatID,boss_message,parse_mode='HTML',disable_web_page_preview=True,disable_notification=True)
      self.bossid = id.message_id
      self.list_lists_ID.append(self.bossid)
      self.clearOldList(self.areaName, self.areaNumber, self.list_lists_ID)
      return self.bossid
    except:
      print(".................... wait 30 seconds, too many messages")
      sleep = time.sleep(30)
      return sleep

  def sendOverview(self,message,rb,rr,old_rr,lockmodul_message,lm,timer,newMessageAfter):
    print("rupel: " + str(rr))
    print("old R: " + str(old_rr))
#    if lm == 0:
#      message += "\n\nAktuelle Lockmodule:\nEs gibt keine... z\U000000fcnd doch eines"
    if timer == 0 and timer < newMessageAfter and self.chatID != self.singlechatID:
      self.newOverviewSend = 1
    elif timer == 0 or self.oldoverviewMessage == message:
      self.newOverviewSend = 0
      self.sendLockmodul(True,lockmodul_message)
      return message, self.newOverviewSend
        #LINE 1: timer ist nicht 0 && alte liste hat min 1 zeichen && venue messages in separaten channel
          #LINE 2: alte liste ist größer als die neue && rüpel anzahl ist identisch && liste wurde nicht neu gesendet
            #LINE 3: venue messages in separaten channel && alte liste hat min 1 zeichen && alte liste und neue liste sind unterschiedlich && liste wurde nicht neu gesendet
    if  (timer != 0 and len(self.oldoverviewMessage) > 1 and self.chatID != self.singlechatID) or \
          (len(self.oldoverviewMessage) > len(message) and old_rr == rr and self.newOverviewSend == 0) or \
            (self.chatID != self.singlechatID and len(self.oldoverviewMessage) > 1 and len(self.oldoverviewMessage) != len(message) and self.newOverviewSend == 0):
      try:
        self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.overviewid.message_id, parse_mode='HTML',disable_web_page_preview=True)
        self.oldoverviewMessage = message
        self.newOverviewSend = 0
        self.sendLockmodul(True,lockmodul_message)
        return message
      except:
        print("Konnte Rüpel Liste nicht editieren !!! ID: " + str(self.overviewid.message_id))
    try:
      self.bot.delete_message(self.chatID,self.overviewid.message_id)
      self.list_lists_ID.remove(self.overviewid.message_id)
    except:
      print("Rüpel Liste konnte nicht entfernt werden !!")
    if message == "":
      message = "Aktuell keine Rockestops vorhanden"
      self.oldoverviewMessage = ""
    else:
      self.oldoverviewMessage = message
    try:
      self.overviewid = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True)
      self.list_lists_ID.append(self.overviewid.message_id)
      self.clearOldList(self.areaName, self.areaNumber, self.list_lists_ID)
      self.newOverviewSend = 1
      self.sendLockmodul(False,lockmodul_message)
      return self.newOverviewSend
    except:
      print(".................... wait 30 seconds, too many messages")
      sleep = time.sleep(30)
      return sleep    

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
      self.list_lists_ID.remove(self.lockmodulid.message_id)
      self.oldLockmodulMessage = lockmodul_message
    except:
      print("\nLockmodul Liste konnte nicht entfernt werden !!")
    if len(lockmodul_message) > 5:
      try:
        self.lockmodulid = self.bot.send_message(self.chatID, lockmodul_message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=False) 
        self.list_lists_ID.append(self.lockmodulid.message_id)
        self.clearOldList(self.areaName, self.areaNumber, self.list_lists_ID)
        self.oldLockmodulMessage = lockmodul_message
      except:
        print(".................... wait 30 seconds, too many messages")
        sleep = time.sleep(30)
        return sleep

  
  def clearOldList (self, areaName, areaNumber, list_lists_ID):
    filename_list_lists_ID = self.areaName+self.areaNumber+"/lists.txt"
    outF = open(filename_list_lists_ID,"w")
    outF.writelines(str(self.list_lists_ID))
    outF.close()

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
    outF = open(self.areaName+self.areaNumber+"/output.txt","w")
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
    outF = open(self.areaName+self.areaNumber+"/boss-output.txt","w")
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
    outF = open(self.areaName+self.areaNumber+"/lockmodul-output.txt","w")
    outF.writelines(str(self.list_lockmodul_message_ID))
    outF.close()