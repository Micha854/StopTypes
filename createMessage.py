#!/usr/bin/env python
# -*- coding: utf-8 -*-

import helper
import stopType
import time

class createMessage():
  message_rocket = ""
  message_lockmodul = ""
  message_overview_rocket = ""
  message_overview_lockmodul = ""
  message = ""
  def create(self,Sql,typ,hours):
    Help = helper.Helper()
    StopTyp = stopType.stopType()
    
    #Aufteilung des Ergebnisses aus der MySQL-Abfrage in Listen
    list_name = Help.split_string(Sql.name[2:len(Sql.name)-3])
    list_latitude = Help.split_string(Sql.latitude[2:len(Sql.latitude)-3])
    list_longitude = Help.split_string(Sql.longitude[2:len(Sql.longitude)-3])
    list_type = Help.split_string(Sql.typ[2:len(Sql.typ)-3])
    list_time = Help.split_string_time(Sql.zeit)
    i = 0	#Parameter i geht die einzelnen einträge durch
    j = 1	#Parameter j geht die list_time durch, da diese Liste anders aufgebaut ist
    run = len(list_name)
    #Iteration durch alle Einträge
    if len(str(list_name)) == 4:
      if typ == "rocket":
        self.message_rocket = "Aktuell keine Rocketstops"
        run = 0 
      elif typ == "lockmodul":
        self.message_lockmodul = "Z\U000000fcnd doch welche"
        run = 0
    if run == 1:
      list_name = Help.split_string(Sql.name[2:len(Sql.name)-4])
      list_latitude = Help.split_string(Sql.latitude[2:len(Sql.latitude)-4])
      list_longitude = Help.split_string(Sql.longitude[2:len(Sql.longitude)-4])
      list_type = Help.split_string(Sql.typ[2:len(Sql.typ)-4])

    while i < run:
      try:
        pokestopName = list_name[i]
        pokestopLatitude = list_latitude[i]
        pokestopLongitude = list_longitude[i]
        pokestopTyp = StopTyp.getType(int(list_type[i]))
        zeit = list_time[j]
      except:
        print("Index out of range! Generiere Nachricht neu")
        return self.create(Sql,typ,hours)	
      pokestopName = pokestopName[1:len(pokestopName)-1] 		
      pokestopLatitude = pokestopLatitude[0:10]		
      pokestopLongitude = pokestopLongitude[0:10]	

      #Zeitangabe zusammenbauen aus einzelnen einträgen        
      Newtime = Help.split_string_stunden(zeit)
      stunden = (int(Newtime[3]) + int(hours)) % 24
      minute = Newtime[4]
      minute = minute[1:len(minute)]
      minute = str(minute)
      minute = Help.split_string_minuten(minute)
      minute = Help.nice_time(str(minute[0]))

      message_location = '\U0001f4cd'+ "<a href='https://maps.google.de/?q=" + pokestopLatitude + "," + pokestopLongitude +"'" + ">" +  pokestopName + "</a>" + "\n"
      message_time = " " +'\U0001f55b' + " Ende " + str(stunden) + ":" + minute + " "  + "\n\n"

      if typ == "rocket":
        message_type = pokestopTyp
        self.message_rocket += message_location + message_type + message_time
      elif typ == "lockmodul":
        message_type = pokestopTyp
        self.message_lockmodul += message_location + message_type + message_time

      j +=1
      i +=1
    if typ == "rocket":
      self.message_overview_rocket ="Aktuell " + str(run) + " Rocket Stops: \n\n" + StopTyp.Skanto + StopTyp.Srelaxo + StopTyp.Sgestein + StopTyp.Seis +StopTyp.Sgeist + StopTyp.Selektro +StopTyp.Sfee + StopTyp.Sstahl + StopTyp.Sunlicht+ StopTyp.Skaefer + StopTyp.Sfeuer + StopTyp.Sdrache + StopTyp.Skampf + StopTyp.Sflug + StopTyp.Spflanze + StopTyp.Sboden + StopTyp.Snormal + StopTyp.Sgift + StopTyp.Spsycho + StopTyp.Swasser + StopTyp.Skarpador + "\n\n"
    elif typ == "lockmodul":
      self.message_overview_lockmodul ="Aktuell " + str(run) + " Lockmodule: \n\n" + StopTyp.Snormal + StopTyp.Sgletscher + StopTyp.Smoos + StopTyp.Smagnet + "\n\n"

    ####Erstellung der finalen Nachricht
    self.message = self.message_overview_rocket + self.message_rocket + self.message_overview_lockmodul + self.message_lockmodul