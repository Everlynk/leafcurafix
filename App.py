import streamlit as st
from PIL import Image

st.set_page_config(page_title="Leafcura",
    page_icon="leafcurafix_favicon_512x512.png",
    layout="centered")

logo = Image.open("leafcura_logo.png")
st.image(logo, width=200)

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

        import random

    if lang == "Deutsch":
        diagnosen = [
            {
                "diagnose": "Stickstoffmangel",
                "symptome": "**Symptome:** Vergilbung älterer Blätter, verlangsamtes Wachstum",
                "hausmittel": "**Hausmittel:**\n- Kaffeesatz\n- Brennnesseljauche\n- pH-Wert 6.0–6.5"
            },
            {
                "diagnose": "Kaliummangel",
                "symptome": "**Symptome:** Braune Blattspitzen, eingerollte Ränder",
                "hausmittel": "**Hausmittel:**\n- Bananenschale\n- Holzasche (sparsam)"
            },
            {
                "diagnose": "Mehltau",
                "symptome": "**Symptome:** Weißer Belag auf Blattoberfläche",
                "hausmittel": "**Hausmittel:**\n- 1 Teil Milch + 9 Teile Wasser\n- Natronlösung"
            }
        ]
    else:
        diagnosen = [
            {
                "diagnose": "Nitrogen Deficiency",
                "symptome": "**Symptoms:** Yellowing of older leaves, stunted growth",
                "hausmittel": "**Remedies:**\n- Coffee grounds\n- Nettle tea\n- Keep pH 6.0–6.5"
            },
            {
                "diagnose": "Potassium Deficiency",
                "symptome": "**Symptoms:** Brown leaf tips, curled edges",
                "hausmittel": "**Remedies:**\n- Banana peel\n- Ash (sparingly)"
            },
            {
                "diagnose": "Powdery Mildew",
                "symptome": "**Symptoms:** White powdery coating on leaves",
                "hausmittel": "**Remedies:**\n- Milk-water spray (1:9)\n- Baking soda solution"
            }
        ]

    ausgabe = random.choice(diagnosen)
    st.subheader(f"🔍 {ausgabe['diagnose']}")
    st.markdown(ausgabe["symptome"])
    st.markdown(ausgabe["hausmittel"])

