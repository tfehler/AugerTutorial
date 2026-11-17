# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] id="juxsdVgb45cy"
# # **Python-Tutorial**

# %% [markdown] id="z6_bOKFN5KNn"
# ## 1. Grundbegriffe
#
# Bevor wir beginnen, gehen wir einige grundlegende Konzepte und Operationen durch, die in fast allen Codes vorkommen werden, die ihr erstellt.

# %% colab={"base_uri": "https://localhost:8080/"} id="q7v0zroN5KNr" outputId="3727e508-d688-4271-dce1-535c67bc33c7"
x = 3       #Wir definieren eine numerische Variable.
print(x)    #Die 'print()' Funktion gibt es auf dem Bildschirm aus.

y = 4
print(y + 5)

z = x + 2*y  #Auf der grundlegendsten Ebene funktioniert Python wie ein Taschenrechner.
print(z)

# %% [markdown] id="_nnRF-n7K81k"
# Versuchen Sie, die folgenden Berechnungen zu schreiben und auf dem Bildschirm anzuzeigen.
#
# *   2*3-1
# *   8/2*4
# *   3*2**4
# *   (3*2)**4
# *   3-2**4
# *   3**4-3
# *   2**3
# *   5e-3
#

# %%

# %% colab={"base_uri": "https://localhost:8080/", "height": 176} id="aGeggUoa5KNz" outputId="58421685-7477-4336-85d1-4df108b1a31f"
del z          # Die Funktion 'del' löscht die Variable.

print(z)       # Fehler! (z existiert nicht mehr, da wir es gelöscht haben)

# %% [markdown] id="_fTJJTvs5KN-"
# ## 2. Variablentypen
#
# 1. `type()` zeigt den Datentyp einer Variablen an.

# %% id="0bEZWlr35KOA"
print(type(4))     #int (ganze Zahl)
print(type(4.0))   #float (Gleitkommazahl, Zahl mit Komma, Dezimalzahl)
print(type(True))  #boolean (Boolesch, binär, wahr oder falsch, 0 oder 1)
print(type(None))  #NoneType (leere Variable, enthält nichts)
print(type('c'))   #str (Zeichenfolge)
print(type("Hallo"))#str (Zeichenfolge)
print(type([]))    #list (Liste, geordnete Menge von Elementen)
print(type(print)) #builtin_function_or_method (Funktion, Abfolge von Prozessen, Algorithmus)

# %% [markdown] id="YOUY4kjZ5KOF"
# ### Man kann Zahlen in Strings umwandeln und umgekehrt.

# %% id="ZBUFaw5O5KOG"
zahl = 2
string = str(zahl) #wandelt Zahl in String um
print(type(zahl))
print(type(string))

print(zahl+zahl+zahl) #Man kann Zahlen addieren
print(string+string+string) #Man kann Strings nicht addieren, sie werden stattdessen verknüpft

print('Das Ergebniss ist ' + str(zahl)) #Eine numerische Variable kann in einer Nachricht ausgegeben werden.

# %% id="8fZm_xGK5KOL"
print(int(string)+int(string)) # wandelt String in Zahl um

# %% id="7XyuTq9Z5KOO"
float_zahl = float("2.2") #Dasselbe gilt für Zahlen mit Komma.
float_zahl + float_zahl

# %% [markdown] id="KPccKkFk5KOS" jupyter={"outputs_hidden": true}
# ### Liste
#
# Eine Liste ist eine Variable, in der ich beliebige Arten von Variablen speichern kann – in der Reihenfolge, die ich möchte.

# %% id="KF8-9Vzn5KOS"
liste = [] #Ich erstelle eine leere Liste.
liste = list() #leere Liste; oder um einen anderen Datentyp in eine Liste umzuwandeln.
print(liste)

liste = [0] #Liste mit einem einzigen Element, der Zahl 0
print(liste)

#Jedes Element ist durch ein Komma getrennt.
liste = ['Pepe', 8] #Liste mit zwei Elementen, dem String 'Pepe' und der Zahl 8
print(liste)

# %% id="Q4VNJquxnRRt"
teilchen_liste=['Sauerstoff','Nitrogen','Eisen','Proton']
print(len(teilchen_liste)) #gibt die Anzahl der Elemente der Liste zurück

print(len([])) #Eine leere Liste hat 0 Elemente.

# %% [markdown] id="aDZTY7Sk5KOV"
# Weitere Möglichkeiten, Listen zu erstellen:

# %% id="DjnDJc8L5KOW"
element = 30
wiederholungen_anzahl = 5
wiederholte_liste = [element] * wiederholungen_anzahl #Erstelle eine Liste mit der Häufigkeit, mit der das ausgewählte Element gewählt wurde.
print(wiederholte_liste)

