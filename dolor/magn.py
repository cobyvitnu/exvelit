input_text = "This is a sample text."
input_ids = tokenizer.encode(input_text, return_tensors="pt")
attention_mask = tokenizer.encode(input_text, return_tensors="pt", max_length=512, padding="max_length", truncation=True)
outputs = model(input_ids, attention_mask=attention_mask)
logits = outputs.logits
predicted_class = torch.argmax(logits)
print(predicted_class)
