import telebot
import time

class sendMessage():
  filename = ""
  oldBossMessage = ""
  oldBossMessage2 = ""
  oldoverviewMessage = ""
  oldoverviewMessage2= ""
  chatID = 0
  bossid = 0
  overviewid = 0
  overviewid2= 0
  bot = ""
  messageID = 0
  list_output = []
  list_message_ID = []
  list_boss_output = []
  list_boss_message_ID = []

  def setConfig(self,token,chatID,filename):
    self.chatID = chatID
    self.bot = telebot.TeleBot(token)
    self.filename = filename


  def singleStops(self,bolt_line,name,latitude,longitude,typ):
    id = self.bot.send_venue(self.chatID,latitude,longitude,bolt_line,name,disable_notification=True)
    if typ > 40 and typ < 45:
      self.list_boss_output.append(name)
      self.list_boss_message_ID.append(id.message_id)
      outF = open(self.filename +"boss-output.txt","w")
      outF.writelines(str(self.list_boss_message_ID))
      outF.close()
      return id.message_id
    self.list_output.append(name)
    self.list_message_ID.append(id.message_id)
    outF = open(self.filename +"output.txt","w")
    outF.writelines(str(self.list_message_ID))
    outF.close()
    return id.message_id
    

  def sendBoss(self,message,message2):
    if self.oldBossMessage == message and self.oldBossMessage2 == message2:
      return self.bossid
    if len(message) > 5:
      try:
        id = self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.bossid, parse_mode='HTML',disable_web_page_preview=True) ##Nachricht traunstein quests
        self.oldBossMessage = message
        if len(message2) > 5:
          id = self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.bossid-1, parse_mode='HTML',disable_web_page_preview=True) ##Nachricht traunstein quests
          self.oldBossMessage2 = message2
        self.bossid = id.message_id
        return self.bossid
      except:
        print("ID nicht gefunden")
    try:
      self.bot.delete_message(self.chatID,self.bossid)
      if len(message2) > 5:
        self.bot.delete_message(self.chatID,self.bossid-1)
    except:
      print("Nichts zu entfernen")
    if message == "":
      message = "Aktuell keine Bosse vorhanden"
      self.oldBossMessage = ""
      id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True)
      self.bossid = id.message_id 
      return self.bossid
    id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True)
    if(message2):
      id = self.bot.send_message(self.chatID, message2, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True)
      self.oldBossMessage2 = message2
    self.oldBossMessage = message
    self.bossid = id.message_id
    return self.bossid


  def sendOverview(self,message,message2):
    if self.oldoverviewMessage == message and self.oldoverviewMessage2 == message2:
      return
    try:  
      self.bot.delete_message(self.chatID,self.overviewid)
      self.bot.delete_message(self.chatID,self.overviewid-1)
    except:
      print("Nichts zu entfernen")
    id = self.bot.send_message(self.chatID, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True)
    if(message2):
      id = self.bot.send_message(self.chatID, message2, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True)
      self.overviewid2 = id.message_id
      self.oldoverviewMessage2 = message2
    
    self.overviewid = id.message_id
    self.oldoverviewMessage = message


  def clearOutputList(self,encounter):
    i = 0
    print("Checke Outputliste\n")
    for name in self.list_output:
      if not encounter.__contains__(name):
        try:
          print("Entferne Nachricht")
          self.bot.delete_message(self.chatID,self.list_message_ID[i])
          self.list_message_ID.__delitem__(i)
          self.list_output.__delitem__(i)
        except:
          print("Nachricht konnte nicht entfernt werden")
      i +=1
    outF = open(self.filename +"output.txt","w")
    outF.writelines(str(self.list_message_ID))
    outF.close()
    i = 0
    for name in self.list_boss_output:
      if not encounter.__contains__(name):
        try:
          print("Entferne Nachricht")
          self.bot.delete_message(self.chatID,self.list_boss_message_ID[i])
          self.list_boss_message_ID.__delitem__(i)
          self.list_boss_output.__delitem__(i)
        except:
          print("Nachricht konnte nicht entfernt werden")
      i +=1
    outF = open("boss-output.txt","w")
    outF.writelines(str(self.list_boss_message_ID))
    outF.close()
