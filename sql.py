import MySQLdb
import time

class Sql():
  name = []
  incident_expiration = []
  incident_grunt_type = []
  longitude = []
  latitude = []

  def startSQL(self,cfg):
    #Verbindungsaufbau zur MySQL-Datenbank
    try:
      connection = MySQLdb.connect(host=cfg.host,db=cfg.database,user=cfg.user, passwd=cfg.password)
      cursor = connection.cursor()
    except:
      print("Kein Verbindungsaufbau zur Datenbank, probiere es in 15 Sekunden erneut\n")
      time.sleep(15)
      return self.startSQL(cfg)
    self.name.clear()
    self.incident_grunt_type.clear()
    self.incident_expiration.clear()
    self.longitude.clear()
    self.latitude.clear()

    Mysqlall = cursor.execute("SELECT name,latitude,longitude,incident_grunt_type,incident_expiration FROM pokestop where longitude BETWEEN " + cfg.min_longitude + " AND " + cfg.max_longitude + " AND latitude BETWEEN " + cfg.min_latitude + " AND " + cfg.max_latitude + " AND timestampdiff(SECOND,incident_expiration,NOW())<3600 ORDER BY incident_expiration,name")
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
