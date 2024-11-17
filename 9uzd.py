from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

input_text = "Reiz kādā tālā zemē..."

input_ids = tokenizer.encode(input_text, return_tensors="pt")

output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7, top_k=50, top_p=0.95)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)
