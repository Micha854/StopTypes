import helper
import stopType
import datetime


class createMessage():
  message = ""
  message2= ""
  def create(self,send,sql,verlinkung):
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0
    j = 0
    message = ""
    message2= ""
    boss_message = send.oldBossMessage
    boss_message2= send.oldBossMessage2
    changed = True
    print("ANzahl namen: "+str(len(sql.name)))
    for name in sql.name:
      if send.list_output.__contains__(name):
        f = open(send.filename+"output.txt", "r")
            # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        typ = stop.getType(sql.incident_grunt_type[i])
        id = list_string[send.list_output.index(name)]
        if len(message) > 5000:
          message2 += str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " |" +str(typ) + " | "+ "<a href='"+ verlinkung + str(id) + "'>" + str(name) + "</a>" + "\n"
          message = message
        else:
          message += str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " |" +str(typ) + " | "+ "<a href='"+ verlinkung + str(id) + "'>" + str(name) + "</a>" + "\n"
        i +=1
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

        bolt_line = typ + " \u23F1 Ende " + str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute)))

        id = send.singleStops(bolt_line,stopName,latitude,longitude,sql.incident_grunt_type[i])
        if sql.incident_grunt_type[i] > 40 and sql.incident_grunt_type[i] < 45:
          if len(boss_message) > 5000:
            boss_message2 += str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " |" +str(typ) + "| " + "<a href='"+verlinkung + str(id) + "'>" + str(stopName) + "</a>" + "\n"
            boss_message = boss_message
          else:
            boss_message += str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " |" +str(typ) + "| " + "<a href='"+verlinkung + str(id) + "'>" + str(stopName) + "</a>" + "\n"
          j +=1
        else:
          #message += '\U0001f4cd'+ "<a href='https://t.me/TraunsteinTeamRocket/" + str(id) + "'>" + stopName + "</a>" + "\n" + "  \U00002514 Ende " + str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " | " + typ + "\n"
          if len(message) > 5000:
            message2 += str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " |" +str(typ) + " | "+ "<a href='"+verlinkung + str(id) + "'>" + str(stopName) + "</a>" + "\n"
            message = message
          else:
            message += str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute))) + " |" +str(typ) + " | "+ "<a href='"+verlinkung + str(id) + "'>" + str(stopName) + "</a>" + "\n"
        i +=1
    
    len_message = len(message)
    len_boss = len(boss_message)
    len_message2 = len(message2)
    len_boss2 = len(boss_message2)

    print("Wert j: "+ str(j))
    print("Wert Liste:" + str(send.list_boss_output.__len__()))
    
    print(" Boss msg 1: (" + str(len_boss) + " characters --------------------------------------------------------------)\n\n" + boss_message)
    print(" Boss msg 2: (" + str(len_boss2) + " characters -------------------------------------------------------------)\n\n" + boss_message2)
    print("Rüpel msg 1: (" + str(len_message) + " characters -----------------------------------------------------------)\n\n" + message)
    print("Rüpel msg 2: (" + str(len_message2) + " characters ----------------------------------------------------------)\n\n" + message2)
    

    if j == send.list_boss_output.__len__():
      changed = False
    if changed:
      boss_message = self.list_boss(send,sql,verlinkung)
    bossid = send.sendBoss(boss_message, boss_message2)
    message_overview_rocket ="Aktuell " + str(i-j) + " Team Rocket Stops: \n\n" + stop.Skanto + stop.Srelaxo + stop.Sgestein + stop.Seis +stop.Sgeist + stop.Selektro +stop.Sfee + stop.Sstahl + stop.Sunlicht+ stop.Skaefer + stop.Sfeuer + stop.Sdrache + stop.Skampf + stop.Sflug + stop.Spflanze + stop.Sboden + stop.Snormal + stop.Sgift + stop.Spsycho + stop.Swasser + stop.Skarpador + "\n\n"

    

    if(j > 0):
      if len(message2) > 5:
        message2 += "\n <a href='"+verlinkung + str(bossid) + "'" + ">" + "Hier" + " gehts zu den Bossen</a>"
      else:
        message += "\n <a href='"+verlinkung + str(bossid) + "'" + ">" + "Hier" + " gehts zu den Bossen</a>"
    else:
      message += "\n <b>Aktuell keine Bosse vorhanden</b>"

    send.sendOverview(message_overview_rocket + message, message2)

  def list_boss(self,send,sql,verlinkung):
    boss_message = ""
    boss_message2= ""
    Help = helper.Helper()
    stop = stopType.stopType()
    i = 0
    for name in sql.name:
      if send.list_boss_output.__contains__(name):
        f = open(send.filename+"boss-output.txt", "r")
              # Split the string based on space delimiter 
        list_string = f.read()
        list_string = list_string[1:len(list_string)-1]
        f.close()
        list_string = list_string.split(', ') 
        zeit = sql.incident_expiration[i]
        zeit = zeit + datetime.timedelta(hours=1)
        typ = stop.getType(sql.incident_grunt_type[i])
        id = list_string[send.list_boss_output.index(name)]
        boss_message += str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute)))+ " |"  +str(typ) + "| " + "<a href='"+verlinkung + str(id) + "'>" + str(name) + "</a>" + "\n"
        boss_message2 += str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute)))+ " |"  +str(typ) + "| " + "<a href='"+verlinkung + str(id) + "'>" + str(name) + "</a>" + "\n"
      i +=1
    return boss_message + boss_message2