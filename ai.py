import openai
from config import apikey
openai.api_key = apikey
openai.api_base = 'https://api.pawan.krd/v1'

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Human: how are you?\nAI:",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["Human: ", "AI: "]
)

print(response.choices[0].text)