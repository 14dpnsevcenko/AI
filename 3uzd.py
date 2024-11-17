import re

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

def extract_words(text):
    return set(re.findall(r'\w+', text.lower()))

words1 = extract_words(text1)
words2 = extract_words(text2)

common_words = words1 & words2

all_words = words1 | words2

similarity_percentage = len(common_words) / len(all_words) * 100

print("Sakrītošie vārdi:", common_words)
print(f"Sakritības līmenis: {similarity_percentage:.2f}%")
