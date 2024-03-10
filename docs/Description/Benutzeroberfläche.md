# Benutzeroberfläche

Unsere App verfügt über eine Vielzahl von Funktionen, die es dem Benutzer ermöglichen, den Bot zu starten, neue Bilder zu erstellen. Zudem können Action- und Playsets erstelt und bearbeitet weden. Diese Funktionen wurden mit Hilfe des PyQt5-Pakets implementiert.

Besonders leicht ist der PyQt Designer der für die benutzerfreundliche Erstellung der GUI genutzt wurde. Dieses Tool ist Teil des PyQt5-Moduls. Es ermöglicht die Entwicklung der Benutzeroberfläche visuell. Anschließend werden nur noch die Methoden in Python entwickelt. Dadurch wird die Entwicklung ansprechender und funktionaler Benutzeroberflächen erleichtert und beschleunigt, ohne dabei auf Flexibilität und Anpassbarkeit zu verlieren.

## Hauptmenü

Das Hauptmenü besteht im Grunde aus nur zwei Buttons: dem 'Load Game' und 'Start/Stop'. Der 'Load Game'-Button öffnet einen Dateiauswahldialog, über den das zu spielende Spiel ausgewählt wird. Nach der Auswahl des Spiels erfolgt die Auswahl des Spielfelds. Anschließend kann der Bot mit dem 'Start/Stop'-Button gestartet werden.

## Screenshot-Tool

Im Create-Menü wird ebenfalls ein Dateiauswahldialog verwendet, jedoch mit einem zusätzlichen Button für die Auswahl des Spielfeldes, der gleichzeitig die ausgewählte Größe anzeigt. Nach Abschluss dieser beiden Aktionen wird der 'Take Screenshot'-Button freigegeben, der ähnlich wie die Auswahl des Spielfeldes funktioniert. Sobald ein Bild erstellt wurde, wird es darunter angezeigt, um sicherzustellen, dass es den Anforderungen entspricht. Anschließend kann der Name in ein Namensfeld eingegeben und mit dem 'Save'-Button gesichert werden. Wenn ein Fehler auftritt, gibt der Button selbst eine Rückmeldung.

## Playset-Builder 



Im Builder-Menü werden alle Action- und Playsets geladen und können dort bearbeitet oder neue erstellt werden. Vor dem Anzeigen eines Sets muss erneut über einen Dateiauswahldialog das Spiel gewählt werden. Auf der linken Seite befindet sich eine Box, in der die Sets angezeigt werden. Oberhalb dieser Box befindet sich eine Dropdown-Liste, aus der ausgewählt wird, welches Set gerade in der Box angezeigt werden soll.

In der Mitte und auf der rechten Seite befindet sich jeweils eine weitere Boxen. Die mittlere enthält alle Funktionen und erstellt Actionsets, während die rechte Box alle verfügbaren Bilder enthält. Unterhalb dieser beiden Boxen befindet sich eine Textbox mit einem zugehörigen Button zum Hinzufügen von weiteren Elementen.

Im Dropdown-Menü gibt es zudem die Möglichkeit, neue Actionsets zu erstellen. Dafür erscheint ein Textfeld, in das der Name des neuen Actionsets eingegeben und anschließend gespeichert wird.

Die einzelnen Objekte können per Drag-and-Drop in die linke Box eingefügt werden. Zum Entfernen wird ein Element ausgewählt und per 'Entf'-Taste gelöscht. Mit dem 'Save'-Button werden alle Änderungen gespeichert.
