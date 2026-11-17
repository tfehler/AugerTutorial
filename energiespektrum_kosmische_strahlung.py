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

# %% [markdown] id="OhDcNMJWoITD"
# # Untersuchung des Energiespektrums kosmischer Strahlung
#
# ### Eine praktische Datenanalyse-Übung am Beispiel des Pierre-Auger-Observatoriums
#
# **Physik – Jahrgangsstufe 11 (Gymnasium)**
#
# In dieser Übung untersuchen wir eine der spannendsten Fragen der Astroteilchenphysik:
#
# **Wie hängt die Anzahl der auf der Erde eintreffenden Teilchen kosmischer Strahlung von deren Energie ab?**
#
# Anhand echter experimenteller Daten des Pierre-Auger-Observatoriums lernen wir, wie Wissenschaftlerinnen und Wissenschaftler das Energiespektrum kosmischer Strahlung erstellen.
#
# Wir werden die Daten erkunden, Diagramme erstellen, einfache Berechnungen durchführen und die Ergebnisse interpretieren.
#
# Es sind keine Vorkenntnisse in Python erforderlich.

# %% [markdown] id="CkRRTQ7VoXxm"
# ## Was werden wir tun?
#
# Im Rahmen dieser Übung durchlaufen wir die Schritte einer echten wissenschaftlichen Analyse.
#
# 1. Wir lernen, was kosmische Strahlung ist und wie sie nachgewiesen wird.
# 2. Wir untersuchen Messdaten des Pierre-Auger-Observatoriums.
# 3. Wir analysieren die Energien einzelner Ereignisse kosmischer Strahlung.
# 4. Wir zählen, wie viele Ereignisse in verschiedene Energieintervalle fallen.
# 5. Wir korrigieren unsere Messdaten hinsichtlich der Detektor-Exposure.
# 6. Wir erstellen das Energiespektrum der kosmischen Strahlung.
# 7. Wir interpretieren die Ergebnisse und identifizieren interessante Merkmale.
#
# Am Ende haben Sie mithilfe echter experimenteller Messdaten ein Energiespektrum erstellt.

# %% [markdown] id="fiuT3LnLo1fO"
# ## Ein paar Hinweise, bevor wir beginnen
#
# Wir werden Python verwenden, um experimentelle Daten zu analysieren.
#
# Python ist eine Programmiersprache, die häufig von Wissenschaftlern genutzt wird, um Messdaten auszuwerten, Berechnungen durchzuführen und Grafiken zu erstellen.
#
# Du musst nicht jede Zeile Code in diesem Notebook im Detail verstehen. Wichtig ist, dass du nachvollziehen kannst, was die jeweilige Operation bewirkt und welche Informationen sich daraus gewinnen lassen.
#
# **So gehst du vor:**
#
# - Befolge die Anweisungen in den einzelnen Abschnitten.
# - Führe die Code-Zellen nacheinander aus.
# - Besprich die Fragen mit deinem Partner bzw. deiner Partnerin.
# - Wenn du dazu aufgefordert wirst, den Code anzupassen, versuche zu verstehen, wie sich dadurch das Ergebnis verändert.
#
# Einige Zellen enthalten unvollständigen Code, den du selbst vervollständigen musst.

# %% [markdown] id="AMggT1IPpF8d"
# # 1. Was ist kosmische Strahlung?
#
# Kosmische Strahlung besteht aus hochenergetischen Teilchen, die aus dem Weltraum auf die Erde treffen.
#
# Der Großteil dieser Teilchen sind Atomkerne – vor allem Protonen und Heliumkerne –, wobei auch schwerere Atomkerne vorkommen.
#
# Sie bewegen sich mit Geschwindigkeiten nahe der Lichtgeschwindigkeit durch den Weltraum und können dabei enorme Energien erreichen.
#
# Wenn ein Teilchen der kosmischen Strahlung in die Erdatmosphäre eindringt, stößt es mit einem Atomkern in der Atmosphäre zusammen. Bei diesem Zusammenstoß entstehen Sekundärteilchen, die wiederum mit weiteren Atomkernen in der Atmosphäre wechselwirken und so noch mehr Teilchen erzeugen können.
#
# Die dadurch entstehende Kaskade von Teilchen nennt man einen **ausgedehnten Luftschauer**.
#
# ### Zum Nachdenken
#
# 1. Warum ist es deiner Meinung nach schwierig, kosmische Strahlung direkt nachzuweisen?
# 2. Was geschieht, wenn ein hochenergetisches Teilchen auf die Atmosphäre trifft?
# 3. Warum könnte man einen sehr großen Detektor benötigen, um kosmische Strahlung mit besonders hoher Energie zu untersuchen?

