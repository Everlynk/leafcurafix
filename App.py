import streamlit as st
from PIL import Image, UnidentifiedImageError
import io
import pyheif

# Seitenlayout & Icon
st.set_page_config(
    page_title="Leafcura",
    page_icon="leafcurafix_favicon_512x512.png",
    layout="centered"
)

# Logo
logo = Image.open("leafcura_logo.png")
st.image(logo, width=200)

# Sprache auswählen
lang = st.sidebar.radio("Sprache / Language", ("Deutsch", "English"))

# Sprachabhängige Texte
if lang == "Deutsch":
    st.title("LeafcuraFix – Blattdiagnose & Hausmittel")
    upload_label = "📷 Lade ein Bild deines Pflanzenblatts hoch:"
    analyse_button = "🔍 Analyse starten"
    analysing = "Analyse läuft..."
    diagnosis = "Diagnose: Stickstoffmangel"
    symptoms = "**Symptome:** Vergilbung älterer Blätter, verlangsamtes Wachstum"
    remedies = "**Hausmittel:**\n- Kaffeesatz ins Substrat\n- Brennnesseljauche\n- pH-Wert zwischen 6.0–6.5 halten"
    error_text = "❌ Bild konnte nicht geladen werden. Bitte lade ein gültiges JPG, PNG oder HEIC hoch."
else:
    st.title("LeafcuraFix – Leaf Diagnosis & Natural Remedies")
    upload_label = "📷 Upload a photo of your plant leaf:"
    analyse_button = "🔍 Start analysis"
    analysing = "Analyzing..."
    diagnosis = "Diagnosis: Nitrogen Deficiency"
    symptoms = "**Symptoms:** Yellowing of older leaves, slowed growth"
    remedies = "**Remedies:**\n- Coffee grounds\n- Nettle tea\n- Maintain pH between 6.0–6.5"
    error_text = "❌ Could not load image. Please upload a valid JPG, PNG, or HEIC file."

# Bild hochladen
uploaded_file = st.file_uploader(upload_label, type=["jpg", "jpeg", "png", "heic"])

if uploaded_file:
    try:
        # HEIC-Bilder erkennen und konvertieren
        if uploaded_file.name.lower().endswith(".heic"):
            heif_file = pyheif.read(uploaded_file.read())
            image = Image.frombytes(
                heif_file.mode, heif_file.size, heif_file.data,
                "raw", heif_file.mode, heif_file.stride
            )
        else:
            image = Image.open(uploaded_file)

        # Anzeige
        st.image(image, caption="Preview", use_container_width=True)

        # JPG-Export vorbereiten (auch bei HEIC)
        buffer = io.BytesIO()
        image.convert("RGB").save(buffer, format="JPEG")
        buffer.seek(0)

        # Download-Button
        st.download_button(
            label="📥 Konvertiertes Bild herunterladen (JPG)",
            data=buffer,
            file_name="leafcura_upload.jpg",
            mime="image/jpeg"
        )

        # Analyse-Button
        if st.button(analyse_button):
            st.write(analysing)
            st.subheader(diagnosis)
            st.markdown(symptoms)
            st.markdown(remedies)

    except UnidentifiedImageError:
        st.error(error_text)
    except Exception as e:
        st.error(f"⚠️ Fehler beim Verarbeiten der Datei: {e}")
