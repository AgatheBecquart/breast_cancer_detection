import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os

st.set_page_config(page_title="Détection de tumeurs avec l'IA", page_icon=":camera:", layout="wide")

st.title("Détection de tumeurs avec l'IA")

col1, col2 = st.columns(2)

with col1:
    st.header("Téléchargez une image")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    first_name = st.text_input("Prénom")
    last_name = st.text_input("Nom")

with col2:
    st.header("Résultats")
    if uploaded_file is not None:
        model = YOLO('best.pt')
        image = Image.open(uploaded_file)
        results = model.predict(image)
        result_image = results[0].plot()
        st.image(result_image)

        # Ask the user if they want to save the predictions
        save_predictions = st.checkbox("Enregistrer les résultats")

        # Save the image and user information if the user wants to and has entered their name and last name
        if save_predictions and first_name and last_name:
            save_dir = "images_enregistrées"
            os.makedirs(save_dir, exist_ok=True)
            result_pil_image = Image.fromarray(result_image)

            # Check if the file already exists
            save_path = os.path.join(save_dir, f"{first_name}_{last_name}.jpg")
            if os.path.exists(save_path):
                # Ask the user if they want to add a number to their name
                add_number = st.checkbox("Ce nom et prénom existent déjà. Voulez-vous ajouter un chiffre à votre nom?")
                if add_number:
                    # Find the next available number to add to the file name
                    i = 1
                    while os.path.exists(os.path.join(save_dir, f"{first_name}_{last_name}_{i}.jpg")):
                        i += 1
                    save_path = os.path.join(save_dir, f"{first_name}_{last_name}_{i}.jpg")

            result_pil_image.save(save_path)

# Create a selectbox to select a saved prediction
save_dir = "images_enregistrées"
saved_files = sorted(os.listdir(save_dir))
selected_file = st.selectbox("Sélectionnez une prédiction enregistrée", [""] + saved_files)

# Display the selected prediction
if selected_file:
    image = Image.open(os.path.join(save_dir, selected_file))
    st.image(image, caption=selected_file)