# %% [markdown] id="bH6OoK5WsxWM"
# # 2. Das Pierre-Auger-Observatorium
#
# Das Pierre-Auger-Observatorium befindet sich in der Nähe von Malargüe in der argentinischen Provinz Mendoza.
#
# Es ist eines der weltweit größten Observatorien zur Erforschung kosmischer Strahlung.
#
# Das Observatorium nutzt zwei sich ergänzende Verfahren zur Untersuchung ausgedehnter Luftschauer.
#
# ### Oberflächendetektor (Surface Detector, SD)
#
# Der Oberflächendetektor besteht aus Wasser-Tscherenkow-Detektoren, die über ein großes Gebiet verteilt sind.
#
# Diese Detektoren messen die Sekundärteilchen, die den Boden erreichen.
#
# ### Fluoreszenzdetektor (Fluorescence Detector, FD)
#
# Der Fluoreszenzdetektor besteht aus Teleskopen, die ultraviolettes Licht beobachten. Dieses Licht entsteht, wenn Teilchen eines Luftschauers Stickstoffmoleküle in der Atmosphäre anregen.
#
# Durch die Kombination dieser Messungen können Wissenschaftler Eigenschaften der ursprünglichen kosmischen Strahlung rekonstruieren, darunter deren Energie und Einfallsrichtung.
#
# In dieser Übung arbeiten wir mit rekonstruierten Messdaten des Oberflächendetektors.

# %% id="Js7ifFy-n44O"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set the default appearance of our plots
plt.rcParams["figure.figsize"] = (9, 5)
plt.rcParams["font.size"] = 12

print("Bereit zur Analyse von Daten zur kosmischen Strahlung!")

# %% [markdown] id="IAmZxyjbpUpD"
# # 3. Untersuchung der experimentellen Daten
#
# Wir verwenden echte Messdaten, die von der Pierre-Auger-Kollaboration bereitgestellt wurden.
#
# Die Daten liegen in CSV-Dateien (Comma-Separated Values) vor. Jede Zeile entspricht einem Ereignis kosmischer Strahlung, während jede Spalte Informationen zu diesem Ereignis enthält.
#
# Unser Datenarchiv umfasst drei Datensätze:
#
# - **SD1500:** Ereignisse, die mit dem Oberflächen-Detektor-Array (Surface Detector array) mit 1500 m Abstand detektiert wurden.
# - **SD750:** Ereignisse, die mit dem Oberflächen-Detektor-Array mit 750 m Abstand detektiert wurden.
# - **Inclined:** Ereignisse, die unter großen Zenitwinkeln einfallen.
#
# Wir konzentrieren uns dabei hauptsächlich auf den Datensatz SD1500.
#
# ### Vorbereitung der Dateien
#
# Die Datei `summary.zip` muss sich im selben Ordner befinden wie dieses Notebook.
#
# Der nachstehende Code entpackt das Archiv und stellt die CSV-Dateien für die Analyse bereit.

# %% id="Jh5egauupuOX"
from pathlib import Path
import zipfile

# Find the ZIP archive in the notebook's working directory
zip_path = Path("summary.zip")

if not zip_path.exists():
    raise FileNotFoundError(
        "summary.zip wurde nicht gefunden."
"Legen Sie die Datei in denselben Ordner wie dieses Notebook."
    )

# Extract the archive
with zipfile.ZipFile(zip_path, "r") as archive:
    archive.extractall("auger_data")

print("Daten erfolgreich extrahiert!")

# %% id="ZMrVhLzrtgPA"
# Load the three CSV files

data_sd1500 = pd.read_csv(
    "auger_data/summary/dataSummarySD1500.csv"
)

