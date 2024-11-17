import langid

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

for text in texts:
    language, confidence = langid.classify(text)
    print(f"Teksts: '{text}' -> Valoda: {language} (Pārliecība: {confidence:.2f})")
