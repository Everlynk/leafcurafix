import openai
import streamlit as st

# OpenAI-Client initialisieren mit Secret aus Streamlit
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def ask_gpt(diagnose_text: str) -> str:
    # Prompt für ChatGPT vorbereiten
    prompt = (
        f"Ich habe an meiner Pflanze folgendes festgestellt: {diagnose_text}. "
        "Welche natürlichen Hausmittel helfen dagegen? Erkläre es einfach."
    )

    # Chat-Vervollständigung abfragen (neue API)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Du bist ein Pflanzenexperte, der hilfreiche Ratschläge gibt."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
