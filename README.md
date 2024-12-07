# Meeting Extractor

This is a simple script that extracts meeting details from an email. It uses the OpenAI API to extract the meeting details from the email content.

## Installation

1. Clone the repository
2. Install the dependencies
```
pip install openai
pip install pyyaml
```
3. Set the OpenAI API key in the `api-key.yaml` file
4. Run the script

## Open-ai API Key

You can get the OpenAI API key from [here](https://platform.openai.com/api-keys).
A valid API key starts with `sk-proj-`.

## Usage

1. Run the script
2. Enter the email content when prompted
3. The script will output the extracted meeting details with a format of YAML.
```
{
    "meetings": [
        {
            "time": "2024-03-20 14:00 - 15:00",
            "location": "Conference Room A",
            "description": "Project progress discussion",
            "title": "Project Update"
        },
        {
            "time": "2024-03-22 10:30 - 11:30",
            "location": "Virtual Meeting",
            "description": "Sprint review meeting",
            "title": "Sprint Review"
        }
    ]
}
```
If no meetings are found, the script will output:
```
{
    "meetings": null
}
```