import MySQLdb
import time
import json
import re

class Sql():
  name = []
  incident_expiration = []
  incident_grunt_type = []
  longitude = []
  latitude = []
  Lname = []
  Lincident_expiration = []
  Lincident_grunt_type = []
  Llongitude = []
  Llatitude = []

  def myGeo(self,cfg):
    try:
      connection = MySQLdb.connect(host=cfg.host,db=cfg.database,user=cfg.user, passwd=cfg.password)
      cursor = connection.cursor()
    except:
      print("Kein Verbindungsaufbau zur Datenbank, probiere es in 15 Sekunden erneut\n")
      time.sleep(15)
      return self.myGeo(cfg)
    cursor.execute("SELECT fence_data FROM `settings_geofence`")
    result = cursor.fetchall()

    x = str(result).replace("[('[", "").replace("]',)]", "").replace('"[', "").replace(']\',)', "").replace(']"', "").replace("('[", "").split(""", """)
    x = tuple(x)	
    geofence_dict=dict([])
    geofence_cords = "000000"
    dictkey = 'temp'
    first_cord = "000000"

    for item in x[0:len(x)-1]:
        element = item.replace(",", " ").replace('"', "")
        if re.search('[a-zA-Z]', element):
            geofence_cords += first_cord
            geofence_dict[dictkey] = geofence_cords
            dictkey = element
            geofence_cords = ""
            first_cord = ""
        else:
            if first_cord == "":
                first_cord = element
            element += ', '
            geofence_cords += element
    geofence_cords += first_cord
    geofence_dict[dictkey] = geofence_cords

    cursor = cursor.close()
    connection.close()
    del geofence_dict['temp']
    return geofence_dict

  def rocketSQL(self,cfg,abfrage):
    #Verbindungsaufbau zur MySQL-Datenbank
    try:
      connection = MySQLdb.connect(host=cfg.host,db=cfg.database,user=cfg.user, passwd=cfg.password)
      cursor = connection.cursor()
    except:
      print("Kein Verbindungsaufbau zur Datenbank, probiere es in 15 Sekunden erneut\n")
      time.sleep(15)
      return self.rocketSQL(cfg,abfrage)
    self.name.clear()
    self.incident_grunt_type.clear()
    self.incident_expiration.clear()
    self.longitude.clear()
    self.latitude.clear()

    cursor.execute(abfrage)
    all = cursor.fetchall()

    i = 0
    while i < len(all):
      self.name.append(all[i][0])
      self.latitude.append(all[i][1])
      self.longitude.append(all[i][2])
      self.incident_grunt_type.append(all[i][3])
      self.incident_expiration.append(all[i][4])
      i +=1

    cursor = cursor.close()
    connection.close()

  def lockmodulSQL(self,cfg,abfrage):
    #Verbindungsaufbau zur MySQL-Datenbank
    try:
      connection = MySQLdb.connect(host=cfg.host,db=cfg.database,user=cfg.user, passwd=cfg.password)
      cursor = connection.cursor()
    except:
      print("Kein Verbindungsaufbau zur Datenbank, probiere es in 15 Sekunden erneut\n")
      time.sleep(15)
      return self.lockmodulSQL(cfg,abfrage)
    self.Lname.clear()
    self.Lincident_grunt_type.clear()
    self.Lincident_expiration.clear()
    self.Llongitude.clear()
    self.Llatitude.clear()

    cursor.execute(abfrage)
    all = cursor.fetchall()

    i = 0
    while i < len(all):
      self.Lname.append(all[i][0])
      self.Llatitude.append(all[i][1])
      self.Llongitude.append(all[i][2])
      self.Lincident_grunt_type.append(all[i][3])
      self.Lincident_expiration.append(all[i][4])
      i +=1

    cursor = cursor.close()
    connection.close()
