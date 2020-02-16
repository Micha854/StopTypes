import telebot

class Clear():
  def clear(self,token,singlechatID,cfg):
    bot = telebot.TeleBot(token)
    try:
      f = open(cfg.areaName+"output.txt", "r")
    except:
      return
    oldMessages = f.read()
    f.close()
    oldMessages = oldMessages[1:len(oldMessages)-1]
    oldMessages = oldMessages.split(', ') 
    for messageID in oldMessages:
      try:
        bot.delete_message(singlechatID,message_id=messageID)
      except:
        print("1Nachricht konnte nicht entfernt werden")
    try:
      f = open(cfg.areaName+"boss-output.txt", "r")
    except:
      return
    oldMessages = f.read()
    f.close()
    oldMessages = oldMessages[1:len(oldMessages)-1]
    oldMessages = oldMessages.split(', ') 
    for messageID in oldMessages:
      try:
        bot.delete_message(singlechatID,message_id=messageID)
      except:
        print("2Nachricht konnte nicht entfernt werden")
    try:
      f = open(cfg.areaName+"lockmodul-output.txt", "r")
    except:
      return
    oldMessages = f.read()
    f.close()
    oldMessages = oldMessages[1:len(oldMessages)-1]
    oldMessages = oldMessages.split(', ') 
    for messageID in oldMessages:
      try:
        bot.delete_message(singlechatID,message_id=messageID)
      except:
        print("3Nachricht konnte nicht entfernt werden")
