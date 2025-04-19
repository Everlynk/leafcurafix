import streamlit as st
from PIL import Image
import io
import os

# Optional für HEIC
try:
    import pyheif
except ImportError:
    pyheif = None

from fpdf import FPDF

# Seiteneinstellungen
st.set_page_config(
    page_title="Leafcura",
    page_icon="leafcurafix_favicon_512x512.png",
    layout="centered"
)

# Logo anzeigen
if os.path.exists("leafcura_logo.png"):
    logo = Image.open("leafcura_logo.png")
    st.image(logo, width=200)

# Sprache wählen
lang = st.sidebar.radio("Sprache / Language", ("Deutsch", "English"))

# Texte je nach Sprache
if lang == "Deutsch":
    st.title("LeafcuraFix – Blattdiagnose & Hausmittel")
    upload_label = "📷 Lade ein Bild deines Pflanzenblatts hoch:"
    analysing = "🔍 Analyse läuft..."
    diagnosis = "Diagnose: Stickstoffmangel"
    symptoms = "**Symptome:** Vergilbung älterer Blätter, verlangsamtes Wachstum"
    remedies = "**Hausmittel:**\n- Kaffeesatz ins Substrat\n- Brennnesseljauche\n- pH-Wert zwischen 6.0–6.5 halten"
    download_button_label = "📄 Diagnosebericht als PDF herunterladen"
else:
    st.title("LeafcuraFix – Leaf Diagnosis & Natural Remedies")
    upload_label = "📷 Upload a photo of your plant leaf:"
    analysing = "🔍 Analyzing..."
    diagnosis = "Diagnosis: Nitrogen Deficiency"
    symptoms = "**Symptoms:** Yellowing of older leaves, slowed growth"
    remedies = "**Home Remedies:**\n- Add used coffee grounds\n- Use nettle tea\n- Maintain pH between 6.0–6.5"
    download_button_label = "📄 Download diagnosis report as PDF"

# Datei-Upload
uploaded_file = st.file_uploader(upload_label, type=["jpg", "jpeg", "png", "heic"])

image = None
if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1].lower()
    if file_ext == "heic" and pyheif:
        heif_file = pyheif.read(uploaded_file.read())
        image = Image.frombytes(
            heif_file.mode, heif_file.size, heif_file.data, "raw", heif_file.mode, heif_file.stride
        )
    else:
        try:
            image = Image.open(uploaded_file)
        except Exception as e:
            st.error("❌ Bild konnte nicht geöffnet werden.")

    if image:
        st.image(image, caption="📸 Vorschau", use_container_width=True)
        st.write(analysing)

        # Diagnose-Anzeige
        st.subheader(diagnosis)
        st.markdown(symptoms)
        st.markdown(remedies)

        # PDF generieren
        def generate_pdf():
            pdf = FPDF()
            pdf.add_page()
            font_path = os.path.join(os.getcwd(), "DejaVuSans.ttf")
            pdf.add_font("DejaVu", "", font_path, uni=True)
            pdf.set_font("DejaVu", size=14)

            pdf.cell(0, 10, "LeafcuraFix Diagnosebericht", ln=True, align="C")
            pdf.ln(10)

            pdf.set_font("DejaVu", "B", 12)
            pdf.cell(0, 10, "Diagnose", ln=True)
            pdf.set_font("DejaVu", "", 12)
            pdf.multi_cell(0, 10, diagnosis.replace("Diagnose: ", "").replace("Diagnosis: ", ""))
            pdf.ln(5)

            pdf.set_font("DejaVu", "B", 12)
            pdf.cell(0, 10, "Symptome / Symptoms", ln=True)
            pdf.set_font("DejaVu", "", 12)
            pdf.multi_cell(0, 10, symptoms.replace("**Symptome:**", "").replace("**Symptoms:**", "").strip())
            pdf.ln(5)

            pdf.set_font("DejaVu", "B", 12)
            pdf.cell(0, 10, "Hausmittel / Remedies", ln=True)
            pdf.set_font("DejaVu", "", 12)
            pdf.multi_cell(0, 10, remedies.replace("**Hausmittel:**", "").replace("**Home Remedies:**", "").strip())

            # PDF korrekt streamen
            buffer = io.BytesIO()
            pdf.output(buffer)
            buffer.seek(0)
            return buffer

        # PDF Download-Button
        pdf_file = generate_pdf()
        st.download_button(
            label=download_button_label,
            data=pdf_file,
            file_name="leafcura_diagnose.pdf",
            mime="application/pdf"
        )