data_sd750 = pd.read_csv(
    "auger_data/summary/dataSummarySD750.csv"
)

data_inclined = pd.read_csv(
    "auger_data/summary/dataSummaryInclined.csv"
)

print("SD1500:", len(data_sd1500), "events")
print("SD750:", len(data_sd750), "events")
print("Inclined:", len(data_inclined), "events")

# %% [markdown] id="9zHbYCq8pvEb"
# ### Wie sieht ein experimenteller Datensatz aus?
#
# Betrachten wir die ersten Ereignisse, die im SD1500-Datensatz aufgezeichnet wurden.
#
# Jede Zeile entspricht einem Ereignis durch kosmische Strahlung.
#
# Jede Spalte enthält eine bestimmte Eigenschaft des Ereignisses, wie etwa dessen Energie oder Einfallsrichtung.

# %% id="XeMIdoMcp1nP"
display(data_sd1500.head())

# %% id="VGxFBDKXtrVk"
print("Verfügbare Variablen:\n")

for column in data_sd1500.columns:
    print(column)

# %% [markdown] id="CSOyNS1Et_CZ"
# ### Einige wichtige Variablen
#
# Im Verlauf dieser Übung werden wir verschiedene Variablen verwenden.
#
# | Variable | Bedeutung |
# |---|---|
# | `sd_energy` | Rekonstruierte Energie der kosmischen Strahlung |
# | `sd_theta` | Zenitwinkel der einfallenden kosmischen Strahlung |
# | `sd_phi` | Azimutwinkel der einfallenden kosmischen Strahlung |
# | `sd_s1000` | Signal, gemessen in einem Referenzabstand von 1000 m |
# | `sd_s38` | Schauersignal, korrigiert auf einen Referenz-Zenitwinkel von 38° |
# | `sd_exposure` | Detektor-Exposure zum Zeitpunkt des Ereignisses |
#
# Die Energie wird in **EeV (Exa-Elektronenvolt)** angegeben.
#
# Zur Erinnerung:
#
# $1$ EeV = $10^{18}$ eV
#
# Zum Beispiel:
#
# $5$ EeV = $5 × 10^{18}$ eV.

# %% [markdown] id="bTvHOl9hwR9_"
# # 4. Wie sind die Energien der kosmischen Strahlung verteilt?
#
# Jedes Ereignis in unserem Datensatz entspricht einem registrierten Luftschauer. Für jedes Ereignis haben die Wissenschaftlerinnen und Wissenschaftler die Energie des ursprünglichen kosmischen Teilchens rekonstruiert.
#
# Aber treffen Teilchen aller Energien gleich häufig auf die Erde?
#
# Um das herauszufinden, untersuchen wir zunächst die Energieverteilung unserer Messdaten.
#
# ### 4.1 Die Energie der einzelnen Ereignisse
#
# Wir betrachten zunächst die rekonstruierte Energie aller Ereignisse im SD1500-Datensatz.
#
# Schauen wir uns zunächst einige grundlegende Eigenschaften der Energieverteilung an.

# %% id="q0pabuq5wdc7"
# Wählen Sie die rekonstruierten Energien aus
energy = data_sd1500["sd_energy"].dropna()

# Ungültige Werte entfernen
energy = energy[energy > 0]

print("Anzahl der Ereignisse:", len(energy))
print("Mindestenergie:", energy.min(), "EeV")
print("Maximale Energie:", energy.max(), "EeV")
print("Mittlere Energie:", energy.mean(), "EeV")

# %% [markdown] id="TMAmkOdiw5tb"
# 1. Wie viele Ereignisse sind in unserem Datensatz enthalten?
# 2. Wie hoch ist die höchste rekonstruierte Energie?
# 3. Wie groß ist der Unterschied zwischen der mittleren und der maximalen Energie?
# ### 4.2 Darstellung der Energieverteilung
# Um zu verstehen, wie häufig verschiedene Energien auftreten, können wir ein Histogramm erstellen.
#
# Ein Histogramm fasst Messwerte in Intervallen zusammen und zählt, wie viele Messwerte in das jeweilige Intervall fallen.
#
# Da die Energien kosmischer Strahlung einen sehr großen Bereich abdecken, verwenden wir eine logarithmische Energieachse.

