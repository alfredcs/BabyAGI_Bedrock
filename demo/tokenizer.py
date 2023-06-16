from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

token_subdirectory="tokens/"
tokenizer.save_vocabulary(token_subdirectory)
x=tokenizer("Who is behind the resecue plan of SVB's failur ein early 2023?")['input_ids']
print(x)
