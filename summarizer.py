from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    results = summarizer(chunks, max_length=130, min_length=30, do_sample=False)
    return ' '.join([res['summary_text'] for res in results])
