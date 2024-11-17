import re
from collections import Counter

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

words = re.findall(r'\w+', text.lower())

word_counts = Counter(words)

print("Vārdu biežums tekstā:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
