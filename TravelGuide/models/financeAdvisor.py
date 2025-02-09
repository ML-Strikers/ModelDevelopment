
from imports import *


client = ollama.Client()

# connect to db for the following
user_input = None
place_visit = None

model = "financeAdvisior"


prompt = f"""

You are a financial consultant
User asks: {user_input}
How shall the user be advised to plan their visit to {place_visit}?

"""

response = client.generate(model=model, prompt=prompt)  

response = client.generate(model=model, prompt=prompt)
(response.response)