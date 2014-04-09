#!/usr/bin/python
#initialisieren

#hier wird die aktuelle tagesposition gespeichert
swoche={"mon":{"strecke":0,"pos":"zuhause"},
        "die":{"strecke":0,"pos":"zuhause"},
        "mit":{"strecke":0,"pos":"zuhause"},
        "don":{"strecke":0,"pos":"zuhause"},
        "fre":{"strecke":0,"pos":"zuhause"}
        }
montag = []
dienstag = []
mittwoch = []
donnerstag = []
freitag = []
woche = {"mon":montag,"die":dienstag,"mit":mittwoch,"don":donnerstag,"fre":freitag}
termin={"hirschhalde":{"name":"Altenheim Hirschhalde",
                       "code":"hirschhalde", #verwendet als start bzw ziel ort zur kilometer berechnung
                       "dauer":45,  #wie lange geht der termin
                       "ort":"Donaueschingen"  #wo ist es
                       },
        "zuhause":{"name":"Zuhause",
                       "code":"zuhause", #verwendet als start bzw ziel ort zur kilometer berechnung
                       "dauer":0,  #wie lange geht der termin
                       "ort":"Vöhrenbach"  #wo ist es
                       },
        "praxis":{"name":"Praxis",
                  "code":"praxis", #verwendet als start bzw ziel ort zur kilometer berechnung
                  "dauer":45,  #wie lange geht der termin
                  "ort":"Donaueschingen"  #wo ist es
                  }
        }
                       
#routing
#routingtabelle mit den entfernungen, jedes mit jedem vernetzt
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

# addtermin("mon","praxis")
def addtermin(tag,art,position = "end"):
  if position == "end":
    woche[tag].append(termin[art])


#strecke berechnen
def berechnestrecke(art="alle"):
  if art == "alle":
    for key in woche:
      while len(woche[key])>0:
        print(key)
        print(woche[key][0]["name"])
        swoche[key]["strecke"] += strecken[swoche[key]["pos"]][woche[key][0]["code"]]
        swoche[key]["pos"] = woche[key][0]["code"]
        del woche[key][0]
      swoche[key]["strecke"] += strecken[swoche[key]["pos"]]["zuhause"]
      swoche[key]["pos"] = "zuhause"

#testarea
addtermin("mit","hirschhalde")
addtermin("mit","hirschhalde")
addtermin("mit","praxis")

addtermin("die","praxis")
addtermin("die","hirschhalde")
addtermin("die","praxis")

addtermin("don","hirschhalde")
addtermin("don","hirschhalde")
addtermin("don","praxis")

addtermin("fre","praxis")
addtermin("fre","hirschhalde")
addtermin("fre","praxis")
berechnestrecke()

