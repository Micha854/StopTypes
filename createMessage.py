import helper
import stopType
import datetime


class createMessage():
  def create(self,send,sql,cfg):
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0 # summe gesamt
    j = 0 # bosse
    k = 0 # rocket stops
    lm= 0
    newk = 0
    message = ""
    boss_message = send.oldBossMessage
    lockmodul_message = ""
    changed = True
    
    #now time
    now = datetime.datetime.now()
    print("\n\n-------------------------------------- Update " + cfg.areaName + cfg.areaNumber + " " + now.strftime("%m/%d/%Y, %H:%M:%S") + " --------------------------------------\n")
    print("gefundene Pokestops: " + str(len(sql.name)) + "\n")
    newk = len(sql.name)

    for name in sql.Lname:
      typ = stop.getType(sql.Lincident_grunt_type[lm])
      lm +=1

    for name in sql.name:
      if send.list_output.__contains__(name):
        f = open(cfg.areaName+cfg.areaNumber+"output.txt", "r")
            # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        typ = stop.getType(sql.incident_grunt_type[i])
        id = list_string[send.list_output.index(name)]
        # erste nachricht
        message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(name) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        k +=1
        i +=1
      elif send.list_boss_output.__contains__(name):
        typ = stop.getType(sql.incident_grunt_type[i])
        j +=1
        i +=1
      else:
        stopName = sql.name[i]
        latitude = sql.latitude[i]
        longitude = sql.longitude[i]
        typ = stop.getType(sql.incident_grunt_type[i])
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        print("... verarbeite Pokestop: " + str(stopName))
        bolt_line = str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " " + stop.Emoji + stop.Infotext       
        id = send.singleStops(bolt_line,stopName,latitude,longitude,sql.incident_grunt_type[i])
        if sql.incident_grunt_type[i] > 40 and sql.incident_grunt_type[i] < 45:
          boss_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(name) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
          j +=1
        else:
          # update Nachricht
          message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + str(name) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        i +=1
    
    if j == send.list_boss_output.__len__():
      changed = False
      print("Finish !\n")
      if j > 0:
        print("Rocket Bosse: "+ str(j))
      if k > 0:
        print("Rocket Rüpel: "+ str(k))
    if changed:
      print("changed: "+ str(j))
    boss_message = self.list_boss(send,sql,cfg)
    bossid = send.sendBoss(boss_message)

    # define lists
    listLM = stop.Sstandard + stop.Sgletscher + stop.Smoos + stop.Smagnet
    listRR = stop.Srelaxo + stop.Skarpador + stop.Skanto + stop.Snormal + stop.Swasser + stop.Sfeuer + stop.Sdrache + stop.Sflug + stop.Spflanze + stop.Skaefer + stop.Sboden + stop.Sgestein + stop.Sgift + stop.Spsycho + stop.Skampf + stop.Seis + stop.Sgeist + stop.Selektro + stop.Sfee + stop.Sstahl + stop.Sunlicht
    listRB = stop.Sarlo + stop.Scliff + stop.Ssierra + stop.Sgiovanni

    print("\nListen:\n")

    print("LM: "+ listLM)
    print("RR: "+ listRR)   
    print("RB: "+ listRB + "\n")
    
    if listLM:
      listLM = "L: " + listLM
      u1 = "\n"
    else:
      u1 = ''

    if listRR:
      listRR = "R: " + listRR
      u2 = "\n"
    else:
      u2 = ''

    if listRB:
      listRB = "B: " + listRB
    
    message_overview_rocket = listLM + u1 + listRR + u2 + listRB + "\n\n" + "<b>Aktuell " + str(i-j) + " <a href='" + cfg.chatUrl +"/'>Team Rocket Stops:</a></b> \n\n"

    message += "\n <a href='" + cfg.chatUrl +"/" + str(bossid) + "'>" + "<b>Hier gehts zu den Bossen</b></a>"
    lockmodul_message = self.list_lockmodul(send,sql,cfg)
    send.sendOverview(message_overview_rocket + message,newk,j,k,lockmodul_message)


  def list_boss(self,send,sql,cfg):
    boss_message = ""
    message_overview_boss = ""
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0
    j = 0
    for name in sql.name:
      if send.list_boss_output.__contains__(name):
        f = open(cfg.areaName+cfg.areaNumber+"boss-output.txt", "r")
              # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        typ = stop.getType(sql.incident_grunt_type[i])
        id = list_string[send.list_boss_output.index(name)]
        boss_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + name + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        j +=1
      i +=1
      message_overview_boss = stop.Sarlo + stop.Scliff + stop.Ssierra + stop.Sgiovanni + "\n\n" + "<b>Aktuell " + str(j) + " <a href='" + cfg.chatUrl +"/'>Rocket Boss Stops:</a></b> \n\n"
    return message_overview_boss + boss_message

  def list_lockmodul(self,send,sql,cfg):
    lockmodul_message = ""
    message_overview_lockmodul = ""
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0
    lm= 0
    for name in sql.Lname:
      if send.list_lockmodul_output.__contains__(name):
        f = open(cfg.areaName+cfg.areaNumber+"lockmodul-output.txt", "r")
              # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.Lincident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        typ = stop.getType(sql.Lincident_grunt_type[i])
        id = list_string[send.list_lockmodul_output.index(name)]
        lockmodul_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + name + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        i +=1
        lm+=1
        if lm == 1:
          text_modul = "Modul:"
        else:
          text_modul = "Module:"
      else:
        stopName = sql.Lname[i]
        latitude = sql.Llatitude[i]
        longitude = sql.Llongitude[i]
        typ = stop.getType(sql.Lincident_grunt_type[i])
        zeit = sql.Lincident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        bolt_line = str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " " + stop.Emoji + stop.Infotext
        id = send.singleStops(bolt_line,stopName,latitude,longitude,sql.Lincident_grunt_type[i])
        lockmodul_message += stop.Emoji + "<a href='" + cfg.singlechatUrl +"/" + str(id) + "'>" + name + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        i +=1
        lm+=1
        if lm == 1:
          text_modul = "Modul:"
        else:
          text_modul = "Module:"
      message_overview_lockmodul = stop.Sstandard + stop.Sgletscher + stop.Smoos + stop.Smagnet + "\n\n" + "<b>Aktuell " + str(lm) + " <a href='" + cfg.chatUrl +"/'>Lock " + text_modul + "</a></b> \n\n"
    return message_overview_lockmodul + lockmodul_message