#!/usr/bin/env python
# -*- coding: utf-8 -*-

class stopType():
  feuer = 0
  kanto = 0
  relaxo = 0
  kaefer = 0
  drache = 0
  kampf = 0
  flug = 0
  pflanze = 0
  boden = 0
  normal = 0
  gift = 0
  psycho = 0
  gestein = 0
  wasser = 0
  karpador = 0
  eis = 0
  elektro = 0
  stahl = 0
  geist = 0
  unlicht = 0
  fee = 0
  cliff = 0
  arlo = 0
  sierra = 0
  giovanni = 0
#  boss = 0

  Efeuer = ""
  Ekanto = ""
  Erelaxo = ""
  Ekaefer = ""
  Edrache = ""
  Ekampf = ""
  Eflug = ""
  Epflanze = ""
  Eboden = ""
  Enormal = ""
  Egift = ""
  Epsycho = ""
  Egestein = ""
  Ewasser = ""
  Ekarpador = ""
  Eeis = ""
  Eelektro = ""
  Estahl = ""
  Egeist = ""
  Eunlicht = ""
  Efee = ""
  Ecliff = ""
  Earlo = ""
  Esierra = ""
  Egiovanni = ""
#  Eboss = ""

  Sfeuer = ""
  Skanto = ""
  Srelaxo = ""
  Skaefer = ""
  Sdrache = ""
  Skampf = ""
  Sflug = ""
  Spflanze = ""
  Sboden = ""
  Snormal = ""
  Sgift = ""
  Spsycho = ""
  Sgestein = ""
  Swasser = ""
  Skarpador = ""
  Seis = ""
  Selektro = ""
  Sstahl = ""
  Sgeist = ""
  Sunlicht = ""
  Sfee = ""
  Scliff = ""
  Sarlo = ""
  Ssierra = ""
  Sgiovanni = ""
#  Sboss = ""

  Tfeuer = ""
  Tkanto = ""
  Trelaxo = ""
  Tkaefer = ""
  Tdrache = ""
  Tkampf = ""
  Tflug = ""
  Tpflanze = ""
  Tboden = ""
  Tnormal = ""
  Tgift = ""
  Tpsycho = ""
  Tgestein = ""
  Twasser = ""
  Tkarpador = ""
  Teis = ""
  Telektro = ""
  Tstahl = ""
  Tgeist = ""
  Tunlicht = ""
  Tfee = ""
  Tcliff = ""
  Tarlo = ""
  Tsierra = ""
  Tgiovanni = ""
#  Tboss = ""

  standard = 0
  gletscher = 0
  moos = 0
  magnet = 0

  Estandard = ""
  Egletscher = ""
  Emoos = ""
  Emagnet = ""

  Sstandard = ""
  Sgletscher = ""
  Smoos = ""
  Smagnet = ""

  Tstandard = ""
  Tgletscher = ""
  Tmoos = ""
  Tmagnet = ""

