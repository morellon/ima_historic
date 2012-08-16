#!/usr/bin/env python
# -*- coding: utf-8 -*
from google.appengine.ext import db
from ima import HistoricData
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging

class MainPage(webapp.RequestHandler):
    def get(self):
        pass

class CronPage(webapp.RequestHandler):
    def get(self):
        trackings = db.HistoricData("SELECT * FROM HistoricData")
        pass

application = webapp.WSGIApplication(
    [
        ('/', MainPage),
        ('/tasks/update', CronPage)
    ],
    debug=True
)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
