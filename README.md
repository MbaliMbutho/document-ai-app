# 📄 Document AI Analyzer (FastAPI)

This project is a simple **FastAPI-based text analysis API** that performs:
- 🧠 Sentiment analysis using Hugging Face Transformers (`bert-base-uncased`)
- 🏷️ Named Entity Recognition (NER) using spaCy
- 📤 File upload endpoint supporting `.txt` and `.csv` inputs

---

## 🚀 Features

- `POST /analyze/`: Upload a `.txt` or `.csv` file and get:
  - Sentiment prediction (`positive` or `negative`)
  - Extracted named entities (person, organization, date, etc.)

---

## 📁 Project Structure

document-ai-app/
│
├── app.py # Main FastAPI application
├── insight_extractor.py # (Optional) Future functionality or helper logic
├── summarizer.py # (Optional) Custom summarization or analysis tools
├── requirements.txt # Python dependencies
└── pycache/ # Python cache files


---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Tiyani33/document-ai-app.git
cd document-ai-app


2. Create a virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate  # On Windows


3. Install dependencies:

pip install -r requirements.txt
python -m spacy download en_core_web_sm

4. ▶️ Running the App
Run the Streamlit app:
streamlit run app.py

📜 License
This project is licensed under the MIT License.