# %% id="pL508pqdxCIj"
# Logarithmisch verteilte Intervalle erstellen
bins = np.logspace(
    np.log10(energy.min()),
    np.log10(energy.max()),
    25
)

plt.hist(energy, bins=bins, edgecolor="black")

plt.xscale("log")
plt.xlabel("Energie [EeV]")
plt.ylabel("Anzahl der Ereignisse")
plt.title("Energieverteilung der kosmischen Strahlung")

plt.grid(alpha=0.3)
plt.show()

# %% [markdown] id="aY-3Jp-Fxp78"
# 1.   Treten Ereignisse mit niedriger Energie oder Ereignisse mit hoher Energie häufiger auf?
# 2.   Nimmt die Anzahl der Ereignisse mit zunehmender Energie zu oder ab?
# 3.   Warum verwenden wir Ihrer Meinung nach eine logarithmische Skala anstelle einer linearen Skala?

# %% [markdown] id="00dGvPo-ymG9"
# In unserem Datensatz besitzt jedes Ereignis eine eigene rekonstruierte Energie. Um das Energiespektrum zu erstellen, müssen wir herausfinden, wie viele Ereignisse in verschiedenen Energiebereichen auftreten.
#
# Dazu teilen wir den gesamten Energiebereich in kleinere Intervalle, sogenannte **Energie-Bins**.
#
# Anschließend zählen wir, wie viele Ereignisse in jedes dieser Intervalle fallen.
#
# ### Warum verwenden wir logarithmische Intervalle?
#
# Die Energien der kosmischen Strahlung erstrecken sich über mehrere Größenordnungen. Deshalb sind gleich große Intervalle auf einer linearen Energieskala für unsere Untersuchung nicht besonders geeignet.
#
# Stattdessen verwenden wir Intervalle, die auf einer logarithmischen Skala gleich breit sind.
#
# Das bedeutet beispielsweise, dass die Energieintervalle nicht alle dieselbe absolute Breite haben, sondern denselben relativen Größenbereich abdecken.
#
# ### Eine wichtige Einschränkung
#
# Für unsere Untersuchung verwenden wir zunächst nur vertikale Ereignisse des SD1500-Detektors mit:
#
# - Zenitwinkel kleiner als $60^\circ$
# - Energie von mindestens $2{,}5\,\mathrm{EeV}$
#
# Oberhalb dieser Energieschwelle arbeitet der SD1500-Detektor mit einer Detektionseffizienz von mehr als 97 %.
#
# Damit vermeiden wir, dass unsere Untersuchung durch eine stark energieabhängige Detektionseffizienz beeinflusst wird.

# %% id="bCfGDqQoy0VZ"
# Wählen Sie vertikale SD1500-Ereignisse oberhalb der Energieschwelle aus.

energy_min = 2.5  # EeV

selected_events = data_sd1500[
    (data_sd1500["sd_theta"] < 60) &
    (data_sd1500["sd_energy"] >= energy_min)
].copy()

print("Ereignisse vor der Auswahl:", len(data_sd1500))
print("Ereignisse nach der Auswahl:", len(selected_events))

# %% id="tpcHIcnSzD45"
energy = selected_events["sd_energy"].dropna()

print("Anzahl der ausgewählten Ereignisse:", len(energy))
print("Mindestenergie:", energy.min(), "EeV")
print("Maximale Energie:", energy.max(), "EeV")

# %% [markdown] id="YBSmXg3VzRNU"
# Wir wollen nun festlegen, in wie viele Energieintervalle wir unsere Messdaten einteilen.
#
# Dazu müssen wir zwei Dinge bestimmen:
#
# 1. Die minimale Energie: $E_{\min}=2{,}5\,\mathrm{EeV}$
# 2. Die Anzahl der Energieintervalle.
#
# Je mehr Intervalle wir verwenden, desto genauer können wir Unterschiede innerhalb der Energieverteilung untersuchen. Allerdings befinden sich dann weniger Ereignisse in jedem einzelnen Intervall.
#
# Wir beginnen mit 12 Energieintervallen.
#
# **Aufgabe 1:** Überlege, was passieren könnte, wenn wir statt 12 beispielsweise 5 oder 30 Intervalle verwenden.

