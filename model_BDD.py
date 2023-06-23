import sqlite3

connexion = sqlite3.connect("detection.db")
curseur = connexion.cursor()

curseur.execute("""
    CREATE TABLE IF NOT EXISTS prediction(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        image_path TEXT NOT NULL
    )
""")

connexion.commit()
connexion.close()