# %% [markdown] id="tZfS9T-d5KOa"
# **Operationen** mit Listen

# %% id="O5I6Mc6t5KOb"
liste_a = ["3"] * 2
liste_b = ["5"] * 4

liste_summe = liste_a + liste_b

# Die Addition verknüpft die Elemente der addierten Listen zu einer einzigen Liste.
print(liste_summe)

# %% id="HaoPHvOdpL4H"
teilchen_liste = ['Sauerstoff','Nitrogen','Eisen','Proton']
neues_element = 'Lithium'

#Mit der Funktion `listenname.append(elementname)` füge ich das Element am Ende der Liste hinzu.
print(teilchen_liste)
teilchen_liste.append(neues_element)
print(teilchen_liste)

# %% id="NP7F1OqaqQvQ"
#Mit `listenname[n]` greife ich auf das n-te Element der gewünschten Liste zu, wobei „n“ eine ganze Zahl ist.
print(teilchen_liste[0]) #Beachten Sie, dass das erste Element die Zahl 0 ist.
print(teilchen_liste[1]) #dann ist das Element [1] das zweite
print(teilchen_liste[len(teilchen_liste)-1]) #Wenn ich das letzte Element haben möchte, frage ich die Anzahl der Elemente minus 1 ab.
print(teilchen_liste[-1]) #Oder einfacher: nur mit -1

# %% [markdown] id="I5VhK8525KOe"
# Zugriff auf Elemente einer Liste: Die Nummerierung beginnt bei 0 und reicht bis length-1.

# %% id="PWGZhZHA5KOf"
satz = "Peter lernt, in Python zu programmieren."
liste_satz = satz.split(" ") #Teilt den String in die Elemente auf, die durch das angegebene Trennzeichen – in diesem Fall ein Leerzeichen – voneinander getrennt sind.
print(liste_satz)

# %% id="uaz8sKO0sY-L"
beginn = 1
ende = 3
print(liste_satz[beginn:ende]) # Ich kann alle Elemente in einem Intervall abrufen.
print(liste_satz[beginn:]) # oder von einem Platz an
print(liste_satz[:ende]) # oder vom ersten bis zu einem Platz

# %% id="kySc4EAl5KO0"
step = 3
print(liste_satz[0:7:step]) # Ich kann auch Elemente überspringen.
print(liste_satz[::step]) # Wenn ich nichts angebe, ist davon auszugehen, dass es vom Anfang bis zum Ende reicht.
print(liste_satz[-1:0:-1]) # Ich kann auch rückwärts gehen.

# %% id="q7HqFXad5KO_"
print(min([1, 4, 2.2])) # Das Minimum kann angezeigt werden.

# %% [markdown] id="f_fHB-oJTWXc"
# Führen Sie die folgenden Operationen aus (bitte in der angegebenen Reihenfolge; die Semikolons stehen für das Drücken der „Enter“-Taste in der Konsole oder einen Zeilenumbruch im Skript).
#
# 1. x = [3, 4, 7, 11];y = [1, 5, 6]
# 2. [x, y]
# 3. x + y
# 4. z = x+y
# 5. x[0]=0; w=1
# 6. w = [x,y]
# 7. x[0]=0;w
# 8. len(y)
# 9. print(y)
# 10. y*2
# 11. y.append(100);y
# 12. y[-1]
# 13. z[2:4]
# 14. z[:5]

# %% id="U8PspPxN18nB"

# %% [markdown] id="p02kQaQ65KPC"
# ### Dictionaries
#
# Anstatt wie bei Listen über einen Index zuzugreifen, erfolgt der Zugriff über ein Wort oder einen Schlüssel, der als „Key“ bezeichnet wird.

# %% id="DAhOvJin5KPD"
# Zwei Möglichkeiten, ein Dictionary zu erstellen
dict_teilchen = dict()
dict_teilchen = {}

# %% id="OPcMc7wbghPu"
# Ich kann jedem „Key“ (dem Teilchentyp) eine Variable (in diesem Fall die Anzahl der Teilchen) zuweisen.
dict_teilchen['Photon'] = 598
dict_teilchen['Elektron'] = 4546
dict_teilchen['Proton'] = 8787

print(dict_teilchen)

# %% id="pE2dk12J5KPG"
# So greife ich auf den Inhalt des Schlüssels „Helium“ zu.
dict_teilchen['Helium'] = 10

# %% id="b5iGyYNY5KPI"
# So kann ich die Werte und Keys sehen, die im Dictionary vorhanden sind.
print(dict_teilchen.values())
print(dict_teilchen.keys())
print(dict_teilchen.items())


