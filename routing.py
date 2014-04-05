#!/usr/bin/python

#eine streckenlänge wird abgefragt

def wielangist(start, ziel):
  try:
    url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=" + start + "&destinations=" + ziel + "&language=de-DE&sensor=false"
  except:
    print("Ungültige Eingabe")
    return false
  try:
    nfd=urllib.urlopen(url)
    routingobj = json-load(nfd)
    nfd.close()
    distance=routingobj["rows"][0]["elements"][0]["distance"]["value"]
    return distance
  except ,e:
    print("Fehler beim Zugriff auf die GoogleApi"+e.message)
    return false

"ndf = network file descriptor"
