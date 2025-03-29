import streamlit as st
from PIL import Image
import numpy as np

# Sprachwahl
lang = st.sidebar.radio("Sprache / Language", ("Deutsch", "English"))

# Titel und Texte
if lang == "Deutsch":
    st.title("LeafcuraFix – Blattdiagnose & Hausmittel")
    upload_label = "Lade ein Bild deines Pflanzenblatts hoch:"
    analysing = "Analyse läuft..."
    diagnosis = "Diagnose: Stickstoffmangel"
    symptoms = "**Symptome:** Vergilbung älterer Blätter, verlangsamtes Wachstum"
    remedies = "**Hausmittel:**\n- Kaffeesatz ins Substrat\n- Brennnesseljauche\n- pH-Wert zwischen 6.0–6.5 halten"
else:
    st.title("LeafcuraFix – Leaf Diagnosis & Natural Remedies")
    upload_label = "Upload a photo of your plant leaf:"
    analysing = "Analyzing..."
    diagnosis = "Diagnosis: Nitrogen Deficiency"
    symptoms = "**Symptoms:** Yellowing of older leaves, slowed growth"
    remedies = "**Home Remedies:**\n- Add used coffee grounds\n- Use nettle tea\n- Maintain pH between 6.0–6.5"

# Datei-Upload
uploaded_file = st.file_uploader(upload_label, type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Preview", use_column_width=True)
    st.write(analysing)

    # Demo-Ausgabe (Platzhalter für KI)
    st.subheader(diagnosis)
    st.markdown(symptoms)
    st.markdown(remedies)
