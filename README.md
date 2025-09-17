# Flask Blog Application

Eine einfache Blog-Anwendung mit Flask, die grundlegende CRUD-Funktionalitäten unterstützt.

## Funktionen

1. Beiträge anzeigen

    - Alle Blog-Beiträge werden auf der Startseite angezeigt.

    - Jeder Beitrag zeigt Autor, Titel, Inhalt und Anzahl der Likes an.

2. Beiträge hinzufügen

    - Neue Blog-Beiträge können über ein Formular erstellt werden.

    - Jeder Beitrag enthält Autor, Titel und Inhalt.

    - Beiträge werden in einer JSON-Datei gespeichert.

3. Beiträge löschen

    - Ein vorhandener Beitrag kann über seine eindeutige ID gelöscht werden.

    - Änderungen werden automatisch in der JSON-Datei gespeichert.

4. Beiträge aktualisieren

    - Bestehende Beiträge können bearbeitet werden (Titel, Autor, Inhalt).

    - Die JSON-Datei wird nach der Aktualisierung angepasst.

5. Beiträge liken

    - Jeder Beitrag kann "geliked" werden.

    - Die Anzahl der Likes wird ebenfalls in der JSON-Datei gespeichert.

## Installation

1. Repository klonen:
    ```bash
    git clone <REPO_URL>
    cd <REPO_NAME>


2. Virtuelle Umgebung erstellen und aktivieren:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux / Mac
    venv\Scripts\activate      # Windows


3. Flask installieren:
    ```bash
    pip install flask


4. Anwendung starten:
    ```bash
    python app.py


5. Im Browser öffnen:
    ```bash
    http://127.0.0.1:5000

## Datenstruktur

Die Blog-Beiträge werden in einer JSON-Datei (posts.json) gespeichert:
    
    [
        {"id": 1, "author": "John Doe", "title": "First Post", "content": "This is my first post.", "likes": 0},
        {"id": 2, "author": "Jane Doe", "title": "Second Post", "content": "This is another post.", "likes": 0}
    ]


## Jeder Beitrag enthält:

  - id → eindeutige Kennung des Beitrags

  - author → Name des Autors

  - title → Titel des Beitrags

  - content → Inhalt des Beitrags

  - likes → Anzahl der Likes
