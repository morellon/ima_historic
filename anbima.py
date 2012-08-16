import httplib, urllib

def get_indexes(date):
    strdate = date.strftime("%d%m%Y")
    strdate = "15082012"
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
    raw_indexes = body.splitlines()[2:]
    indexes = {}
    for idx in raw_indexes:
        idx_parts = idx.split(';')
        key = " ".join(idx_parts[0:2])
        indexes[key] = {
            "date":  date,
            "value": float(idx_parts[3].replace(".", "").replace(",", "."))
        }
    return indexes
