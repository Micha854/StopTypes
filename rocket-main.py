import config
import createMessage
import sql
import sendMessage
import sys
import time
import clear

cfg = config.Config()
try:
  cfg.readConfig(sys.argv[1])
except:
  cfg.readConfig("rocket-config.ini")

clear = clear.Clear()
clear.clear(cfg.token,cfg.singlechatId,cfg)
send = sendMessage.sendMessage()
send.setConfig(cfg.token,cfg.singlechatId,cfg.chatId,cfg.areaName)

sys.stdout.write("\x1b]2;%s\x07" % cfg.areaName)

while 1 == 1:
  Sql = sql.Sql()
  Sql.lockmodulSQL(cfg,"SELECT name,latitude,longitude,active_fort_modifier,lure_expiration FROM pokestop where timestampdiff(SECOND,lure_expiration,NOW())<3600 AND ST_CONTAINS(st_geomfromtext('POLYGON(( " + cfg.fence + " ))') , point(pokestop.latitude,pokestop.longitude)) ORDER BY lure_expiration,name")
  Sql.rocketSQL(cfg,"SELECT name,latitude,longitude,incident_grunt_type,incident_expiration FROM pokestop where timestampdiff(SECOND,incident_expiration,NOW())<3600 AND ST_CONTAINS(st_geomfromtext('POLYGON(( " + cfg.fence + " ))') , point(pokestop.latitude,pokestop.longitude)) ORDER BY incident_expiration,name")
  send.clearOutputList(Sql.name,Sql.Lname)
  create = createMessage.createMessage()
  create.create(send,Sql,cfg)
  time.sleep(10)
  #send.send(create.message)