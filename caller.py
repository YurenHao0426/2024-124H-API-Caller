import openai
import re
import yaml

# Load API key from yaml file
with open('api-key.yaml', 'r') as file:
    config = yaml.safe_load(file)
    api_key = config['openai']['api_key']

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

def extract_meeting_details(long_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that extracts meeting details from text. You must respond in a specific format that can be parsed as YAML."},
            {"role": "user", "content": f"""Please extract all mentioned meetings from the following text and format the response as YAML:

{long_text}

Format the response as:
meetings:
  - time: "YYYY-MM-DD HH:MM - HH:MM"
    location: "location name"
    description: "event description"
    title: "meeting title"
  - time: "YYYY-MM-DD HH:MM - HH:MM"
    location: "location name"
    description: "event description"
    title: "meeting title"

If no meetings are found, respond with:
meetings: null"""}
        ],
        max_tokens=1500,
        temperature=0.2
    )
    
    try:
        result = yaml.safe_load(response.choices[0].message.content)
        return result
    except yaml.YAMLError:
        return {"meetings": None}