import helper
import stopType
import datetime
import time
import json

class createMessage():
  def create(self,send,sql,cfg,timer,newMessageAfter,gmt):
    
### can be configured custom ###
    
    rb_limit = 48                 # Boss Limit
    rr_limit = 45                 # Rüpel Limit
    lm_limit = 48                 # Lockmodul Limit
    rb_types = [41,42,43,44]      # Boss Types
    lm_types = [501,502,503,504]  # Lockmodul Types
    newSortAfterLimit = True      # True or False

################################

    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0
    rb_sum = 0
    rr_sum = 0
    rb = 0
    rr = 0
    old_rr = 0
    lm= 0
    boss_message = send.oldBossMessage
    message = ""
    lockmodul_message = ""
    changed = True    
    
    if timer > newMessageAfter:
      timer = 0
    
    if cfg.chatId != cfg.singlechatId:
      newSend = newMessageAfter - timer
      print("Rüpel Liste neu Senden in " + str(newSend) + " Sekunden")

    if newSortAfterLimit == 1:
      with open(cfg.areaName+cfg.areaNumber+"/output.txt") as input:
        arrays = json.load(input)
        anzahl_rr = len(arrays)
      rr_list_limit = rr_limit-1

    #now time
    now = datetime.datetime.now()
    print("\n\n####################==========\\ *** Rocket *** Update " + cfg.areaName + " " + now.strftime("%m/%d/%Y, %H:%M:%S") + " /==========####################\n")
    print("gefundene Pokestops: " + str(len(sql.name)) + "\n")

    for name in sql.Lname:
      stop.getType(sql.Lincident_grunt_type[lm])
      lm +=1

    # Output for Console
    for typ in sql.incident_grunt_type:
      if typ in (rb_types):
        rb_sum +=1
      else:
        rr_sum +=1

    for name in sql.name:
      stopName = "Unknown Stop" if name is None else name
      if send.list_output.__contains__(name) and cfg.rocketStops == True:
        f = open(cfg.areaName+cfg.areaNumber+"/output.txt", "r")
            # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=gmt)
        stop.getType(sql.incident_grunt_type[i])
        id = list_string[send.list_output.index(name)]

        if cfg.singlechatId:
          linked = cfg.singlechatUrl + "/" + str(id)
        else:
          linked = "https://maps.google.de/?q=" + str(sql.latitude[i]) + ", " + str(sql.longitude[i])

        # update nachricht
        if sql.incident_grunt_type[i] not in (rb_types):
          if newSortAfterLimit == True:
            if anzahl_rr > rr_limit:
              message = "\u270BLimit der Liste erreicht...\n\U00002514 <b>" + str(rr_limit-rr_list_limit) + "</b> Stops ausgeblendet\n\n"
              rr_limit+=1
            else:
              message += stop.Emoji + "<a href='" + linked + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
          else:
            if rr < rr_limit:
              message += stop.Emoji + "<a href='" + linked + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
            elif rr == rr_limit+1:
              message += "\n\U00002514 Limit der Liste erreicht...\n"
          rr +=1
          old_rr +=1
      elif send.list_boss_output.__contains__(name):
        stop.getType(sql.incident_grunt_type[i])
        if sql.incident_grunt_type[i] in (rb_types):
          rb +=1
      else:
        if cfg.rocketStops == True or sql.incident_grunt_type[i] in (rb_types):
          latitude = sql.latitude[i]
          longitude = sql.longitude[i]
          stop.getType(sql.incident_grunt_type[i])
          zeit = sql.incident_expiration[i]
          zeit = zeit + datetime.timedelta(hours=gmt)
          #print("... verarbeite Pokestop: " + str(stopName))

          bolt_line = str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " " + stop.Emoji + stop.Infotext
          
          if cfg.singlechatId:
            id = send.singleStops(bolt_line,name,latitude,longitude,sql.incident_grunt_type[i],lm_types,rb_types)
            linked = cfg.singlechatUrl + "/" + str(id)
          else:
            linked = "https://maps.google.de/?q=" + str(sql.latitude[i]) + ", " + str(sql.longitude[i])

          # erste Nachricht
          if sql.incident_grunt_type[i] in (rb_types):
            print("Send " + str(rb+1) + "/" + str(rb_sum) + " ===> " + "Rocket BOSSE: " + str(stopName))
            rb +=1
          else:
            if rr < rr_limit:
              message += stop.Emoji + "<a href='" + linked + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
            #elif rr == rr_limit+1:
            #  message += "\n\U00002514 Limit der Liste erreicht...\n"
            print("Send " + str(rr+1) + "/" + str(rr_sum) + " ===> " + "Rocket RÜPEL: " + str(stopName))
            rr +=1
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
    boss_message = self.list_boss(send,sql,cfg,rb_types,rb_limit,gmt)
    bossid = send.sendBoss(boss_message,rb)

    if cfg.lureModule == True:
      lockmodul_message = self.list_lockmodul(send,sql,cfg,lm_types,rb_types,lm_limit,gmt)
      send.sendLockmodul(True,lockmodul_message)

    # define lists
    listLM = stop.Sstandard + stop.Sgletscher + stop.Smoos + stop.Smagnet
    listRR = stop.Srelaxo + stop.Skarpador + stop.Skanto + stop.Snormal + stop.Swasser + stop.Sfeuer + stop.Sdrache + stop.Sflug + stop.Spflanze + stop.Skaefer + stop.Sboden + stop.Sgestein + stop.Sgift + stop.Spsycho + stop.Skampf + stop.Seis + stop.Sgeist + stop.Selektro + stop.Sfee + stop.Sstahl + stop.Sunlicht
    listRB = stop.Scliff + stop.Sarlo + stop.Ssierra + stop.Sgiovanni

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
    
    message_overview_rocket = listLM + listRR + listRB + "\n" + "<b>Aktuell " + str(rr) + " <a href='" + cfg.chatUrl +"/'>Team Rocket Stops:</a></b> \n\n"

    if not rb == 0:
      message += "\n <a href='" + cfg.chatUrl +"/" + str(bossid) + "'>" + "<b>Hier gehts zu den Bossen</b></a>"

    if cfg.rocketStops == True:
      #lockmodul_message = self.list_lockmodul(send,sql,cfg,lm_types,rb_types,lm_limit,gmt)
      send.sendOverview(message_overview_rocket + message,rb,rr,old_rr,lockmodul_message,lm,timer,newMessageAfter)


  def list_boss(self,send,sql,cfg,rb_types,rb_limit,gmt):
    boss_message = ""
    message_overview_boss = ""
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0
    rb = 0
    for name in sql.name:
      stopName = "Unknown Stop" if name is None else name
      if send.list_boss_output.__contains__(name):
        f = open(cfg.areaName+cfg.areaNumber+"/boss-output.txt", "r")
              # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=gmt)
        stop.getType(sql.incident_grunt_type[i])
        id = list_string[send.list_boss_output.index(name)]

        if cfg.singlechatId:
          linked = cfg.singlechatUrl + "/" + str(id)
        else:
          linked = "https://maps.google.de/?q=" + str(sql.latitude[i]) + ", " + str(sql.longitude[i])

        if sql.incident_grunt_type[i] in (rb_types):
          if rb < rb_limit:
            boss_message += stop.Emoji + "<a href='" + linked + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
          elif rb == rb_limit+1:
            boss_message += "\n\U00002514 Limit der Liste erreicht...\n"
          rb +=1
      elif not cfg.singlechatId:
        stop.getType(sql.incident_grunt_type[i])
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=gmt)
        
        linked = "https://maps.google.de/?q=" + str(sql.latitude[i]) + ", " + str(sql.longitude[i])

        if sql.incident_grunt_type[i] in (rb_types):
          if rb < rb_limit:
            boss_message += stop.Emoji + "<a href='" + linked + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
          elif rb == rb_limit+1:
            boss_message += "\n\U00002514 Limit der Liste erreicht...\n"
          rb +=1
      i +=1
      if not rb == 0:
        message_overview_boss = stop.Scliff + stop.Sarlo + stop.Ssierra + stop.Sgiovanni + "\n\n" + "<b>Aktuell " + str(rb) + " <a href='" + cfg.chatUrl +"/'>Rocket Boss Stops:</a></b> \n\n"
    return message_overview_boss + boss_message

  def list_lockmodul(self,send,sql,cfg,lm_types,rb_types,lm_limit,gmt):
    lockmodul_message = ""
    message_overview_lockmodul = ""
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0
    lm= 0
    for name in sql.Lname:
      stopName = "Unknown Stop" if name is None else name
      if send.list_lockmodul_output.__contains__(name):
        f = open(cfg.areaName+cfg.areaNumber+"/lockmodul-output.txt", "r")
              # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.Lincident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=gmt)
        stop.getType(sql.Lincident_grunt_type[i])
        id = list_string[send.list_lockmodul_output.index(name)]

        if cfg.singlechatId:
          linked = cfg.singlechatUrl + "/" + str(id)
        else:
          linked = "https://maps.google.de/?q=" + str(sql.Llatitude[i]) + ", " + str(sql.Llongitude[i])

        if lm < lm_limit:
          lockmodul_message += stop.Emoji + "<a href='" + linked + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        elif lm == lm_limit+1:
          lockmodul_message += "\n\U00002514 Limit der Liste erreicht...\n"
        lm+=1
        text_modul = "Modul:" if lm == 1 else "Module:"
      else:
        stop.getType(sql.Lincident_grunt_type[i])
        zeit = sql.Lincident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=gmt)
        bolt_line = str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " " + stop.Emoji + stop.Infotext
        
        if cfg.singlechatId:
          id = send.singleStops(bolt_line,name,sql.Llatitude[i],sql.Llongitude[i],sql.Lincident_grunt_type[i],lm_types,rb_types)
          linked = cfg.singlechatUrl + "/" + str(id)
        else:
          linked = "https://maps.google.de/?q=" + str(sql.Llatitude[i]) + ", " + str(sql.Llongitude[i])

        if lm < lm_limit:
          lockmodul_message += stop.Emoji + "<a href='" + linked + "'>" + str(stopName) + "</a>" + "\n\U00002514 <b>" + str(zeit.hour) + ":" + str(Help.nice_time(str(zeit.minute)))+ "</b> "  + stop.Infotext + "\n"
        elif lm == lm_limit+1:
          lockmodul_message += "\n\U00002514 Limit der Liste erreicht...\n"
        lm+=1
        text_modul = "Modul:" if lm == 1 else "Module:"
      i +=1
      message_overview_lockmodul = stop.Sstandard + stop.Sgletscher + stop.Smoos + stop.Smagnet + "\n\n" + "<b>Aktuell " + str(lm) + " <a href='" + cfg.chatUrl +"/'>Lock " + text_modul + "</a></b> \n\n"
    return message_overview_lockmodul + lockmodul_message