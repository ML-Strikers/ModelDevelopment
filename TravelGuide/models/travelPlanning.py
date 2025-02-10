
# from imports import *

import ollama

client = ollama.Client()

# connect to db for the following
user_input = None
place_visit = None

model = "travelPlanner:latest"


prompt = f"""
plan me a trip to LA for 5 days
"""

response = client.generate(model=model, prompt=prompt)  
print(response.response)