# %% id="0nv_QpI_zQ5S"
# Wählen Sie die Anzahl der Energieintervalle aus
number_of_bins = 12

# Den Energiebereich bestimmen
energy_max = energy.max()

# Logarithmisch unterteilte Energieintervalle erstellen
energy_bins = np.logspace(
    np.log10(energy_min),
    np.log10(energy_max),
    number_of_bins + 1
)

print("Energieintervallgrenzen [EeV]:")
print(energy_bins)

# %% id="uU1_S7Yczo_N"
plt.figure(figsize=(9, 5))

plt.hist(
    energy,
    bins=energy_bins,
    edgecolor="black"
)

plt.xscale("log")
plt.xlabel("Energie [EeV]")
plt.ylabel("Anzahl der Ereignisse")
plt.title("Energieverteilung mit logarithmischen Intervallen")

plt.grid(alpha=0.3)
plt.show()

# %% [markdown] id="fhn0-K8EzuS-"
# Vergleiche dieses Diagramm mit dem Histogramm aus Abschnitt 4.
# - Was hat sich verändert?
# - Sind die Energieintervalle gleich breit?
# - Warum sind die Intervalle auf der rechten Seite des Diagramms breiter?

# %% [markdown] id="-L7Pf29bzvWp"
# Jetzt kommen wir zum eigentlichen Ziel dieses Abschnitts: Wir wollen wissen, wie viele Ereignisse in jedes Energieintervall fallen.
#
# Python kann diese Zählung automatisch durchführen.
#
# Dazu verwenden wir die Funktion `np.histogram()`. Sie ordnet jedes Ereignis dem passenden Energieintervall zu und zählt die Anzahl der Ereignisse.
#
# **Aufgabe 3:** Führe die folgende Zelle aus und untersuche die Ergebnisse.

# %% id="3aLFdpBAz4Jl"
# Zähle die Ereignisse in jedem Energieintervall
event_counts, bin_edges = np.histogram(
    energy,
    bins=energy_bins
)

# Berechne die Mitte jedes Intervalls.
bin_centers = np.sqrt(
    bin_edges[:-1] * bin_edges[1:]
)

# Erstelle eine Tabelle mit den Ergebnissen
results = pd.DataFrame({
    "E_min [EeV]": bin_edges[:-1],
    "E_max [EeV]": bin_edges[1:],
    "E_center [EeV]": bin_centers,
    "Anzahl der Ereignisse": event_counts
})

display(results.round(2))

# %% id="nvOaw1QS0N6W"
plt.figure(figsize=(9, 5))

plt.scatter(
    bin_centers,
    event_counts,
    s=60
)

plt.plot(
    bin_centers,
    event_counts,
    alpha=0.5
)

plt.xscale("log")
plt.xlabel("Energie [EeV]")
plt.ylabel("Anzahl der Ereignisse")
plt.title("Anzahl der Ereignisse pro Energieintervall")

plt.grid(alpha=0.3)
plt.show()

# %% [markdown] id="8CsRY_Dk1CH-"
# **Aufgabe – Interpretation der Ergebnisse**
#
# 1. In welchem Energieintervall wurden die meisten Ereignisse registriert?
# 2. Wie verändert sich die Anzahl der Ereignisse mit zunehmender Energie?
# 3. Gibt es Energieintervalle, in denen nur sehr wenige Ereignisse vorkommen?
#
# **Aufgabe – Experimentiere mit den Energieintervallen**
#
# Ändere den Wert von `number_of_bins` in der entsprechenden Code-Zelle.
#
# Untersuche die Ergebnisse für:
#
# - 5 Energieintervalle
# - 12 Energieintervalle
# - 30 Energieintervalle
#
# Beantworte anschließend:
#
# 1. Wie verändert sich das Aussehen des Diagramms?
# 2. Was passiert mit der Anzahl der Ereignisse pro Intervall?
# 3. Bleibt die Gesamtzahl aller gezählten Ereignisse gleich?
#
# **Diskussionsfrage:** Warum könnte es problematisch sein, zu wenige oder zu viele Energieintervalle zu verwenden?