# %% [markdown] id="8cxR2wlIVfg_"
# ## Vektoren
#
# Python bietet das Paket NumPy, mit dem wir Arrays erstellen können, die weitgehend unseren Erwartungen entsprechen. Um die Funktionen von NumPy einzubinden, verwenden wir (oder geben in der Konsole ein):
#
# `import numpy as np`
#
# Damit erhalten wir Zugriff auf alle Funktionen von NumPy, indem wir ihnen das Präfix „np.“ voranstellen. Dazu gehören häufig verwendete Funktionen wie cos, sin, sqrt (Quadratwurzel) und log (Logarithmus zur Basis e) sowie die Konstanten e und π. Probieren Sie die folgenden Befehle aus:
#
# 1. x = np.array([3, 4, 7, 11])
# 2. y = np.array([1, 5, 6, 8])
# 3. x + y
# 4. np.linspace(1,8,10)
# 5. np.arange(8,1,-1)
# 6. np.log(x)
# 7. np.cos(np.pi)
# 8. w=x;x[0]=100;print(w)
# 9. len(y)
# 10. A = np.array([[1,2,3,4],[5,6,7,8]]);A
# 11. A*x
# 12. np.dot(A,x)
# 13. np.dot(x,x)
# 14. np.transpose(A)

# %% id="zMA1-PPsVxDn"
import numpy as np

# %% id="WR_ecQinVz32"

# %% [markdown] id="E0gkokRMWLBe"
# Versuchen Sie, die folgenden Sequenzen mit den Funktionen zu erzeugen, die wir bisher kennengelernt haben.
# 1. Die geraden Zahlen von 0 bis 50
# 2. Die Sequenz [10, 9.5, 9, 8.5, ..., -8.5, -9, -9.5, -10]

# %% id="Rt7WmOaWWLgx"

# %% [markdown] id="ZUPGCerf5KN4"
# ## 3. Logische und bedingte Vergleiche
#
# Es können die üblichen Operatoren <, >, <=, >=, == (Gleichheit) und != (Ungleichheit) verwendet werden. Vergleiche liefern einen booleschen Wert zurück, der entweder True oder False sein kann.

# %% id="VNTRR9Ki5KN5"
print(2 == 2)   # '==' Gibt True oder False zurück, je nachdem, ob beide Seiten gleich sind oder nicht.
print(2 != 2)   # '!=' Gibt True oder False zurück, je nachdem, ob beide Seiten unterschiedlich sind oder nicht.


x = 3
y = 2
print(x < y) # '<=' Gibt True oder False zurück, je nachdem, ob x kleiner als y ist oder nicht.
print(x > y) # '<=' Gibt True oder False zurück, je nachdem, ob x kleiner als y ist oder nicht.
print(x <= y) # '<=' Gibt True oder False zurück, je nachdem, ob x kleiner oder gleich y ist oder nicht.
print(x >= y) # '<=' Gibt True oder False zurück, je nachdem, ob x kleiner oder gleich y ist oder nicht.

# %% [markdown] id="3X0jgI0e5KPm"
# ### **if** (wenn, Bedingung)
#
# Wenn ein Prozess nur dann ausgeführt werden soll, wenn eine bestimmte Bedingung erfüllt ist. Wenn (Bedingung wahr), dann (Prozess).

# %% id="qh0iiBPXrJEq"
x = 3
y = 2
if x > y:
  print('x ist größer als y')

# %% id="a4LZ8rWAzZDm"
x = 3
y = 2
if x > y:
  print('x ist größer als y') #Ich muss alles, was sich innerhalb des „if“ befindet, einrücken oder mit Abständen versehen.

# %% id="LXQWzXbr5KPr"
# Wenn die Bedingung falsch ist, werden die Prozesse innerhalb des 'if' niemals ausgeführt.
x = 1
y = 2
if x > y:
  print('x ist größer als y')
print('Das steht außerhalb des if, weil es nicht eingerückt ist.')

# %% [markdown] id="tKGpbEejtCPb"
# ### **else** (andernfalls)
#
# Wenn (Bedingung wahr), dann (Ablauf).
# Andernfalls (die Bedingung war falsch), dann (anderer Ablauf)

# %% id="Cv_7jngRs3C2"
x = 1
y = 2
if x > y:
  print('x ist größer als y')
else: # Wir können festlegen, dass – falls die Bedingung im „if“ falsch war – das ausgeführt wird, was wir in den „else“-Block schreiben.
  print('x ist NICHT größer als y')

# %% [markdown] id="dC0uZMdztpKF"
# ### **elif** (oder wenn)
#
# Wird verwendet, wenn wir in weitere Bedingungen unterteilen möchten:
# Wenn (Bedingung), dann (Ablauf).
# Wenn (weitere Bedingung), dann (Ablauf).

