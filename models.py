#!/usr/bin/env python
# -*- coding: utf-8 -*
from google.appengine.ext import db
import datetime, time, json

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(time.mktime(obj.timetuple()))
        else:
            return json.JSONEncoder.default(self, obj)


class BASE(db.Model):
    def to_json(self):
        return JSONEncoder().encode(self.to_dict())

    def to_dict(self):
        return db.to_dict(self)


class FinancialAsset(BASE):
    name = db.StringProperty(multiline=False)
    code = db.StringProperty(multiline=False)


class HistoricDatum(BASE):
    financial_asset = db.ReferenceProperty(FinancialAsset,
                                           collection_name='historic_data')
    date = db.DateTimeProperty(auto_now_add=False)
    value = db.FloatProperty()

    def to_dict(self):
        return {
            'date': self.date,
            'value': self.value
        }
