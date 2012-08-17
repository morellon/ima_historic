#!/usr/bin/env python
# -*- coding: utf-8 -*
from google.appengine.ext import db
from models import HistoricDatum, FinancialAsset, JSONEncoder
from datetime import date, timedelta
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging, urllib, time
import anbima

class HistoricDataPage(webapp.RequestHandler):
    def get(self, code):
        code = urllib.unquote_plus(code)
        asset = db.GqlQuery("SELECT * FROM FinancialAsset WHERE code = :code", code=code).get()
        logging.error("Asset: %s" % code)
        if not asset:
            data = []
        else:
            data = asset.historic_data.order("date")

        series = [[datum.date, datum.value] for datum in data]
        self.response.out.write(JSONEncoder().encode(series))

class CronPage(webapp.RequestHandler):
    def get(self):
        day = timedelta(days=1)
        today = date.today()
        for i in range(6):
            historic_data = anbima.get_indexes(today - i*day)
            code = "IMA-B TOTAL"
            if code in historic_data:
                asset = db.GqlQuery("SELECT * FROM FinancialAsset WHERE code = :code", code=code).get()
                if not asset:
                    asset = FinancialAsset()
                    asset.name = code
                    asset.code = code
                    asset.put()

                index_data = historic_data[code]
                data = db.GqlQuery("SELECT * FROM HistoricDatum WHERE date = :date", date=index_data["date"]).get()
                if not data:
                    data = HistoricDatum()
                    data.date = index_data["date"]
                    data.value = index_data["value"]
                    data.financial_asset = asset
                    data.put()
        pass

application = webapp.WSGIApplication(
    [
        (r'/assets/(.+)/data', HistoricDataPage),
        ('/tasks/update', CronPage)
    ],
    debug=True
)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
