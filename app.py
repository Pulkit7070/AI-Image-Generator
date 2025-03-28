from flask import Flask, request, jsonify, render_template, send_file
import requests
from datetime import datetime
import os

app = Flask(__name__)

# Create a directory for storing images if it doesn't exist
if not os.path.exists('static/generated_images'):
    os.makedirs('static/generated_images')

# Load Hugging Face API Key from environment variable
api_key = os.getenv("HUGGINGFACE_API_KEY")

# SDXL API Endpoint
api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    try:
        # Get prompt from request
        prompt = request.json.get('prompt')
        
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        # Headers for authentication
        headers = {"Authorization": f"Bearer {api_key}"}

        # API Request with smaller resolution (approximately 2/3 of 1024x1024)
        response = requests.post(api_url, headers=headers, json={
            "inputs": prompt,
            "parameters": {
                "width": 880,
                "height": 480
            }
        })

        if response.status_code == 200:
            # Generate unique filename using timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"generated_image_{timestamp}.png"
            filepath = os.path.join('static/generated_images', filename)
            
            # Save the image
            with open(filepath, "wb") as f:
                f.write(response.content)
            
            # Return the image URL
            return jsonify({
                'success': True,
                'message': 'Image generated successfully',
                'image_url': f'/static/generated_images/{filename}'
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Error generating image',
                'error': response.json()
            }), 500

    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Server error',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
