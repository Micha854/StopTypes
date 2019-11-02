#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import time
####Abfrage der Daten aus der MySQL Datenbank

class Sql():
  name = ""
  latitude = ""
  longitude = ""
  typ = ""
  zeit = ""
  def startSQL(self,cfg,typ,expirationType):
    #Verbindungsaufbau zur MySQL-Datenbank
    try:
      connection = MySQLdb.connect(host=cfg.host,db=cfg.database,user=cfg.user, passwd=cfg.password)
      cursor = connection.cursor()
    except:
      print("Kein Verbindungsaufbau zur Datenbank, probiere es in 15 Sekunden erneut\n")
      time.sleep(15)
      return self.startSQL(cfg,typ,expirationType)


    #Abfragen der Daten aus der Datenbank

    sql = "SELECT name FROM pokestop where longitude BETWEEN " + cfg.min_longitude + " AND " + cfg.max_longitude + " AND latitude BETWEEN " + cfg.min_latitude + " AND " + cfg.max_latitude + " AND timestampdiff(SECOND," + expirationType + ",NOW())<7200 ORDER BY "+expirationType
    MySQLname = cursor.execute(sql)
    name = cursor.fetchall()
    self.name = str(name)

    sql = "SELECT latitude FROM pokestop where longitude BETWEEN " + cfg.min_longitude + " AND " + cfg.max_longitude + " AND latitude BETWEEN " + cfg.min_latitude + " AND " + cfg.max_latitude + " AND timestampdiff(SECOND," + expirationType + ",NOW())<7200 ORDER BY "+expirationType
    MySQLlatitude = cursor.execute(sql)
    latitude = cursor.fetchall()
    self.latitude = str(latitude)

    sql = "SELECT longitude FROM pokestop where longitude BETWEEN " + cfg.min_longitude + " AND " + cfg.max_longitude + " AND latitude BETWEEN " + cfg.min_latitude + " AND " + cfg.max_latitude + " AND timestampdiff(SECOND," + expirationType + ",NOW())<7200 ORDER BY "+expirationType
    MySQLlongitude = cursor.execute(sql)
    longitude= cursor.fetchall()
    self.longitude= str(longitude)

    #####Nur Lockmodul Bereich
    if typ == "lockmodul":
      MySQLtyp = cursor.execute("SELECT active_fort_modifier FROM pokestop where longitude BETWEEN " + cfg.min_longitude + " AND " + cfg.max_longitude + " AND latitude BETWEEN " + cfg.min_latitude + " AND " + cfg.max_latitude + " AND timestampdiff(SECOND,lure_expiration,NOW())<7200 ORDER BY lure_expiration")
      typ= cursor.fetchall()
      self.typ= str(typ)

      MySQLtime = cursor.execute("SELECT lure_expiration FROM pokestop where longitude BETWEEN " + cfg.min_longitude + " AND " + cfg.max_longitude + " AND latitude BETWEEN " + cfg.min_latitude + " AND " + cfg.max_latitude + " AND timestampdiff(SECOND,lure_expiration,NOW())<7200 ORDER BY lure_expiration")
      Mytime= cursor.fetchall()
      self.zeit= str(Mytime)
      
    #####Nur Rocketstop Bereich
    if typ == "rocket":
      MySQLtyp = cursor.execute("SELECT incident_grunt_type FROM pokestop where longitude BETWEEN " + cfg.min_longitude + " AND " + cfg.max_longitude + " AND latitude BETWEEN " + cfg.min_latitude + " AND " + cfg.max_latitude + " AND timestampdiff(SECOND,incident_expiration,NOW())<7200 ORDER BY incident_expiration")
      typ= cursor.fetchall()
      self.typ= str(typ)

      MySQLtime = cursor.execute("SELECT incident_expiration FROM pokestop where longitude BETWEEN " + cfg.min_longitude + " AND " + cfg.max_longitude + " AND latitude BETWEEN " + cfg.min_latitude + " AND " + cfg.max_latitude + " AND timestampdiff(SECOND,incident_expiration,NOW())<7200 ORDER BY incident_expiration")
      Mytime= cursor.fetchall()
      self.zeit= str(Mytime)    
    #Verbindungsabbau zur MySQL-Datenbank
    #cursor = cursor.close()
    connection.close()