# %% id="GyasRAjVuDCU"
x = 2
y = 2
if x > y:
  print('x ist grösser als y')
elif x == y: # Die wahre Bedingung wird ausgeführt; wenn beide (die des „if“ und die des „elif“) falsch sind, wird das „else“ ausgeführt.
  print('x ist gleich y')
else:
  print('x ist kleiner als y')

# %% [markdown] id="3mM_AGBVquRi"
# ## 4. Schleifen (Loops)
#
# Sie sind das wichtigste Werkzeug in der Programmierung. Sie ermöglichen es, eine Reihe von Abläufen eine bestimmte Anzahl von Malen oder so lange zu wiederholen, bis eine bestimmte Bedingung erfüllt ist.

# %% [markdown] id="4xQdqIM0kLxd"
# ### **For**
# Es handelt sich um eine Schleife; sie wird verwendet, wenn eine Reihe von Vorgängen eine bestimmte Anzahl von Malen wiederholt werden soll.
#
# 1. _for_ Element *in* Liste:
# > Sie durchläuft jedes Element der Liste und führt für jedes davon die Aktionen aus, die eingerückt sind.
#

# %% id="lqTWrUOF5KPm"
# Ich gebe die ganzen Zahlen von 0 bis 9 aus.
ganze_zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 'neun']
for i in ganze_zahlen:
    print(i) # „i“ ist bei jedem Durchlauf das nächste Element der Liste „ganze_zahlen“.

# %% id="-CzJ0QQC5KPo"
# Die Funktion range(letzte_zahl) liefert direkt die Ganzzahlen von 0 bis letzte_zahl-1.
letzte_zahl = 10
for i in range(letzte_zahl):
    print(i, ganze_zahlen[i])

# %% id="T2xm0GVX5KPp"
# Wenn ich range(startwert, endwert) verwende, erhalte ich die Ganzzahlen von startwert bis endwert-1.
endwert=10
startwert=5

for i in range(startwert, endwert):
    print(i)

# %% id="axK50tYRoOSt"
# Wenn ich range(startwert, endwert, schrittweite) verwende, erhalte ich die Ganzzahlen von startwert bis endwert-1.
endwert=10
startwert=5
schritt=2
for i in range(startwert,endwert,schritt):
    print(i)

# %% id="VptZ4p8ZohSZ"
# Ich kann die Elemente einer Liste durchlaufen.
liste_teilchen=['Helium','Proton','Eisen','Sauerstoff','Nitrogen']
for teilchen in liste_teilchen:
    print(teilchen)

# %% id="Dn7LVqVlp_EB"
# oder aber die Indizes der Elemente
liste_teilchen=['Helium','Proton','Eisen','Sauerstoff','Nitrogen']
for i in range(len(liste_teilchen)):
    print(liste_teilchen[i])

# %% [markdown] id="vCx30KX5ZGB1"
# ### **while**
# Es handelt sich um eine Schleife – ähnlich wie bei **for** –, die verwendet wird, wenn eine Reihe von Abläufen wiederholt werden soll. Der Unterschied besteht darin, dass die Anzahl der Wiederholungen nicht fest vorgegeben ist; stattdessen wird der Vorgang so lange wiederholt, wie eine bestimmte Bedingung erfüllt ist.
#
# 1. _while_ (Bedingung):
# > Solange die Bedingung wahr ist, werden die eingerückten Aktionen ausgeführt; anschließend wird die **Bedingung** erneut überprüft.
#
# Solange (Bedingung wahr), führe Folgendes aus:
#

# %% id="ZMOEOMyp5KPu"
# Wir erstellen einen Zähler, bei dem wir i=0 definieren und bei jeder Wiederholung eins dazuaddieren.
i = 0
while i < 10: # Die 'while'-Schleife endet, wenn i=10 ist, und verlässt den Schleifenblock.
  print(i)
  i = i + 1

# %% [markdown] id="yMsPfVnnbBfO"
# ### **break**
# Abbrechen. Dient dazu, eine Schleife zu unterbrechen.
#
# 1. _while_ (Bedingung) oder _for_ Element _in_ Liste:
# > _if_ (Bedingung):
# > break
#
# Wenn (Bedingung wahr), dann brich die Schleife ab.

# %% id="PZ8K-97d5KPx"
# Wir erstellen eine Suchfunktion; wir möchten prüfen, ob ein bestimmtes Element zu einer Liste gehört.
liste_teilchen=['Helium','Proton','Eisen','Sauerstoff','Nitrogen']
teilchen = 'Eisen'

