# JSON - Permanente Daten

## Warum JSON

Wir haben uns für die Verwendung der JavaScript Object Notation (JSON) entschieden, da sie heutzutage zu den etablierten Standards gehört. Ihre Beliebtheit gründet sich auf mehreren Gründen: Zum einen ist sie als Mensch leicht zu lesen und einfach zu erstellen. Dies macht die Arbeit mit ihr besonders angenehm und effizient. Zum anderen ist JSON im Web-Bereich stark vertreten, was sie zur perfekten Wahl für den Austausch von Daten zwischen verschiedenen Systemen macht. 

## JSON Handler Klasse

Die JsonHandler-Klasse bietet eine API zum Umgang mit JSON-Daten in Python-Anwendungen. Sie ermöglicht das einfache Laden vorhandener JSON-Daten aus der config Datei, das Speichern von Änderungen sowie das Erstellen neuer JSON-Strukturen. Die Klasse unterstützt nicht nur die Verwaltung von reinen Daten, sondern ermöglicht auch die Handhabung von komplexen Datenstrukturen wie das speichern und ändern der erstellen Bilder, mithilfe der GUI.

Durch die Integration der GUI lassen sich Bilder zusammen mit ihren Metadaten in das JSON-Format einbinden. Dies umfasst Informationen wie die Bildgröße, den Dateipfad und die Bildschirm- und Fenstergröße, was besonders nützlich ist, um den Bot auf vielen verschieden Geräten mit unterschiedlichen Vorraussetzungen laufen zu lassen. Zudem wird die Speicherung der erstellten Action- und Playsets gehandharbt. 

Darüber hinaus erleichtert die JsonHandler-Klasse die Verwaltung von Ressourcendaten, indem sie eine benutzerfreundliche Schnittstelle zum Erstellen, Aktualisieren und Abrufen von Ressourcen bietet. Dies ist insbesondere nützlich wenn Games mit vielen verschieden Ressourcen gespielt werden.

Insgesamt ermöglicht die JsonHandler-Klasse eine nahtlose Integration von JSON in Python-Anwendungen und bietet eine effiziente, flexible und skalierbare Möglichkeit zur Verwaltung von Daten verschiedener Art. Durch eine kleien änderung unterstützt diese auch das Einlesen mehrere Dateien, was sie besonders flexibel macht.

## Skalierbarkeit in der Zukunft

Durch wenige Anpassungen ist es möglich, die Klasse so zu erweitern, dass sie nicht mehr ausschließlich Daten aus einer Datei liest, sondern auch über eine Web-API abruft. Diese Web-API kann leicht mit Python Flask erstellt und als Backend genutzt werden. Die Daten werden dann in einer Datenbank gespeichert und können über die API abgerufen werden.