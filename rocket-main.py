import config
import createMessage
import sql
import sendMessage
import sys
import time
import clear
import os

from datetime import datetime
timestamp = time.time()
time_now = datetime.fromtimestamp(timestamp)
time_utc = datetime.utcfromtimestamp(timestamp)
utc_offset_secs = (time_now - time_utc).total_seconds()

# Flag variable to hold if the current time is behind UTC.
is_behind_utc = False

# If the current time is behind UTC convert the offset
# seconds to a positive value and set the flag variable.
if utc_offset_secs < 0:
    is_behind_utc = True
    utc_offset_secs *= -1

# Build a UTC offset string suitable for use in a timestamp.

if is_behind_utc:
    pos_neg_prefix = "-"
else:
    pos_neg_prefix = "+"

utc_offset = time.gmtime(utc_offset_secs)
utc_offset_fmt = time.strftime("%H", utc_offset)
gmt = int(pos_neg_prefix + utc_offset_fmt)

cfg = config.Config()
try:
  cfg.readConfig(sys.argv[1])
except:
  cfg.readConfig("config.ini")

if not os.path.exists(cfg.areaName+cfg.areaNumber):
    os.mkdir(cfg.areaName+cfg.areaNumber)
    print("Temp Directory " , cfg.areaName+cfg.areaNumber ,  " Created ")
else:    
    print("Temp Directory " , cfg.areaName+cfg.areaNumber ,  " already exists")
    
Sql = sql.Sql()
result = Sql.myGeo(cfg)

#if not os.path.isfile(cfg.areaName+cfg.areaNumber+"/geofence.txt"):
fence_file = open(cfg.areaName+cfg.areaNumber+"/geofence.txt", "w")
write_cords = fence_file.write(result[cfg.areaName])
fence_file.close()

fence_file = open(cfg.areaName+cfg.areaNumber+"/geofence.txt", "r")
geofence = fence_file.read()
fence_file.close()

clear = clear.Clear()
clear.clear(cfg.token,cfg.chatId,cfg.singlechatId,cfg)
send = sendMessage.sendMessage()
send.setConfig(cfg.token,cfg.singlechatId,cfg.chatId,cfg.areaName,cfg.areaNumber)

sys.stdout.write("\x1b]2;%s\x07" % cfg.areaName+cfg.areaNumber)

newMessageAfter = float(cfg.newMessageAfter) * 60
sleep_time = int(cfg.sleep_time)
timer = 0

while 1 == 1:
  if timer > newMessageAfter:
    timer = 0
  else:
    timer +=sleep_time
    
  Sql.lockmodulSQL(cfg,"SELECT name,latitude,longitude,active_fort_modifier,lure_expiration FROM pokestop where lure_expiration > utc_timestamp() AND ST_CONTAINS(st_geomfromtext('POLYGON(( " + geofence + " ))') , point(pokestop.latitude,pokestop.longitude)) ORDER BY lure_expiration,active_fort_modifier,name")
  Sql.rocketSQL(cfg,"SELECT name,latitude,longitude,incident_grunt_type,incident_expiration FROM pokestop where incident_expiration > utc_timestamp() AND ST_CONTAINS(st_geomfromtext('POLYGON(( " + geofence + " ))') , point(pokestop.latitude,pokestop.longitude)) ORDER BY incident_expiration,incident_grunt_type,name")
  send.clearOutputList(Sql.name,Sql.Lname)
  create = createMessage.createMessage()
  create.create(send,Sql,cfg,timer,newMessageAfter,gmt)
  time.sleep(sleep_time)
  #send.send(create.message)