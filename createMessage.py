import helper
import stopType
import datetime
import time


class createMessage():
  def create(self,send,sql,cfg,timer,newMessageAfter):
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0 # summe gesamt
    rb = 0 # bosse = j
    rr = 0 # rocket stops = k
    lm= 0
    ilen = 0
    message = ""
    boss_message = send.oldBossMessage
    lockmodul_message = ""
    changed = True
    
    if timer > newMessageAfter:
      timer = 0
      print("=== NEW SEND ===")
    else:
      print(str(timer))
      print("\n")
      print(str(newMessageAfter))
    
    if cfg.chatId != cfg.singlechatId:
      newSend = newMessageAfter - timer
      print("Rüpel Liste neu Senden in " + str(newSend) + " Sekunden")


    #now time
    now = datetime.datetime.now()
    print("\n\n-------------------------------------- Update " + cfg.areaName + cfg.areaNumber + " " + now.strftime("%m/%d/%Y, %H:%M:%S") + " --------------------------------------\n")
    print("gefundene Pokestops: " + str(len(sql.name)) + "\n")
    ilen = len(sql.name)

    for name in sql.Lname:
      stop.getType(sql.Lincident_grunt_type[lm])
      lm +=1

    for name in sql.name:
      stopName = "Unknown Stop" if name is None else name
      if send.list_output.__contains__(name):
        f = open(cfg.areaName+cfg.areaNumber+"output.txt", "r")
            # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        stop.getType(sql.incident_grunt_type[i])
        id = list_string[send.list_output.index(stopName)]
        # erste nachricht
        if i < 45:
          message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        elif i == 46:
          message += "\n\U00002514 Limit der Liste erreicht...\n"
        rr +=1
      elif send.list_boss_output.__contains__(stopName):
        stop.getType(sql.incident_grunt_type[i])
        rb +=1
      else:
        #stopName = sql.name[i]
        latitude = sql.latitude[i]
        longitude = sql.longitude[i]
        stop.getType(sql.incident_grunt_type[i])
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        print("... verarbeite Pokestop: " + str(stopName))
        bolt_line = str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " " + stop.Emoji + stop.Infotext       
        id = send.singleStops(bolt_line,stopName,latitude,longitude,sql.incident_grunt_type[i])
        if sql.incident_grunt_type[i] > 40 and sql.incident_grunt_type[i] < 45:
          boss_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
          rb +=1
        else:
          # update Nachricht
          if i < 45:
            message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
          elif i == 46:
            message += "\n\U00002514 Limit der Liste erreicht...\n"
        print("Rocket Stop " + str(i+1) + "/" + str(len(sql.name)) + " ===> message len: " + str(len(message)))
      i +=1
    
    if rb == send.list_boss_output.__len__():
      changed = False
      print("Finish !\n")
      if rb > 0:
        print("Rocket Bosse: "+ str(rb))
      if rr > 0:
        print("Rocket Rüpel: "+ str(rr))
    if changed:
      print("changed: "+ str(rb))
    boss_message = self.list_boss(send,sql,cfg)
    bossid = send.sendBoss(boss_message,rb)

    # define lists
    listLM = stop.Sstandard + stop.Sgletscher + stop.Smoos + stop.Smagnet
    listRR = stop.Srelaxo + stop.Skarpador + stop.Skanto + stop.Snormal + stop.Swasser + stop.Sfeuer + stop.Sdrache + stop.Sflug + stop.Spflanze + stop.Skaefer + stop.Sboden + stop.Sgestein + stop.Sgift + stop.Spsycho + stop.Skampf + stop.Seis + stop.Sgeist + stop.Selektro + stop.Sfee + stop.Sstahl + stop.Sunlicht
    listRB = stop.Sarlo + stop.Scliff + stop.Ssierra + stop.Sgiovanni

    print("\nListen:\n")

    print("LM: "+ listLM)
    print("RR: "+ listRR)   
    print("RB: "+ listRB + "\n")
    
    if listLM:
      listLM = "L: " + listLM + "\n"

    if listRR:
      listRR = "R: " + listRR + "\n"

    if listRB:
      listRB = "B: " + listRB + "\n"
    
    message_overview_rocket = listLM + listRR + listRB + "\n" + "<b>Aktuell " + str(i-rb) + " <a href='" + cfg.chatUrl +"/'>Team Rocket Stops:</a></b> \n\n"

    if not rb == 0:
      message += "\n <a href='" + cfg.chatUrl +"/" + str(bossid) + "'>" + "<b>Hier gehts zu den Bossen</b></a>"

    lockmodul_message = self.list_lockmodul(send,sql,cfg)
    send.sendOverview(message_overview_rocket + message,ilen,rb,rr,lockmodul_message,lm,timer,newMessageAfter)


  def list_boss(self,send,sql,cfg):
    boss_message = ""
    message_overview_boss = ""
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0
    rb = 0
    for name in sql.name:
      stopName = "Unknown Stop" if name is None else name
      if send.list_boss_output.__contains__(name):
        f = open(cfg.areaName+cfg.areaNumber+"boss-output.txt", "r")
              # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        stop.getType(sql.incident_grunt_type[i])
        id = list_string[send.list_boss_output.index(stopName)]
        boss_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        rb +=1
      i +=1
      message_overview_boss = stop.Sarlo + stop.Scliff + stop.Ssierra + stop.Sgiovanni + "\n\n" + "<b>Aktuell " + str(rb) + " <a href='" + cfg.chatUrl +"/'>Rocket Boss Stops:</a></b> \n\n"
    return message_overview_boss + boss_message

  def list_lockmodul(self,send,sql,cfg):
    lockmodul_message = ""
    message_overview_lockmodul = ""
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0
    lm= 0
    for name in sql.Lname:
      stopName = "Unknown Stop" if name is None else name
      if send.list_lockmodul_output.__contains__(name):
        f = open(cfg.areaName+cfg.areaNumber+"lockmodul-output.txt", "r")
              # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.Lincident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        stop.getType(sql.Lincident_grunt_type[i])
        id = list_string[send.list_lockmodul_output.index(stopName)]
        lockmodul_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        lm+=1
        text_modul = "Modul:" if lm == 1 else "Module:"
      else:
        #stopName = sql.Lname[i]
        latitude = sql.Llatitude[i]
        longitude = sql.Llongitude[i]
        stop.getType(sql.Lincident_grunt_type[i])
        zeit = sql.Lincident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        bolt_line = str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " " + stop.Emoji + stop.Infotext
        id = send.singleStops(bolt_line,stopName,latitude,longitude,sql.Lincident_grunt_type[i])
        lockmodul_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        lm+=1
        text_modul = "Modul:" if lm == 1 else "Module:"
      i +=1
      message_overview_lockmodul = stop.Sstandard + stop.Sgletscher + stop.Smoos + stop.Smagnet + "\n\n" + "<b>Aktuell " + str(lm) + " <a href='" + cfg.chatUrl +"/'>Lock " + text_modul + "</a></b> \n\n"
    return message_overview_lockmodul + lockmodul_message