#!/usr/bin/env python
# -*- coding: utf-8 -*
from google.appengine.ext import db
from models import HistoricData
from datetime import date
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging
import anbima

class MainPage(webapp.RequestHandler):
    def get(self):
        pass

class CronPage(webapp.RequestHandler):
    def get(self):
        current_date = date.today()
        historic_data = anbima.get_indexes(current_date)
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
