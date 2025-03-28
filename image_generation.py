import requests
import os
from datetime import datetime

# Load Hugging Face API Key from environment variable
api_key = os.getenv("HUGGINGFACE_API_KEY")

# SDXL API Endpoint
api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

# Get prompt from user
user_input = input("Enter your prompt for image generation: ")

# Headers for authentication
headers = {"Authorization": f"Bearer {api_key}"}

# API Request
response = requests.post(api_url, headers=headers, json={"inputs": user_input})

# Save the image if successful
if response.status_code == 200:
    # Generate unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_image_{timestamp}.png"
    
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Image saved successfully as '{filename}'.")
else:
    print("Error:", response.json())
