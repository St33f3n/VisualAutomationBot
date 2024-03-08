---
Status: inWork
tags:
  - Projekt
Links:
  - "[[Übersicht über alle Projekte]]"
checksum: 
Erstellungsdatum: 2024-03-08
Modifikationsdatum: 2024-03-08
---

# Funktionsweise und Logik

## Grundprinzip

Ich öffne das zu automatisierende Programm und mache von den zu betätigenden Schaltflächen Screenshots.
Danach öffne ich das Playlist Bautool, und setze meine Logik zusammen.
Ich starte den Bot der automatisch nach meiner Vorgaben die Schaltflächen betätigt.

Was passiert dabei unter der Motorhaube:
Beispiel: Ich möchte auf einen Button drücken um ein Menü zu öffnen

Wenn der Bot gestartet ist, lädt er die Daten des ausgewählten Spiels ein. 
Daraufhin frägt er den Benutzer, wo auf dem Monitor sich die Spielfläche befindet.
Diese wird mit dem Mauszeiger und der Taste C festgelegt.
Wenn die Spielfläche festgelegt ist, führt er das hinterlegte Playset aus.
In unserem Fall ist im Playset nur ein Befehl enthalten ein clickIfPicture mit einem doppelten Argument des Buttons.
Das funktioniert, in dem er das gespeicherte Bild in die richtige Größe skaliert und mit dem IRA auf dem Bildschirm sucht.
Hat er das Bild gefunden, wird nun aufgrund des Bildes, die Koordinaten ermittelt und im Bereich des Bildes ein zufälliger Punkt ermittelt, in dem ein Click ausgeführt wird. Danach wird eine kurze Pause eingelegt, um nicht unmenschlich schnell zu sein.
Hat er das Bild nicht gefunden, passiert erst einmal nichts.
Wenn nichts Weiteres im Playset zu finden ist, wird dieser eine Befehl immer wieder ausgeführt, so lange man den Bot laufen lässt.

## Image Recognition Algorythm - IRA

Hier verwenden wir das Prinzip des Template Matching. 
Bei diesem Verfahren wird ein kleines Teilbild (das zu findende Bild) über das gesamte Bild geschoben,
und für jede Position wird die Ähnlichkeit zwischen dem Teilbild und dem Ausschnitt des Bildes berechnet.
Dies geschieht in der Regel durch Methoden wie die Kreuzkorrelation. 
Der Ausschnitt mit der höchsten Übereinstimmung wird dann als das Zielbild erkannt.

## Erweiterte Logik

Ein komplexerer Ablauf ist, wenn man die sogenannten Actionsets verwendet möglich. 
Solche geben ein Teil Playset wieder, welche jedoch bedingt ausgeführt werden können.
Das heißt, ich bin in einem Untermenü des Programms, das erkennt man anhand mehrerer Indikatoren wie:
- andere Titelleiste
- Option zum Schließen des Fensters
- bestimmtes Bild im Hintergrund

Jetzt wird durch die mehreren Konditionen ein Actionset getriggert, welches z. B. ein Gebäude an einem Platz errichten soll.
Während das Actionset ausgeführt wird, werden die anderen Aktionen pausiert, um Missinterpretationen zu vermeiden.
Ist das Actionset durchgelaufen, wird zurück ins Playset gesprungen und weiter bearbeitet.