# %% [markdown] id="5l8DCF1u1nYF"
# ## 6. Die Rolle der Detektor-Exposure.
#
# ### 6.1 Was bedeutet Detektor-Exposure?
#
# Bisher haben wir gezählt, wie viele Ereignisse in den verschiedenen Energieintervallen registriert wurden.
#
# Allerdings hängt die Anzahl der gemessenen Ereignisse nicht nur davon ab, wie häufig kosmische Teilchen auf die Erde treffen.
#
# Sie hängt auch davon ab, wie lange und auf welcher Fläche wir messen und aus welchen Richtungen Teilchen nachgewiesen werden können.
#
# Diese Eigenschaften werden durch die Detektor-Exposure berücksichtigt.
#
# Die Exposure wird in
#
# $
# \mathrm{km^2\,sr\,yr}
# $
#
# angegeben und berücksichtigt:
#
# - die effektive Detektorfläche,
# - den erfassten Raumwinkel,
# - die Beobachtungszeit.
#
# Eine größere Exposure bedeutet, dass mehr kosmische Teilchen registriert werden können, selbst wenn der tatsächliche Teilchenfluss gleich bleibt.
#
# **Merke:** Um verschiedene Messungen miteinander vergleichen zu können, müssen wir die Detektor-Exposure berücksichtigen.
#
# ### 6.2 Untersuchung der Exposure in unseren Messdaten
# Der Datensatz enthält die Variable `sd_exposure`. Sie gibt für jedes Ereignis die akkumulierte Exposure des SD1500-Arrays zum Zeitpunkt der Aufzeichnung an.
#
# Dies ist hilfreich, da wir so die Exposure für den Zeitraum der ausgewählten Ereignisse bestimmen können.

# %% id="djlz6qqW2SzF"
# Gültige Belichtungswerte auswählen
exposure = selected_events["sd_exposure"].dropna()

print("Minimale Exposure:", exposure.min(), "km² sr yr")
print("Maximale Exposure:", exposure.max(), "km² sr yr")

# %% [markdown] id="z3jmoTsb2n29"
# ### 6.3 Warum dürfen wir die Exposure nicht einfach addieren?
# Die Exposurewerte sind kumulativ: Jeder Wert stellt die Exposure dar, die sich bis zum Zeitpunkt eines bestimmten Ereignisses angesammelt hat.
#
# Daher dürfen wir die Exposurewerte einzelner Ereignisse nicht addieren. Dies würde dazu führen, dass derselbe Beobachtungszeitraum mehrfach gezählt wird.
#
# Für unsere vereinfachte Analyse verwenden wir den maximalen Exposurewert innerhalb der ausgewählten Stichprobe als Schätzwert für die kumulierte Exposure:

# %% id="jqOXasCH2txl"
# Ungefähres Gesamtexposure unserer ausgewählten Stichprobe
total_exposure = exposure.max()

print("Gesamtexposure:", total_exposure, "km² sr yr")

# %% [markdown] id="M4hSaXs8213I"
# ### Aufgabe – Überprüfe dein Verständnis
#
# 1. Was bedeutet eine größere Detektor-Exposure?
# 2. Warum können wir die Exposureswerte nicht einfach addieren?
# 3. Warum reicht es nicht aus, nur die Anzahl der registrierten Ereignisse zu kennen?
#
# **Merke:** Die Anzahl der Ereignisse allein sagt uns noch nicht, wie häufig kosmische Teilchen tatsächlich auf die Erde treffen. Dafür müssen wir auch berücksichtigen, wie lange und mit welcher effektiven Fläche wir gemessen haben.

