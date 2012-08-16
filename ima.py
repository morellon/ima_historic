#!/usr/bin/env python
# -*- coding: utf-8 -*
from google.appengine.ext import db
import urllib
import logging
import re
import random
import atom
import atom.service
import gdata.service
import gdata.calendar
import gdata.calendar.service
import time
import yaml

FILE = open("config.yaml","r")
CONFIG = yaml.load(FILE)
FILE.close()

class FinancialAsset(db:Model):
    name = db.StringProperty(multiline=False)
    code = db.StringProperty(multiline=False)

class HistoricData(db.Model):
    date = db.DateTimeProperty(auto_now_add=False)
    value = db.FloatProperty()
