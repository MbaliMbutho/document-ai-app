import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def extract_insights(text):
    doc = nlp(text)
    people = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
    tasks = [sent.text for sent in doc.sents if "should" in sent.text.lower() or "must" in sent.text.lower()]
    return {
        "People Mentioned": Counter(people).most_common(5),
        "Dates": Counter(dates).most_common(5),
        "Action Points": tasks[:5]
    }
