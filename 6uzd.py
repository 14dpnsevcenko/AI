from sumy.parsers.plaintext import PlaintextParser
from sumy.tokenizers import Tokenizer  
from sumy.summarizers.text_rank import TextRankSummarizer  

article = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. 
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

parser = PlaintextParser.from_string(article, Tokenizer())

def summarize_text(text, num_sentences=2):
    summarizer = TextRankSummarizer()  
    summary = summarizer(parser.document, num_sentences)
    return ' '.join(str(sentence) for sentence in summary)


summary = summarize_text(article, 2) 
print("Rezultāts:\n", summary)