for i in range(len(liste_teilchen)):
    if teilchen == liste_teilchen[i]: # Wenn das Element gefunden wird ...
      print(teilchen + ' ist das Element ' + str(i) + ' der Liste')
      break # Verwende eine 'for'-Schleife, und die Variable 'i' entspricht der Position des Elements.

print(i)
print(liste_partikel[i])

# %% [markdown] id="xtTdLUuslmVB"
# Erstellt einen Code, der:
# 1. Die Zahlen findet, deren Quadratwurzeln ganze Zahlen und kleiner als 10 sind.
# 2. Die Primzahlen kleiner als 100 findet (Hinweis: Die Funktion `np.mod(x,y)` berechnet den Rest der Division von x durch y).

# %%

# %% [markdown] id="8qSjpzgl5KQG"
# ## 5. **try** und **except**
#
# try:
#
#     (Führt den folgenden Code aus, wenn kein Fehler auftritt)
#
# except:
#
#     (Wenn ein Fehler auftritt, wird die Ausnahmebehandlung ausgeführt)
#
# Zwei Befehle, die verhindern, dass das Programm bei einem Fehler abbricht – stattdessen erhalten wir eine Benachrichtigung. „Versuche“ (Befehlsfolge), „außer bei Fehler“ (Befehlsfolge).

# %% id="5FKlBUz95KQG"
for i in range(-2,3):
  try: # Führe das Folgende aus, wenn kein Fehler vorliegt.
      print(2/i)
  except: # Wenn ein Fehler auftritt, führe die Ausnahme aus.
      print("Du hast durch 0 geteilt!")


# %% [markdown] id="ggiwi2xt5KQA"
# # 6. Funktionen
# ---
# _def_ funktionsname(input_1,input_2,...):
#
#
# > (Abläufe der Funktion)
#
#
# > (verwenden die Inputs und berechnen einen Output)
#
#
# > _return_ output
#
# ---
#
# Wenn wir einen Codeabschnitt häufig benötigen, wird es mühsam, ihn immer wieder neu schreiben zu müssen. Zudem müssten wir bei einer Änderung jeden einzelnen dieser verstreuten Abschnitte anpassen. Um dies zu vermeiden, kapselt man den Code in einer Funktion, die sich bei Bedarf jederzeit aufrufen lässt.

# %% id="P_hek2SI5KQB"
# Definieren wir eine Funktion, die zwei Zahlen entgegennimmt und sie addiert.
def addition(input_1, input_2): # Diese Zeile definiert die Funktion, sie führt sie NICHT aus.
  output = input_1 + input_2
  #Die Eingabevariablen existieren nur innerhalb der Funktion und werden gelöscht, sobald diese endet.
  return output #Die einzige Variable, die überlebt, ist der Output.

input_1 = 5
input_2 = 3
output = addition(input_1, input_2) # Hier führe ich die Funktion aus.
print(output)

# %% id="NfYVuN7cQI95"
addition('100','2')


# %% [markdown] id="lKaEm1QB5KQA"
# Eine Funktion kann einen Input verändern, ohne einen Output zurückzugeben.

# %% id="RuB9rjjy5KQC"
def erste_und_letzte_tauschen(input_1):
  erste_element = input_1[0]
  letzte_element = input_1[-1]
  input_1[-1] = erste_element
  input_1[0] = letzte_element
  # Es ist eine Funktion ohne „return“; sie ändert lediglich die Eingabeliste.

liste_teilchen = ['Helium','Proton','Eisen','Sauerstoff','Nitrogen']
erste_und_letzte_tauschen(liste_teilchen) # Hier führe ich die Funktion aus.
# Es ist zu beachten, dass für den Output der Funktion keine neue Variable definiert wird, die keine ... hat.
print(liste_teilchen)

# %% [markdown] id="RpNfmxfDopmF"
# Um zu versuchen:
#
# 1. Erstellen Sie eine Funktion, die die Seiten eines Dreiecks entgegennimmt und die von diesen gebildeten Winkel berechnet.
# 2. Nehmen Sie eine Zahl entgegen und geben Sie alle Primzahlen bis zu dieser Zahl zurück.

# %% id="E41EQ69No2-K"

# %% [markdown] id="nIc4UUY-3v0b"
# # 7. Bibliotheken
#
#
# ---
#
#
# _import_ bibliotheksname
#
#
# ---
#
# Wir haben bereits zuvor eine verwendet, aber jetzt stellen wir sie offiziell vor.
# Manchmal möchte man spezifische Funktionen nutzen, die nicht zur Standardausstattung von Python gehören. Hierfür gibt es Funktionsbibliotheken – die man sogar selbst erstellen kann –, welche spezifische Funktionen enthalten.
#
#
# Diese spezifischen Funktionen werden wie folgt aufgerufen:
#
#
# bibliotheksname.funktionsname

