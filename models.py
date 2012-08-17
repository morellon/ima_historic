#!/usr/bin/env python
# -*- coding: utf-8 -*
from google.appengine.ext import db

class FinancialAsset(db.Model):
    name = db.StringProperty(multiline=False)
    code = db.StringProperty(multiline=False)

class HistoricData(db.Model):
    date = db.DateTimeProperty(auto_now_add=False)
    value = db.FloatProperty()
