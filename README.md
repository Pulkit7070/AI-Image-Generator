# AI Image Generator

## Overview
This project is an AI-powered image generator that utilizes the Stability AI model via the Hugging Face API. Users can enter a text prompt, and the application will generate an image based on that prompt. The project is built using Flask for the backend and a simple HTML/CSS/JavaScript frontend.

## Features
- Text-based prompt input for image generation
- Uses Stability AI's Stable Diffusion XL model hosted on Hugging Face
- Generates and saves images locally
- Displays generated images on the frontend
- User-friendly interface

## Technologies Used
- Flask (Python)
- Hugging Face API (Stable Diffusion XL Model)
- HTML, CSS, JavaScript (Frontend UI)
- Requests (for API calls)

## Installation
### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Flask
- Requests library

### Setup
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a folder for storing generated images:
   ```bash
   mkdir -p static/generated_images
   ```
4. Set up your Hugging Face API Key:
   - Obtain an API key from [Hugging Face](https://huggingface.co/)
   - Replace `api_key` in `app.py` with your own key

## Usage
1. Run the Flask app:
   ```bash
   python app.py
   ```
2. Open a browser and go to `http://127.0.0.1:5000/`
3. Enter a text prompt and click "Generate Image"
4. Wait for the AI to generate an image
5. The generated image will be displayed and saved in `static/generated_images/`

## Project Structure
```
/ai-image-generator
│── static/
│   ├── generated_images/   # Stores generated images
│── templates/
│   ├── index.html          # Frontend UI
│── app.py                  # Flask backend
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
```

## API Endpoint
- **POST `/generate-image`**
  - **Request Body:** `{ "prompt": "Your image description here" }`
  - **Response:** `{ "success": true, "image_url": "/static/generated_images/image_name.png" }`

## License
This project is open-source and free to use.

## Author
Developed by Pulkit. Feel free to contribute or report issues!