# %% [markdown] id="V0cDrj7mr6Lm"
# ## Importieren
#
# Um diese Funktionen nutzen zu können, muss die Bibliothek importiert werden.

# %% id="qYCRaZRm3v0c"
import time           # Importiert die Funktionsbibliothek für die Zeitverarbeitung.

startzeit = time.time()          # Nimm die Zeit der Maschine.
time.sleep(1)                         # Warte 1 Sekunde
endzeit = time.time()            # Nimm die Zeit der Maschine.
print(endzeit - startzeit)  # Verstrichene Zeit in Sekunden

# %% id="npB681qh3v0d"
import os   # Bibliothek zur Handhabung von Pfaden, Dateien, Ordnern usw.

# Gibt den Pfad des aktuellen Verzeichnisses zurück (get Current Working Directory)
directory = os.getcwd()
print(directory)

# %% [markdown] id="aBQ-SwTosOHX"
# Ich kann einen Import durchführen, indem ich den Namen der Bibliothek abkürze
#
# ---
#
#
# ***_import_*** bibliotheksname ***as*** abkürzung
#
#
# ---

# %% id="CHiZoAS3sbqt"
import time as t     #Ich importiere die Funktionsbibliothek für die Zeitverarbeitung.

startzeit = time.time()          # Nimm die Zeit der Maschine.
time.sleep(1)                         # Warte 1 Sekunde
endzeit = time.time()            # Nimm die Zeit der Maschine.
print(endzeit - startzeit)  # Verstrichene Zeit in Sekunden

# %% [markdown] id="o45gycvH3v0i"
# Ich kann auch eine einzelne Funktion aus einer Bibliothek importieren
#
# ---
#
#
# ***_from_*** bibliotheksname ***_import_*** funktionsname
#
#
# ---

# %% id="r0H7RXDN3v0i"
from time import time, sleep

startzeit = time()               # Nimm die Zeit der Maschine.
sleep(1)                              # Warte 1 Sekunde
endzeit = time()                 # Nimm die Zeit der Maschine.
print(endzeit - startzeit)  # Verstrichene Zeit in Sekunden

# %% [markdown] id="VaBCVD3r3v0m"
# ## 8. Noch mehr Numpy
#
#
# Dokumentation https://docs.scipy.org/doc/numpy/reference/index.html

# %% id="HMm1Glu43v0n"
import numpy as np

# %% [markdown] id="XqF2i6IK3v2F"
# ### Zufallszahlen generieren

# %% id="CkFWB9_5xB0F"
np.random.random() # Gibt eine Zufallszahl zwischen 0 und 1 zurück, gleichverteilt.

# %% id="YSnWlcSJ3v2G"
# Gibt 'size' Zufallszahlen zwischen 'low' und 'high' zurück, gleichverteilt.
random_vector = np.random.uniform(low=0, high=10, size=10)
print(random_vector)

# %% colab={"base_uri": "https://localhost:8080/", "height": 193} id="tAQSYzFuxyGx" outputId="a6c63f55-f91d-4c9e-e9b1-80913da958d9"
# Gibt 'size' Zufallszahlen mit Gauß- bzw. Normalverteilung zurück
# 'loc' ist der Mittelwert und 'scale' das Sigma
random_vector = np.random.normal(loc=1, scale=0.1, size=10)
print(random_vector)

# %% [markdown] id="Sci40fCi3v2h"
# ## 9. Matplotlib (Visualisierung)
#
# Bibliothek zur Erstellung von Grafiken.
#
#
# Dokumentation
# https://matplotlib.org/

# %% id="RJpYefMi3v2i"
import matplotlib.pylab as plt

# %% id="8-jpoVHq3v2k"
x = np.arange(100) # Vektor von Ganzzahlen zwischen 0 und 100
y = x**2           # Ich quadriere jedes Element.
plt.plot(x, y)     # x-y-Diagramm
plt.show()

# %% id="KfpbHQEH3v2l"
plt.plot(x, y, 'g.', label="Grüne Punkte")
#'g', damit die Darstellung in Grün (green) erfolgt
#'.', damit die Darstellung mit Punkten anstelle einer Linie erfolgt
#label steht für die Legende
plt.plot(x, y+1000, 'r*', label = "Rote Sterne")
#'r' für eine Darstellung in Rot (red)
#'*' für eine Darstellung mit Sternchen
plt.xlabel("X")             # Ich benenne die x-Achse.
plt.ylabel("X$^2$")         # Ich benenne die y-Achse.
plt.title("Parabelen")      # Ich füge einen Titel hinzu.
plt.legend()                # Schaffe die Legende mit den Labels.
plt.show()                  # Zeigt das Bild

