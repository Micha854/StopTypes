import telebot

class Clear():
  def clear(self,token,chatID,filename):
    bot = telebot.TeleBot(token)
    oldMessages =""
    try:
      f = open(filename+"output.txt", "r")
      oldMessages = f.read()
      f.close()
      oldMessages = oldMessages[1:len(oldMessages)-1]
      oldMessages = oldMessages.split(', ') 
      for messageID in oldMessages:
        print("Nachrichten ID: "+messageID)
        try:
          bot.delete_message(chatID,message_id=messageID)
        except:
          print("Nachricht konnte nicht entfernt werden")
    except:
      print("File nicht gefunden")
    
    try:
      f = open(filename+"boss-output.txt", "r")
      oldMessages = f.read()
      f.close()
      oldMessages = oldMessages[1:len(oldMessages)-1]
      oldMessages = oldMessages.split(', ') 
      for messageID in oldMessages:
        try:
          bot.delete_message(chatID,message_id=messageID)
        except:
          print("Nachricht konnte nicht entfernt werden")
    except:
      print("File nicht gefunden")