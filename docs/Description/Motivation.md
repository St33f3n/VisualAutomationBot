# Motivation

## Warum baut man so etwas?

Ursprünglicher Anreiz dazu war ein Freund, der auf seinem Handy mithilfe verschiedener Apps, für das Spielen von Handyspielen Geld bekommt.
Nun hatte ich jedoch eher wenig Lust, Spiele mit eher minderer Qualität und fragwürdigem Datenschutz auf meinem privaten Gerät zu installieren und 
dann auch noch die Zeit zu investieren, die benötigt worden wäre, um die durch die Apps vorgegeben Level zu erreichen.

## Was benötigt man dafür?
Um die ersten zwei Probleme zu lösen, gabs bereits vorhandene Software, die das ganze auf einen PC emuliert. Wir haben der Einfachheit halber als
Android Emulator BlueStacks verwendet.
Gute Performance und einfache Verwendung.
Um jetzt noch seine wertvolle Zeit zu sparen und eigentlich Dinge zu erledigen, die man lieber macht, haben wir uns dazu entschlossen - wie jeder Programmierer, ob jetzt angeheder oder Senior - das dass automatisiert werden muss.

### Die Programmiersprache

Als Programmiersprache ist, bei solchen Aufgeben bei der Berechnungszeit nicht um bedingt eine große Rolle spielt und in Zukunft vielleicht auch mit 
KI erweiterbar ist, Python immer die erste Wahl.
Das hat mehrere Vorteile:
	- Verfügbarkeit von vielen Bilderkennungsbibliotheken
	- Einfacher Zugriff auf Maus und Tastatur
	- Einfache Integration in eine Benutzeroberfläche

### Programmteile

Um nun den Spielen vorzugaukeln, das da jetzt kein Programm läuft, sondern ein echter Spieler, müssen wir die Befehlseingabe genauso wie jeder andere Spieler auch machen - heißt mit Maus/Finger und Tastatur. Für das wurde PyAutoGUI verwendet, genauer gesagt die davon verwendete je nach Betriebssystem hinterlegte Bibliothek.
Genauso müssen wir dafür sorgen, dass wir unregelmäßige Zeitabstände zwischen den einzelnen Eingaben einhalten, um nicht der BotDetection aufzufallen.
Hierfür haben wir einen randomisierten Timer erstellt, der für jede Aktion ein zufälliges Zeitfenster in einem vorher festgelegten Bereich wählt.
Um verschieden Situationen anhand des derzeitigen Monitorbildes zu erkennen, muss noch ein Image Recognition Algorithmus her.
Dabei bietet uns PyAutoGUI schon einige an. Im Hintergrund liegt im Prinzip CV2 eine in C++ geschriebene Bildverarbeitungs-Bibliothek.
Später noch mehr zum IRA. 
Jetzt brauchen wir nur noch die Logik, die dafür sorgt, das zum richtigen Zeitpunkt an die richtige Stelle gedrückt wird.
Da man diese individuell für alle möglichen Anwendungen anpassen muss, wird noch ein permanenter Speicher erforderlich.
Dazu nutzen wir in diesem Fall das Json Format, das in eine lokale Datei speichert. 
Um die Erstellung dieser Logik zu vereinfachen, haben wir ein Benutzerprogramm erstellt, welches die zur Verfügungsstehenden Funktionen optisch darstellt und kombinierbar macht.
Die Funktionen, die zur Verfügung stehen, sind:
- von Bild zu Bild ziehen
- von Bild in eine Richtung wischen
- eine Taste drücken,
- ein Bild klicken, wenn ein Bild vorhanden ist
- eine Befehlskette (im weiteren Actionset genannt) ausführen wenn:
	- Ein bestimmter Wert, der über OCR erfasst wird, erreicht worden ist
	- Ein oder mehrere Bilder am Monitor zu sehen sind

