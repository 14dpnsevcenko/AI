import re

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

def clean_text(text):
    text = re.sub(r'http\S+|www\S+', '', text)  
    text = re.sub(r'[@#]', '', text) 
    text = re.sub(r'[^a-zA-ZāčēģīķļņóšūžĀČĒĢĪĶĻŅŌŠŪŽ\s]', '', text)  
    text = re.sub(r'\s+', ' ', text)  
    text = text.lower()  
    return text.strip()  

cleaned_text = clean_text(raw_text)

print(f"Tīrais teksts: '{cleaned_text}'")