# %% id="Ul5RiXlV3v2n"
y = np.exp(x) # Exponentialfunktion

# Subplots erstellen:
# 2 Spalten, 1 Zeile -> 2 Diagramme.
# Figurengröße in x und y: 12*6
fig, ax = plt.subplots(ncols=2, nrows=1, figsize=(12,6))
plt.suptitle("Das sieht wirklich gut aus.")

#erster plot
ax[0].plot(x, y, 'g.', label="exponentiell!!!")
ax[0].set_xlabel("x")
ax[0].legend()
#zweiter plot
ax[1].semilogy(x, y, 'r*', label = "WOW! Achse und logarithmisch") #rot mit kleinen Sternen
ax[1].legend() #Verwende die Labels, um die Legende zu erstellen.
plt.show()

# %% id="0XnsCyce3v2p"
color = (0.5,0.2,0.8,0.7)#(red,green,blue,alpha) wobei Alpha die Opazität ist
x = np.random.exponential(scale=10,size=100)
y = x**2

plt.loglog(x,y,'o',c=color)
plt.title("logarithmische Skalierung auf beiden Achsen")
plt.show()

# %% id="GBvMy9X23v2q"
plt.bar([1,5,8],[2,4,6])
plt.show()

# %% id="6MjSew8q3v2s"
for size in [10, 100, 1000, 10000]:
    r = np.random.normal(loc=5, scale=3, size=size)
    plt.hist(r, bins=int(np.sqrt(size)))#histograms
    plt.axvline(5, c="red")#vertical lines
    plt.title("size = {}".format(size))
    plt.show()


# %% [markdown] id="LlHFNPc-tzB0"
# Versuch mal:
#
# 1. Die Sinusfunktion zwischen −2π und 2π.
# 2. Die Quadratwurzelfunktion zwischen 0 und 100.
# 3. Die Funktion y = 3x² + 5 zwischen −5 und 5.

# %% id="KS5PhLq8uA38"

# %% [markdown] id="hdYrDT0YuJdj"
# ## Extra
#
# Analysieren Sie die folgenden Programme und bestimmen Sie, was sie bewirken:
#

# %% id="EuFyKMhvujzx"
#1
def y(x):
  result = 1
  for i in range(1,x+1,1):
    result=result*i
  return(result)

#2
def y(x):
  if np.floor(x)-x<0:
    print('X is not an integer.')
    result = NaN
  else:
      if x==0:
        result = 1
      else:
        result=1
        for i in range(1,x+1,1):
            result = result*i
    return(result)
#Hinweis: floor(x) liefert den ganzzahligen Anteil von x.

#3
def m(x):
  n = len(x)
  a = x[0]
  for i in range(2,n):
    if x[i]<a:
      a = x[i]
  return(a)

#4
def A(n):
  A = []
  for i in range(n):
    a = []
    for j in range(n):
      if i==j:
        a.append(1)
      else:
        a.append(0)
        A.append(a)
        A = np.asarray(A)
  return(A)

#5
a = 1
while not (a+1)==1:
  a = a/2
print(a)

#6
def g(x):
  y = 1
  z = 0
  i = 1
  while not y==z:
    z = y;
    y = y+x^i/f(i);
    i = i+1;
  return(y)
#Hinweis: f(i) ist die Funktion aus Punkt a).


# %% [markdown] id="NCr5fbiG3v2v"
# ## ExtraExtra. SciPy (Anpassungen und mehr)
#
# Bibliothek für statistische Analysen und nützliche Funktionen wie Kurvenanpassungen (Fitting).
#
# Dokumentation
# https://scipy-cookbook.readthedocs.io/items/FittingData.html

# %% [markdown] id="Mf3YsdVE1l43"
# Beispiele für Anpassungen

# %% [markdown] id="3bn-pouT3v2v"
# ### Minimierung

# %% id="AUjhYtFY3v2w"
from scipy.optimize import minimize
f = lambda X:((X[0]-5)**2)+(X[1]-7)**2 #zu minimierende Funktion
x0 = [0, 0] #Ausgangswerte, bei denen mit der Untersuchung der Minimierung begonnen werden soll
res = minimize(f, x0, method='Nelder-Mead', tol=1e-6)
res #Minima in [5, 7]

# %% [markdown] id="48JxMtC93v2y"
# ### Kleinste Quadrate

# %% id="7pWNfPDx3v2y"
import numpy as np
from scipy import optimize
import matplotlib.pylab as plt
# %matplotlib inline

# erzeugt Punkte mit Rauschen
num_points = 150
x = np.linspace(-20, 5., num_points)
y = x**2+5*x-2+np.random.normal(scale=10, size=num_points)

# %% [markdown] id="fqWDDdy13v2z"
# Lineares Fiting

