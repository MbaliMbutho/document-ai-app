import streamlit as st
import pdfplumber
import docx
import io
import json
from summarizer import summarize_text
from insight_extractor import extract_insights

def extract_text(file):
    if file.name.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            return '\n'.join(page.extract_text() or '' for page in pdf.pages)
    elif file.name.endswith('.docx'):
        doc = docx.Document(file)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif file.name.endswith('.txt'):
        return file.read().decode()
    else:
        return "Unsupported file type."

st.set_page_config(page_title="AI Document Summarizer", layout="wide")
st.title("📄 AI Document Summarizer & Insight Extractor")

uploaded_file = st.file_uploader("Upload a PDF, Word (.docx), or Text file", type=["pdf", "docx", "txt"])

if uploaded_file:
    with st.spinner("Extracting document text..."):
        text = extract_text(uploaded_file)

    if text:
        st.subheader("📄 Original Document Text")
        with st.expander("Click to preview full text"):
            st.text_area("Document Text", text, height=400)

        if st.button("🔍 Generate Summary & Insights"):
            with st.spinner("Running AI models..."):
                summary = summarize_text(text)
                insights = extract_insights(text)

            st.subheader("🧠 Summary")
            st.write(summary)

            # Download summary button
            summary_bytes = summary.encode('utf-8')
            summary_buffer = io.BytesIO(summary_bytes)

            st.download_button(
                label="💾 Download Summary as TXT",
                data=summary_buffer,
                file_name="summary.txt",
                mime="text/plain"
            )

            st.subheader("🔑 Insights")
            st.write("**People Mentioned:**", insights["People Mentioned"])
            st.write("**Dates:**", insights["Dates"])
            st.write("**Action Points:**")
            for task in insights["Action Points"]:
                st.write(f"- {task}")

            # Download insights button
            insights_str = json.dumps(insights, indent=2)
            insights_bytes = insights_str.encode('utf-8')
            insights_buffer = io.BytesIO(insights_bytes)

            st.download_button(
                label="💾 Download Insights as JSON",
                data=insights_buffer,
                file_name="insights.json",
                mime="application/json"
            )
    else:
        st.error("❌ Could not extract text from the uploaded file.")

