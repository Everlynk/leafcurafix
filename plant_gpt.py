import streamlit as st
from openai import OpenAI

def ask_gpt(diagnose_text: str) -> str:
    try:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        prompt = (
            f"Ich habe an meiner Pflanze folgendes festgestellt: {diagnose_text}. "
            f"Welche natürlichen Hausmittel helfen dagegen? Erkläre es einfach."
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du bist ein Pflanzenexperte, der hilfreiche Ratschläge gibt."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ GPT-Fehler: {e}"
