#!/usr/bin/python

#benutze die Funktion report(string) statt print für user-info anweisungen
#und debug(string) für debugging-infos
#so lässt sich später die ausgabe besser umlenken

import urllib2
import json

def report(string):
  try:
    print(string)
  except:
    pass ##wuuups

def debug(string):
  try:
    print(string)
  except:
    pass ##wuuups

#für den fall, dass die bekannten strecken noch nicht geladen wurden
def ladestrecken(dateiname="strecken.json"):
  try:	#falls die Datei noch nicht vorhanden ist
   	streckendateiobj = open(dateiname,"r")
  except IOError,e:
    report("Fehler beim laden der Datei",e.message())
    return False
  else:
    streckenobj = json.load(streckendateiobj)
    streckendateiobj.close()
    return streckenobj
  finally:
    pass


#hier kommen entfernungsabfragen an
def wielangist(start,ziel):
  if 'strecken' in locals():   #wenn es die matrix schon gibt
    try:                       #erstmal prüfen ob wir die strecke schon kennen
      distanz = strecken[start][ziel]
    except KeyError:            #Ok, die bestimmte Strecke gibts ncoh nciht, also erfragen wir sie und schreiben sie gleich in die matrix
      distanz=wielangistunbekannnt(start,ziel)
      if distanz:
        strecken[start][ziel]=distanz
      else:
        debug("Fehler beim abfragen der GoogleApi. Aber das solltest du ja schon wissen")
    finally:
      return distanz
  else:
    if ladestrecken():   #hier sollte noch was rein um bei einem gesetztem Dateinamen auch wirklcih diesen zu laden
      wielangist(start,ziel)    #inception sollte man ncoh vermeiden
    else:
      report("Faataaaaaal")
      return False
 
""" 
strecken = {"praxis":{"hirschhalde":10,
                      "praxis":0,
                      "zuhause":30},
            "hirschhalde":{"hirschhalde":0,
                           "praxis":10,
                           "zuhause":35},
            "zuhause":{"hirschhalde":35,
                       "praxis":30,
                       "zuhause":0}
            }
            
"""

  




#eine unbekannte streckenlänge wird abgefragt
def wielangistunbekannt(start, ziel):
  try:
    url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=" + start + "&destinations=" + ziel + "&language=de-DE&sensor=false"
  except:
    print("Ungültige Eingabe")
    return False
  try:
    nfd=urllib2.urlopen(url)
    routingobj = json.load(nfd)
    nfd.close()
    try:
      distanz=routingobj["rows"][0]["elements"][0]["distance"]["value"]
      GARstart=routingobj["origin_addresses"][0] #GoogleApiRückgabe
      GARziel=routingobj["destination_addresses"][0]
    except:
      print("Fehlerhaftes Rückgabeobjekt")
      return False
   #yey, es hat geklappt 
    return {0:distanz,1:GARstart,2:GARziel,"distanz":distanz,"ziel":GARziel,"start":GARstart}
  except urllib2.URLError,e:
    print("Fehler beim Zugriff auf die GoogleApi"+e.message)
    return False

"network file descriptor"
distanz = wielangistneuestrecke("Furtwangen","Villingen")
print(distanz[0])
print(distanz[1])
print(distanz[2])