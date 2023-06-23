import sqlite3

def create_prediction(first_name: str, last_name: str, image_path: str) -> None:
    """
    Crée une nouvelle prédiction dans la base de données.

    Args:
        first_name (str): Le prénom de l'utilisateur.
        last_name (str): Le nom de l'utilisateur.
        image_path (str): Le chemin de l'image enregistrée.

    Returns:
        None
    """
    connexion = sqlite3.connect("detection.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO prediction (first_name, last_name, image_path) VALUES (?, ?, ?)", (first_name, last_name, image_path))
    connexion.commit()
    connexion.close()

def read_prediction(first_name: str, last_name: str) -> None:
    """
    Lit les informations d'une prédiction enregistrée dans la base de données.

    Args:
        first_name (str): Le prénom de l'utilisateur.
        last_name (str): Le nom de l'utilisateur.

    Returns:
        Un dictionnaire contenant les informations de la prédiction trouvée, ou None si aucune prédiction n'a été trouvée.
    """
    connexion = sqlite3.connect("detection.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM prediction WHERE first_name = ? AND last_name = ?", (first_name, last_name))
    res = curseur.fetchone()
    connexion.close()

    if not res:
        return None

    return {"first_name": res[1], "last_name": res[2], "image_path": res[3]}

def update_prediction(first_name: str, last_name: str, new_image_path: str) -> None:
    """
    Met à jour les informations d'une prédiction enregistrée dans la base de données.

    Args:
        first_name (str): Le prénom de l'utilisateur.
        last_name (str): Le nom de l'utilisateur.
        new_image_path (str): Le nouveau chemin de l'image enregistrée.

    Returns:
        None
    """
    connexion = sqlite3.connect("detection.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE prediction SET image_path = ? WHERE first_name = ? AND last_name = ?", (new_image_path, first_name, last_name))
    connexion.commit()
    connexion.close()

def delete_prediction(first_name: str, last_name: str) -> None:
    """
    Supprime une prédiction enregistrée dans la base de données.

    Args:
        first_name (str): Le prénom de l'utilisateur.
        last_name (str): Le nom de l'utilisateur.

    Returns:
        None
    """
    connexion = sqlite3.connect("detection.db")
    curseur = connexion.cursor()