#  Emoji = ""
#  Infotext = ""

    ####Rocketstops
  def typ4(self):
    self.kanto +=1
    self.Ekanto ="\U0001f3c1"
    self.Skanto = self.Ekanto + " " + str(self.kanto) + " "
    self.Tkanto = "Kanto Starter"
    self.Emoji = self.Ekanto
    self.Infotext = self.Tkanto
    return self.Emoji + self.Infotext
  def typ5(self):
    self.relaxo +=1
    self.Erelaxo = "\U0001f6cc"
    self.Srelaxo = self.Erelaxo + " " + str(self.relaxo) + " "
    self.Trelaxo = "Relaxo"
    self.Emoji = self.Erelaxo
    self.Infotext = self.Trelaxo
    return self.Emoji + self.Infotext
  def typ7(self):
    self.kaefer +=1
    self.Ekaefer = "\U0001F41E"
    self.Skaefer = self.Ekaefer + " " + str(self.kaefer) + " "
    self.Tkaefer = "... Los mein Super K\U000000e4fer"
    self.Emoji = self.Ekaefer
    self.Infotext = self.Tkaefer
    return self.Emoji + self.Infotext
  def typ10(self):
    self.unlicht +=1
    self.Eunlicht = "\U0001f311"
    self.Sunlicht = self.Eunlicht + " " + str(self.unlicht) + " "
    self.Tunlicht = "... Wo Licht ist, da ist auch Schatten"
    self.Emoji = self.Eunlicht
    self.Infotext = self.Tunlicht
    return self.Emoji + self.Infotext
  def typ12(self):
    self.drache +=1
    self.Edrache = "\U0001f432"
    self.Sdrache = self.Edrache + " " + str(self.drache) + " "
    self.Tdrache = "... Gut gebr\U000000fcllt ist halb gewonnen"
    self.Emoji = self.Edrache
    self.Infotext = self.Tdrache
    return self.Emoji + self.Infotext
  def typ16(self):
    self.kampf +=1
    self.Ekampf = "\U0001f94a"
    self.Skampf = self.Ekampf + " " + str(self.kampf) + " "
    self.Tkampf = "... dient nur der Show"
    self.Emoji = self.Ekampf
    self.Infotext = self.Tkampf
    return self.Emoji + self.Infotext
  def typ18(self):
    self.feuer +=1
    self.Efeuer = "\U0001f525"
    self.Sfeuer = self.Efeuer + " " + str(self.feuer) + " "
    self.Tfeuer = "... Feueratem eines Pokemon"
    self.Emoji = self.Efeuer
    self.Infotext = self.Tfeuer
    return self.Emoji + self.Infotext
  def typ20(self):
    self.flug +=1
    self.Eflug = "\U0001f426"
    self.Sflug = self.Eflug + " " + str(self.flug) + " "
    self.Tflug = "... Mein Vogel Pokemon will"
    self.Emoji = self.Eflug
    self.Infotext = self.Tflug
    return self.Emoji + self.Infotext
  def typ23(self):
    self.pflanze +=1
    self.Epflanze = "\U0001f33f"
    self.Spflanze = self.Epflanze + " " + str(self.pflanze) + " "
    self.Tpflanze = "... nicht gut Beeren essen"
    self.Emoji = self.Epflanze
    self.Infotext = self.Tpflanze
    return self.Emoji + self.Infotext
  def typ25(self):
    self.boden +=1
    self.Eboden = "\U0001f5fb"
    self.Sboden = self.Eboden + " " + str(self.boden) + " "
    self.Tboden = "... in den Boden stampfen"
    self.Emoji = self.Eboden
    self.Infotext = self.Tboden
    return self.Emoji + self.Infotext
  def typ26(self):
    self.eis +=1
    self.Eeis = "\U00002744"
    self.Seis = self.Eeis + " " + str(self.eis) + " "
    self.Teis = "... Du bewegst dich auf d\U000000fcnnen Eis"
    self.Emoji = self.Eeis
    self.Infotext = self.Teis
    return self.Emoji + self.Infotext
  def typ31(self):
    self.normal +=1
    self.Enormal = "\U0001f518"
    self.Snormal = self.Enormal + " " + str(self.normal) + " "
    self.Tnormal = "... noch lange nicht schwach"
    self.Emoji = self.Enormal
    self.Infotext = self.Tnormal
    return self.Emoji + self.Infotext
  def typ32(self):
    self.gift +=1
    self.Egift = "\U0001f40d"
    self.Sgift = self.Egift + " " + str(self.gift) + " "
    self.Tgift = "... Gift drauf nehmen"
    self.Emoji = self.Egift
    self.Infotext = self.Tgift
    return self.Emoji + self.Infotext
  def typ35(self):
    self.psycho +=1
    self.Epsycho = "\U0001f52e"
    self.Spsycho = self.Epsycho + " " + str(self.psycho) + " "
    self.Tpsycho = "... unsichtbaren Kr\U000000e4ften"
    self.Emoji = self.Epsycho
    self.Infotext = self.Tpsycho
    return self.Emoji + self.Infotext
  def typ37(self):
    self.gestein +=1
    self.Egestein = "\U0001f9f1"
    self.Sgestein = self.Egestein + " " + str(self.gestein) + " "
    self.Tgestein = "... Bringen wir den Stein ins Rollen"
    self.Emoji = self.Egestein
    self.Infotext = self.Tgestein
    return self.Emoji + self.Infotext
  def typ38(self):
    self.wasser +=1
    self.Ewasser = "\U0001f4a7"
    self.Swasser = self.Ewasser + " " + str(self.wasser) + " "
    self.Twasser = "... Gew\U000000e4sser sind tr\U000000fcgerisch"
    self.Emoji = self.Ewasser
    self.Infotext = self.Twasser
    return self.Emoji + self.Infotext
  def typ39(self):
    self.karpador +=1
    self.Ekarpador = "\U0001f420"
    self.Skarpador = self.Ekarpador + " " + str(self.karpador) + " "
    self.Tkarpador = "Karpador"
    self.Emoji = self.Ekarpador
    self.Infotext = self.Tkarpador
    return self.Emoji + self.Infotext
  def typ48(self):
    self.geist +=1
    self.Egeist  = "\U0001f47b"
    self.Sgeist  = self.Egeist + " " + str(self.geist) + " "
    self.Tgeist = "... Buhu ... Buhuhu"
    self.Emoji = self.Egeist
    self.Infotext = self.Tgeist
    return self.Emoji + self.Infotext
  def typ49(self):
    self.elektro +=1
    self.Eelektro = "\U000026a1"
    self.Selektro = self.Eelektro + " " + str(self.elektro) + " "
    self.Telektro = "... Du wirst schockiert sein"
    self.Emoji = self.Eelektro
    self.Infotext = self.Telektro
    return self.Emoji + self.Infotext
  def typ97(self):
    self.fee +=1
    self.Efee  = "\U0001f311"
    self.Sfee  = self.Efee + " "+ str(self.fee) + " "
    self.Tfee = "... Wie niedlich mein Pokemon ist"
    self.Emoji = self.Efee
    self.Infotext = self.Tfee
    return self.Emoji + self.Infotext
  def typ98(self):
    self.stahl +=1
    self.Estahl  = "\U0001f311"
    self.Sstahl  = self.Estahl + " " + str(self.stahl) + " "
    self.Tstahl =  "... Gegen meinen eisernen Willen"
    self.Emoji = self.Estahl
    self.Infotext = self.Tstahl
    return self.Emoji + self.Infotext

  ####Bosse
  def typ41(self):
    self.cliff +=1
    self.Ecliff = "\U0001F9B9"
    self.Scliff = self.Ecliff + " " + str(self.cliff) + " "
    self.Tcliff = "Team Leader Cliff"
    self.Emoji = self.Ecliff
    self.Infotext = self.Tcliff
    return self.Emoji + self.Infotext
  def typ42(self):
    self.arlo +=1
    self.Earlo = "\U0001F9B8"
    self.Sarlo = self.Earlo + " " + str(self.arlo) + " "
    self.Tarlo = "Team Leader Arlo"
    self.Emoji = self.Earlo
    self.Infotext = self.Tarlo
    return self.Emoji + self.Infotext
  def typ43(self):
    self.sierra +=1
    self.Esierra = "\U0001F45A"
    self.Ssierra = self.Esierra + " " + str(self.sierra) + " "
    self.Tsierra = "Team Leader Sierra"
    self.Emoji = self.Esierra
    self.Infotext = self.Tsierra
    return self.Emoji + self.Infotext
  def typ44(self):
    self.giovanni +=1
    self.Egiovanni = "\U0001f454"
    self.Sgiovanni = self.Egiovanni + " " + str(self.giovanni) + " "
    self.Tgiovanni = "Rocket Boss Giovanni"
    self.Emoji = self.Egiovanni
    self.Infotext = self.Tgiovanni
    return self.Emoji + self.Infotext

  ####Lockmodule
  def typ501(self):
    self.standard +=1
    self.Estandard = "\U0001F39F"
    self.Sstandard = self.Estandard + " " + str(self.standard) + " "
    self.Tstandard = "Normales Lockmodul"
    self.Emoji = self.Estandard
    self.Infotext = self.Tstandard
    return self.Emoji + self.Infotext
  def typ502(self):
    self.gletscher +=1
    self.Egletscher = "\U00002744"
    self.Sgletscher = self.Egletscher + " " + str(self.gletscher) + " "
    self.Tgletscher = "Gletscher Lockmodul"
    self.Emoji = self.Egletscher
    self.Infotext = self.Tgletscher
    return self.Emoji + self.Infotext
  def typ503(self):
    self.moos +=1
    self.Emoos = "\U0001f33f"
    self.Smoos = self.Emoos + " " + str(self.moos) + " "
    self.Tmoos = "Moos Lockmodul"
    self.Emoji = self.Emoos
    self.Infotext = self.Tmoos
    return self.Emoji + self.Infotext
  def typ504(self):
    self.magnet +=1
    self.Emagnet = "\U0001F9F2"
    self.Smagnet = self.Emagnet + " " + str(self.magnet) + " "
    self.Tmagnet = "Magnet Lockmodul"
    self.Emoji = self.Emagnet
    self.Infotext = self.Tmagnet
    return self.Emoji + self.Infotext

  def getType(self,value):
    switch = {
      None: self.undefine,
      4: self.typ4,
      5: self.typ5,
      7: self.typ7,
      10:self.typ10,
      12:self.typ12,
      16:self.typ16,
      18:self.typ18,
      20:self.typ20,
      23:self.typ23,
      25:self.typ25,
      26:self.typ26,
      31:self.typ31,
      32:self.typ32,
      35:self.typ35,
      37:self.typ37,
      38:self.typ38,
      39:self.typ39,
      48:self.typ48,
      49:self.typ49,
      97:self.typ97,
      98:self.typ98,
      41:self.typ41,
      42:self.typ42,
      43:self.typ43,
      44:self.typ44,
      501:self.typ501,
      502:self.typ502,
      503:self.typ503,
      504:self.typ504
    }
    typ = switch.get(value,lambda: str(value))
    return typ()