import helper
import stopType
import datetime


class createMessage():
  message = ""
  def create(self,send,sql,cfg):
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0 # summe gesamt
    j = 0 # bosse
    k = 0 # rocket stops
    message = ""
    boss_message = send.oldBossMessage
#    boss_message = ""
    lockmodul_message = ""
    changed = True
    Emoji = ""
    Infotext = ""
    print(cfg.areaName)
    print("Anzahl Namen: "+str(len(sql.name)))
    
    #now time
    now = datetime.datetime.now()
    print(now.strftime("%m/%d/%Y, %H:%M:%S"))

    for name in sql.name:
      if send.list_output.__contains__(name):
        f = open(cfg.areaName+"output.txt", "r")
            # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        typ = stop.getType(sql.incident_grunt_type[i])
        print("Wert k1: "+ str(k))
        id = list_string[send.list_output.index(name)]
        print("Wert k2: "+ id)
#erste message???
        message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(name) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        k +=1
        i +=1
        print("all: " + str(list_string))
      elif send.list_boss_output.__contains__(name):
        j +=1
        i +=1
      else:
        stopName = sql.name[i]
        latitude = sql.latitude[i]
        longitude = sql.longitude[i]
        typ = stop.getType(sql.incident_grunt_type[i])
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        print(stopName)

# Format Einzelne Nachricht
        bolt_line = str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " " + stop.Emoji + stop.Infotext
        
        id = send.singleStops(bolt_line,stopName,latitude,longitude,sql.incident_grunt_type[i])
        if sql.incident_grunt_type[i] > 40 and sql.incident_grunt_type[i] < 45:
          boss_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(name) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
#          k +=1
#vorher          k +=1 nun j
          j +=1
        else:
          message += stop.Emoji + "MAIN MESSAGE <a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(name) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
          k +=1
        i +=1
    listLM = stop.Sstandard + stop.Sgletscher + stop.Smoos + stop.Smagnet + "\n"
    print("LM: " + listLM)

    listRB = stop.Scliff + stop.Sarlo + stop.Ssierra + stop.Sgiovanni + "\n"
    print("RB: " + listRB)
    
    listRR = stop.Srelaxo + stop.Skarpador + stop.Skanto + stop.Snormal + stop.Swasser + stop.Sfeuer + stop.Sdrache + stop.Sflug + stop.Spflanze + stop.Skaefer + stop.Sboden + stop.Sgestein + stop.Sgift + stop.Spsycho + stop.Skampf + stop.Seis + stop.Sgeist + stop.Selektro + stop.Sfee + stop.Sstahl + stop.Sunlicht + "\n"
    print("RR: " + listRR)    
    print("Wert i: "+ str(i))   # summe gesamt
    print("Wert j: "+ str(j))   # bosse
    print("Wert k: "+ str(k))   # rocket stops
    print("Wert Liste:" + str(send.list_boss_output.__len__()))
    if j == send.list_boss_output.__len__():
      changed = False
      print("false")
    if changed == True:
      print("changed: "+ str(j))
      boss_message = self.list_boss(send,sql,cfg)
    bossid = send.sendBoss(boss_message)

    message_overview_rocket = listLM + listRB + listRR + "\n...Aktuell " + str(i-j) + " <a href='" + cfg.chatUrl +"/'>Team Rocket Stops:</a> \n\n"

    message += "\n <a href='" + cfg.chatUrl +"/" + str(bossid) + "'>" + "Hier gehts zu den Bossen</a>"
    lockmodul_message = self.list_lockmodul(send,sql,cfg)
    send.sendOverview(message_overview_rocket + message,lockmodul_message)
#    send.sendOverview(message_overview_rocket + message,message_overview_lockmodul + lockmodul_message)
#    send.sendOverview(message_overview_lockmodul + message_overview_rocket + message_overview_boss + message,lockmodul_message)



  def list_boss(self,send,sql,cfg):
    boss_message = ""
    message_overview_boss = ""
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0
    j = 0
    for name in sql.name:
      if send.list_boss_output.__contains__(name):
        f = open(cfg.areaName+"boss-output.txt", "r")
              # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        typ = stop.getType(sql.incident_grunt_type[i])
        id = list_string[send.list_boss_output.index(name)]
#        boss_message += '\U0001f4cd'+ "<a href='https://t.me/pogoquestbw/" + str(id) + "'>" + name + "</a>" + "\n" + "  \U00002514 Ende " + str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute)))+ " | " + typ + "\n"
        boss_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + name + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        j +=1
#        i +=1
      i +=1
      message_overview_boss = stop.Sarlo + stop.Scliff + stop.Ssierra + stop.Sgiovanni + "\n\n" + "Aktuell " + str(j) + " <a href='" + cfg.chatUrl +"/'>Rocket Boss Stops:</a> \n\n"
    return message_overview_boss + boss_message

  def list_lockmodul(self,send,sql,cfg):
    lockmodul_message = ""
    message_overview_lockmodul = ""
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0
    j = 0
    lm= 0
    for name in sql.Lname:
      if send.list_lockmodul_output.__contains__(name):
        f = open(cfg.areaName+"lockmodul-output.txt", "r")
              # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.Lincident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        typ = stop.getType(sql.Lincident_grunt_type[i])
#        id = list_string[j]
        id = list_string[send.list_lockmodul_output.index(name)]
#        lockmodul_message += '\U0001f4cd'+ "<a href='https://t.me/pogoquestbw/" + str(id) + "'>" + name + "</a>" + "\n" + "  \U00002514 Ende " + str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute)))+ " | " + typ + "\n"
        lockmodul_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + name + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        j +=1
        i +=1
        lm+=1
      else:
        stopName = sql.Lname[i]
        latitude = sql.Llatitude[i]
        longitude = sql.Llongitude[i]
        typ = stop.getType(sql.Lincident_grunt_type[i])
        zeit = sql.Lincident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)

        
        bolt_line = typ + " \U0001f55b Ende " + str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute)))

        id = send.singleStops(bolt_line,stopName,latitude,longitude,sql.Lincident_grunt_type[i])
#        lockmodul_message += str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + "|" +typ + "|"+ "<a href='https://t.me/pogoquestbw/" + str(id) + "'>" + stopName + "</a>" + "\n"
        lockmodul_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + name + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        i +=1
        lm+=1
      message_overview_lockmodul = stop.Sstandard + stop.Sgletscher + stop.Smoos + stop.Smagnet + "\n\n" + "Aktuell " + str(lm) + " <a href='" + cfg.chatUrl +"/'>Lock Modul an folgendem Stop:</a> \n\n"
#      lockmodul_message = message_overview_lockmodul + lockmodul_message
#    return lockmodul_message
    return message_overview_lockmodul + lockmodul_message