# %% [markdown] id="uNlPSss-23G1"
# ## 7. Konstruktion des Energiespektrums
#
# ### 7.1 Vom Ereigniszähler zum Energiespektrum
#
# Bisher haben wir untersucht, wie viele Ereignisse in den verschiedenen Energieintervallen registriert wurden.
#
# Allerdings wissen wir jetzt, dass die Anzahl der Ereignisse auch von der Detektor-Exposure abhängt.
#
# Um die Häufigkeit der kosmischen Strahlung bei verschiedenen Energien zu bestimmen, berechnen wir den sogenannten **differentiellen Teilchenfluss**.
#
# Dazu berücksichtigen wir:
#
# - die Anzahl der registrierten Ereignisse,
# - die Breite des Energieintervalls,
# - die Detektor-Exposure.
#
# Der differentielle Teilchenfluss wird näherungsweise durch folgende Gleichung beschrieben:
#
# $
# J(E_i)=\frac{N_i}{\Delta E_i\cdot\mathcal{E}}
# $
#
# Dabei bedeuten:
#
# - $N_i$: Anzahl der Ereignisse im Energieintervall
# - $\Delta E_i$: Breite des Energieintervalls
# - $\mathcal{E}$: Detektor-Exposure
#
# Der differentielle Teilchenfluss beschreibt, wie viele kosmische Teilchen pro Energieintervall, Fläche, Raumwinkel und Zeit eintreffen.
#
# **Unser Ziel:** Wir wollen den Teilchenfluss für jedes Energieintervall berechnen und anschließend grafisch darstellen.

# %% [markdown] id="0rAANTrK4M7X"
# ### 7.2 Berechnung des differentiellen Teilchenflusses

# %% id="tgb_kNSO4Qdl"
# Verwenden Sie die maximal akkumulierte Exposure des vollständigen SD1500-Datensatzes.
total_exposure = data_sd1500["sd_exposure"].max()

print("Detektor-Exposure:", total_exposure, "km² sr yr")

# %% id="J5oSHytm4VXn"
# Berechne die Breite jedes Energieintervalls.
bin_widths = bin_edges[1:] - bin_edges[:-1]

# Berechne den differentiellen Fluss der kosmischen Strahlung
flux = event_counts / (bin_widths * total_exposure)

# Füge die Ergebnisse unserer Tabelle hinzu.
results["Bin width [EeV]"] = bin_widths
results["Flux [km^-2 sr^-1 yr^-1 EeV^-1]"] = flux

display(results.round(4))

# %% [markdown] id="o7Dwndiw4yZq"
# ### 7.3 Darstellung des Energiespektrums
#
# Jetzt können wir unser Energiespektrum darstellen.
#
# Auf der horizontalen Achse tragen wir die Energie auf, auf der vertikalen Achse den berechneten differentiellen Teilchenfluss.
#
# Da sich sowohl die Energien als auch der Teilchenfluss über mehrere Größenordnungen erstrecken, verwenden wir logarithmische Skalen für beide Achsen.

# %% id="cU-m2V_X420F"
plt.figure(figsize=(9, 5))

plt.scatter(bin_centers, flux, s=60)

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Energie [EeV]")
plt.ylabel("Differentieller Teilchenfluss")
plt.title("Energiespektrum der kosmischen Strahlung")

plt.grid(alpha=0.3, which="both")
plt.show()

# %% [markdown] id="N6hicD8B49q5"
# **Aufgabe**
#
# 1. Wie verändert sich der Teilchenfluss mit zunehmender Energie?
# 2. In welchen Energieintervallen ist der Teilchenfluss besonders groß?
# 3. Warum benötigen wir eine logarithmische Darstellung?
#
# **Aufgabe**
#
# Vergleiche dieses Diagramm mit dem Histogramm aus Abschnitt 5.
#
# Warum sehen die beiden Diagramme unterschiedlich aus, obwohl sie auf denselben Messdaten beruhen?

# %% [markdown] id="Kl-NNrju5NWn"
# In wissenschaftlichen Veröffentlichungen wird das Energiespektrum häufig nicht direkt als $J(E)$, sondern als $E^3J(E)$ dargestellt.
#
# Der Grund dafür ist, dass der Teilchenfluss mit steigender Energie sehr stark abnimmt. Durch die Multiplikation mit $E^3$ werden Veränderungen im Verlauf des Energiespektrums besser sichtbar.
#
# Wir können diese Darstellung ebenfalls ausprobieren.

# %% id="a5jS43m-5haK"
flux_scaled = (bin_centers**3) * flux

plt.figure(figsize=(9, 5))

