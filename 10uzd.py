from deep_translator import GoogleTranslator

texts_lv = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

translations = [GoogleTranslator(source='lv', target='en').translate(text) for text in texts_lv]

print("Tulkojumi angļu valodā:")
for i, translation in enumerate(translations, start=1):
    print(f"{i}. {translation}")
