# AI Image Generator

This is an AI-powered image generator using the **Stable Diffusion XL** model from Hugging Face. The application consists of:
- A **Flask web app** (`app.py`) for generating images via a web interface.
- A **standalone script** (`image_generation.py`) for generating images directly from the command line.

## Features
- Generate AI images using text prompts
- Automatically saves generated images
- Secure API authentication using environment variables
- Web-based and command-line interfaces

---

## **Setup & Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/Pulkit7070/AI-Image-Generator.git
cd AI-Image-Generator
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**
To keep your Hugging Face API key secure, store it as an environment variable.

#### **For Windows (Command Prompt):**
```cmd
set HUGGINGFACE_API_KEY=your_secret_token
```

#### **For Mac/Linux (Terminal):**
```bash
export HUGGINGFACE_API_KEY="your_secret_token"
```

---

## **Usage**

### **1. Running the Flask Web App**
```bash
python app.py
```
- Open `http://127.0.0.1:5000/` in your browser.
- Enter a text prompt to generate an image.
- The image will be saved inside the `static/generated_images/` folder.

### **2. Using the Standalone Script**
Run the script to generate an image from the command line:
```bash
python image_generation.py
```
- Enter a prompt when prompted.
- The generated image will be saved in the same directory as the script.

---

## **Security & API Key Protection**
### **⚠️ Important: Do NOT Hardcode API Keys in Your Code**
Your Hugging Face API key should be set using environment variables instead of being hardcoded into the scripts. If you accidentally commit a secret:

```bash
git rm --cached app.py image_generation.py
git commit --amend --no-edit
git push origin main --force
```

If GitHub still blocks the push due to past commits, use:
```bash
git filter-repo --path app.py --path image_generation.py --invert-paths
```
Then push again:
```bash
git add .
git commit -m "Removed API key and updated security"
git push origin main
```

---

## **License**
This project is licensed under the **MIT License**.

---

## **Contributing**
Feel free to fork the repo and submit pull requests with improvements.

### **Contact**
For any issues, open an issue on GitHub or contact me via [GitHub](https://github.com/Pulkit7070).

