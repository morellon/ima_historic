import httplib, urllib, datetime
from datetime import date, timedelta

def get_indexes(date=date.today()):
    day = timedelta(days=1)
    date = date - 1*day
    strdate = date.strftime("%d%m%Y")
    params = urllib.urlencode({'saida': 'csv', 'Idioma': 'PT', 'Dt_ref': strdate})
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }
    conn = httplib.HTTPConnection("www.anbima.com.br")
    conn.request("POST", "/ima/IMA-geral-down.asp", params, headers)
    response = conn.getresponse()
    body = response.read()
    conn.close()
    raw_indexes = body.splitlines()
    indexes = {}
    if len(raw_indexes) < 3:
        return indexes
    for idx in raw_indexes[2:]:
        idx_parts = idx.split(';')
        key = " ".join(idx_parts[0:2])
        indexes[key] = {
            "date":  datetime.datetime.fromordinal(date.toordinal()),
            "value": float(idx_parts[3].replace(".", "").replace(",", "."))
        }
    return indexes

print(get_indexes())
