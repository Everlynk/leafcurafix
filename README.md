# 🌿 LeafcuraFix

**Diagnose in Sekunden. Heilung mit Hausmitteln.**

LeafcuraFix ist deine smarte WebApp zur Pflanzenpflege.  
Lade ein Foto vom Blatt deiner Pflanze hoch – die App erkennt typische Mängel oder Krankheiten und zeigt dir sofort natürliche Lösungen, die du mit einfachen Hausmitteln umsetzen kannst.

[![Streamlit App](https://img.shields.io/badge/LeafcuraFix%20Live%20App-🌐-blue?logo=streamlit)](https://leafcurafix.streamlit.app)  
[![Built with Streamlit](https://img.shields.io/badge/built%20with-Streamlit-orange?logo=streamlit)](https://streamlit.io)  
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✅ Features

- 🌱 Funktioniert mit gängigen Pflanzen (z. B. *Cannabis*, *Tomate*, *Basilikum*)
- 🧠 Sofort-Diagnose per KI (aktuell simuliert)
- 🧪 Hausmittel-Vorschläge (z. B. Kaffeesatz, Essig, Backpulver)
- 🌐 Zweisprachig: Deutsch & Englisch
- 📱 Mobilfreundlich (auch für iPhone)
- 🖼️ HEIC-Support für iOS-Uploads
- 📄 PDF-Export mit Diagnose & Bild

**Ohne Chemie. Ohne Rätselraten. Einfach helfen – Blatt für Blatt.**

---

## 🚀 Lokale Installation

```bash
git clone https://github.com/everlynk/leafcurafix.git
cd leafcurafix
pip install -r requirements.txt
streamlit run App.py
```

---

## ☁️ Deployment via Streamlit Cloud

1. Forke dieses Repository oder lade es auf GitHub hoch  
2. Öffne [Streamlit Cloud](https://streamlit.io/cloud)  
3. Erstelle eine neue App und gib als Hauptdatei `App.py` an

---

## 🤝 Beitrag leisten (Contributing)

Du hast Ideen, willst etwas verbessern oder neue Pflanzen hinzufügen?  
Super! Forke das Repo, erstelle einen Branch und schicke gerne einen Pull Request.

Oder öffne ein [Issue](https://github.com/everlynk/leafcurafix/issues) mit deinem Vorschlag, Feedback oder Bug-Report 💡

---

## 🧰 Technologie-Stack

| Tool       | Zweck                         |
|------------|-------------------------------|
| [Streamlit](https://streamlit.io)          | Web-App Frontend           |
| [Pillow](https://python-pillow.org/)       | Bildverarbeitung           |
| [pyheif](https://pypi.org/project/pyheif/) | HEIC-Unterstützung         |
| [fpdf](https://py-pdf.github.io/fpdf2/)    | PDF-Erstellung             |
| Python 3.11                                | Programmiersprache         |

---

## 🖼️ Screenshots

**Startseite mit Upload:**  
<img src="leafcura_screenshot1.png" alt="Startansicht" width="600"/>

**Analyse-Ergebnis mit Download:**  
<img src="leafcura_screenshot2.png" alt="Analyse" width="600"/>

> *(Speichere deine Screenshots im Projektordner – als `leafcura_screenshot1.png`, `leafcura_screenshot2.png`)*

---

### 📄 Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](./Licence) – frei nutzbar und anpassbar.  
Keine Gewährleistung – Nutzung auf eigene Verantwortung.
