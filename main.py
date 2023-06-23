from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import sqlite3

app = FastAPI(openapi_url="/openapi.json", docs_url="/")

class Prediction(BaseModel):
    first_name: str
    last_name: str
    image_path: str

@app.post("/prediction/")
async def save_prediction(prediction: Prediction):
    # Save the prediction to the database
    connexion = sqlite3.connect("detection.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO prediction (first_name, last_name, image_path) VALUES (?, ?, ?)", (prediction.first_name, prediction.last_name, prediction.image_path))
    connexion.commit()
    connexion.close()

    return {"message": "Prédiction enregistrée avec succès"}

@app.get("/prediction/")
async def read_prediction(first_name: str, last_name: str):
    # Connect to the database
    connexion = sqlite3.connect("detection.db")
    curseur = connexion.cursor()

    # Query the database for the prediction
    curseur.execute("SELECT * FROM prediction WHERE first_name = ? AND last_name = ?", (first_name, last_name))
    res = curseur.fetchone()
    connexion.close()

    # Check if the prediction was found
    if not res:
        return {"message": "Prédiction non trouvée"}

    # Return the prediction information
    return {"first_name": res[1], "last_name": res[2], "image_path": res[3]}
