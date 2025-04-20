import openai
import streamlit as st

def ask_gpt(diagnose_text: str) -> str:
    try:
        openai.api_key = st.secrets["OPENAI_API_KEY"]

        prompt = (
            f"Ich habe an meiner Pflanze folgendes festgestellt: {diagnose_text}. "
            "Welche natürlichen Hausmittel helfen dagegen? Erkläre es einfach."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du bist ein Pflanzenexperte, der hilfreiche Ratschläge gibt."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ GPT-Fehler: {str(e)}"
