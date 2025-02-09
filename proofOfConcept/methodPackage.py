# worked 

import ollama

client = ollama.Client()

model= "llama3.2:1b" 
prompt = "What is Python?"

response = client.generate(model=model, prompt=prompt)
print(response.response)