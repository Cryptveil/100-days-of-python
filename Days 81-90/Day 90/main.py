import requests
import json
import vlc

API_KEY = ""
url = "https://api.ispeech.org/api/rest/v2.0/speech.json"
pdf_file = ""

# Read the PDF file as binary data
with open(pdf_file, "rb") as f:
    pdf_data = f.read()

# Define the parameters for the iSpeech API request
params = {
    "apikey": API_KEY,
    "action": "convert",
    "voice": "usenglishfemale",
    "output": "json",
    "file": (pdf_file, pdf_data, "application/pdf")
}

# Send the API request and get the response
response = requests.post(url, files=params)

# Extract the URL of the speech file from the response
result = json.loads(response.content)
speech_url = result["response"]["url"]

# Use a media player to play the speech file
p = vlc.MediaPlayer(speech_url)
p.play()
