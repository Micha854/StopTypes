import MySQLdb
import time

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

  def rocketSQL(self,cfg,abfrage):
    #Verbindungsaufbau zur MySQL-Datenbank
    try:
      connection = MySQLdb.connect(host=cfg.host,db=cfg.database,user=cfg.user, passwd=cfg.password)
      cursor = connection.cursor()
    except:
      print("Kein Verbindungsaufbau zur Datenbank, probiere es in 15 Sekunden erneut\n")
      time.sleep(15)
      #return self.startSQL(cfg)
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
      #return self.startSQL(cfg)
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
