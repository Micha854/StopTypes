#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import module

####Lade das Configfile
cfg = config.Config()
cfg.readConfig()

modul = module.Module()

if cfg.rocketStops=="true" and cfg.lureModule=="true":
  print("Rocketstops und Lockmodule ausgew\U000000e4hlt")
  modul.full(cfg)
elif cfg.rocketStops =="false" and cfg.lureModule=="true":
  print("Nur Lockmodule ausgew\U000000e4hlt")
  modul.LockModulOnly(cfg)
elif cfg.rocketStops =="true" and cfg.lureModule=="false":
  print("Nur Rocketstops ausgew\U000000e4hlt")
  modul.rocketStopsOnly(cfg)
else:
	print("Es wurde nichts aktiviert. Pr\U000000fcfe im Configfile das die Attribute 'rocketStops' oder 'lureModule' auf 'true' gesetzt sind")