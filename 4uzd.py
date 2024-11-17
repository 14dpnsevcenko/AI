from deep_translator import GoogleTranslator
from textblob import TextBlob

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

def analyze_sentiment(sentence):
    translated_text = GoogleTranslator(source='lv', target='en').translate(sentence)
    
    blob = TextBlob(translated_text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        return "Pozitīvs"
    elif polarity < 0:
        return "Negatīvs"
    else:
        return "Neitrāls"

for sentence in sentences:
    sentiment = analyze_sentiment(sentence)
    print(f"Teikums: '{sentence}' -> Noskaņojums: {sentiment}")