plt.scatter(bin_centers, flux_scaled, s=60)

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Energie [EeV]")
plt.ylabel(r"$E^3 J(E)$")
plt.title("Energiespektrum der kosmischen Strahlung")

plt.grid(alpha=0.3, which="both")
plt.show()

# %% [markdown] id="_YMcn6KJ5wt8"
# ## 8. Interpretation des Energiespektrums
#
# ### 8.1 Was zeigt unser Energiespektrum?
#
# Wir haben nun unser eigenes Energiespektrum der kosmischen Strahlung erstellt.
#
# Es zeigt, wie häufig kosmische Teilchen unterschiedlicher Energien auf der Erde eintreffen.
#
# Betrachten wir unser Ergebnis noch einmal:
#
# - Der Teilchenfluss nimmt mit steigender Energie stark ab.
# - Besonders energiereiche kosmische Teilchen werden nur sehr selten registriert.
# - Das Energiespektrum zeigt, dass kosmische Strahlung nicht bei allen Energien gleich häufig vorkommt.
#
# Das bedeutet: Je höher die Energie eines kosmischen Teilchens ist, desto seltener wird es beobachtet.
#
# Aber unser Energiespektrum enthält noch weitere interessante Informationen.

# %% [markdown] id="GpktWhLQ6FOs"
# ### 8.2 Vergleich mit dem Energiespektrum des Pierre-Auger-Observatoriums
#
# Das veröffentlichte Energiespektrum des Pierre-Auger-Observatoriums zeigt, dass der Teilchenfluss nicht gleichmäßig mit der Energie abnimmt.
#
# Die zeigen zwei besonders wichtige Merkmale:
# - Der „Ankle“ (Knöchel): Bei etwa $5\times10^{18}\,\mathrm{eV}$ wird das Spektrum flacher.
# - Die Flussunterdrückung: Bei etwa $5\times10^{19}\,\mathrm{eV}$ wird das Spektrum deutlich steiler.
#
# Diese Merkmale geben Wissenschaftlerinnen und Wissenschaftlern wichtige Hinweise auf die Herkunft und Ausbreitung der kosmischen Strahlung.

# %% [markdown] id="lYGHxISn6wac"
# ### Was haben wir herausgefunden?
#
# Diskutiert gemeinsam die folgenden Fragen:
#
# 1. Warum nimmt die Anzahl der registrierten kosmischen Teilchen mit steigender Energie ab?
# 2. Warum benötigen wir ein großes Observatorium wie das Pierre-Auger-Observatorium, um besonders energiereiche Teilchen zu untersuchen?
# 3. Was können Veränderungen im Energiespektrum über die Herkunft kosmischer Strahlung verraten?
# 4. Warum ist es wichtig, nicht nur die Anzahl der Ereignisse, sondern auch die Detektor-Exposure zu berücksichtigen?
#
# ### Eine letzte Frage
#
# Das energiereichste Teilchen, das wir untersuchen können, besitzt eine Energie von mehreren $10^{19}\,\mathrm{eV}$.
#
# Wie würdest du jemandem erklären, warum ein einzelnes Teilchen eine so große Energie besitzen kann?

# %% [markdown] id="NcPB1QEI7EP-"
# ## Zusammenfassung
#
# In dieser Übung haben wir anhand echter Messdaten des Pierre-Auger-Observatoriums untersucht, wie kosmische Strahlung auf der Erde nachgewiesen wird.
#
# Dabei haben wir:
#
# 1. Messdaten eines Teilchendetektors untersucht.
# 2. Die Energien kosmischer Teilchen analysiert.
# 3. Ereignisse in Energieintervalle eingeteilt und gezählt.
# 4. Die Detektor-Exposure berücksichtigt.
# 5. Ein eigenes Energiespektrum erstellt.
# 6. Unsere Ergebnisse mit wissenschaftlichen Messungen verglichen.
#
# Damit haben wir einen vereinfachten Einblick in die Arbeit der experimentellen Astroteilchenphysik erhalten.
#
# **Herzlichen Glückwunsch! Ihr habt euer eigenes Energiespektrum kosmischer Strahlung erstellt.**

# %%