# %% id="SX0cstCI3v20"
fitfunc = lambda p, x: p[0]*x+p[1]# Funktion, mit der wir die Daten fitten wollen
p0 = [1, 1] # Anfangsparameter für die Anpassung

# %% id="W8IUvwou3v21"
errfunc = lambda p, x, y: fitfunc(p, x) - y # Abstand zur Zielfunktion
p1, success = optimize.leastsq(errfunc, p0[:], args=(x, y))
plt.plot(x, y, "ro", x, fitfunc(p1, x), "k-", linewidth=3)

# %% [markdown] id="v__fAdUh3v23"
# Quadratische Anpassung

# %% id="X1NUAF4v3v24"
fitfunc = lambda p, x: p[0]*x**2+p[1]*x+p[2]# Funktion, mit der wir die Daten fitten wollen
p0 = [1, 1, 1] # Anfangsparameter für die Anpassung

# %% id="alDUdQQk3v25"
errfunc = lambda p, x, y: fitfunc(p, x) - y # Abstand zur Zielfunktion
p1, success = optimize.leastsq(errfunc, p0[:], args=(x, y))
plt.plot(x, y, "ro", x, fitfunc(p1, x), "k-", linewidth=3)

# %% [markdown] id="jP4raqQ_3v26"
# ### Fit a power law (Scale-free networks)
#
# #### Generate the data
# Generate some data with noise to demonstrate the fitting procedure. Data is generated with an amplitude of 10 and a power-law index of -2.0. Notice that all of our data is well-behaved when the log is taken... you may have to be more careful of this for real data.

# %% id="4aq_wnuM3v27"
# Define function for calculating a power law
powerlaw = lambda x, amp, index: amp * (x**index)

##########
# Generate data points with noise
##########
num_points = 20

# Note: all positive, non-zero data
xdata = np.linspace(1.1, 10.1, num_points)
ydata = powerlaw(xdata, 10.0, -2.0)     # simulated perfect data
yerr = 0.2 * ydata                      # simulated errors (10%)

ydata += np.random.randn(num_points) * yerr       # simulated noisy data

plt.plot(xdata,ydata)
plt.errorbar(xdata, ydata, yerr=yerr, fmt='k.')
plt.show()

# %% [markdown] id="RepHILlH3v29"
#
# #### Fit the data
#
# If your data is well-behaved, you can fit a power-law function by first converting to a linear equation by using the logarithm. Then use the optimize function to fit a straight line. Notice that we are weighting by positional uncertainties during the fit. Also, the best-fit parameters uncertainties are estimated from the variance-covariance matrix. You should read up on when it may not be appropriate to use this form of error estimation.
#
# If you are trying to fit a power-law distribution, [this first solution] or [this second solution](https://github.com/keflavich/plfit) are more appropriated. (Todavia no probamos estos paquetes, y tampoco es la intención que lo hagan de esa forma)
#

# %% id="mPVVG8qK3v2-"
##########
# Fitting the data -- Least Squares Method
##########

# Power-law fitting is best done by first converting
# to a linear equation and then fitting to a straight line.
# Note that the `logyerr` term here is ignoring a constant prefactor.
#
#  y = a * x^b
#  log(y) = log(a) + b*log(x)
#

logx = np.log10(xdata)
logy = np.log10(ydata)
logyerr = yerr / ydata

# define our (line) fitting function
fitfunc = lambda p, x: p[0] + p[1] * x
errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err

pinit = [1.0, -1.0]
out = optimize.leastsq(errfunc, pinit,args=(logx, logy, logyerr), full_output=1)

pfinal = out[0]
covar = out[1]
print(pfinal)
print(covar)

index = pfinal[1]
amp = 10.0**pfinal[0]

indexErr = np.sqrt( covar[1][1] )
ampErr = np.sqrt( covar[0][0] ) * amp

##########
# Plotting data
##########

plt.clf()
plt.subplot(2, 1, 1)
plt.plot(xdata, powerlaw(xdata, amp, index))     # Fit
plt.errorbar(xdata, ydata, yerr=yerr, fmt='k.')  # Data
plt.text(5, 6.5, 'Ampli = %5.2f +/- %5.2f' % (amp, ampErr))
plt.text(5, 5.5, 'Index = %5.2f +/- %5.2f' % (index, indexErr))
plt.title('Best Fit Power Law')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(1, 11)

plt.subplot(2, 1, 2)
plt.loglog(xdata, powerlaw(xdata, amp, index))
plt.errorbar(xdata, ydata, yerr=yerr, fmt='k.')  # Data
plt.xlabel('X (log scale)')
plt.ylabel('Y (log scale)')
plt.xlim(1.0, 11)

# %%
