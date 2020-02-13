import config
import createMessage
import sql
import sendMessage
import sys
import time
import clear

cfg = config.Config()
filename = ""
try:
  cfg.readConfig(sys.argv[1])
  filename = sys.argv[1]
  filename = filename[:len(filename)-4]
except:
  cfg.readConfig("rocket-config.ini")
  filename = "rocket"

clear = clear.Clear()
clear.clear(cfg.token,cfg.chatId,filename)
send = sendMessage.sendMessage()
send.setConfig(cfg.token,cfg.chatId,filename)

while 1 == 1:
  Sql = sql.Sql()
  Sql.startSQL(cfg)
  send.clearOutputList(Sql.name)
  create = createMessage.createMessage()
  create.create(send,Sql,cfg.verlinkung)
  time.sleep(60)