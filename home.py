#!/usr/bin/env python
# -*- coding: utf-8 -*
from google.appengine.ext import db
from models import HistoricData
from datetime import date, timedelta
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging
import anbima

class MainPage(webapp.RequestHandler):
    def get(self):
        pass

class CronPage(webapp.RequestHandler):
    def get(self):
        day = timedelta(days=1)
        today = date.today()
        for i in range(6):
            historic_data = anbima.get_indexes(today - i*day)
            if "IMA-B TOTAL" in historic_data:
                data = HistoricData()
                data.date = historic_data["IMA-B TOTAL"]["date"]
                data.value = historic_data["IMA-B TOTAL"]["value"]
                data.put()
        pass

application = webapp.WSGIApplication(
    [
        ('/ima-b', MainPage),
        ('/tasks/update', CronPage)
    ],
    debug=True
)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
