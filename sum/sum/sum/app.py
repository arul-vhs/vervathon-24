from flask import Flask, render_template, request, jsonify
import requests
import PyPDF2
import os
import random

app = Flask(__name__)

# Replace with your Hugging Face API token
HUGGINGFACE_API_TOKEN = "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"

# Function to summarize text
def summarize_text(text):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
    }
    payload = {"inputs": text}
    response = requests.post("https://api-inference.huggingface.co/models/facebook/bart-large-cnn", headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()[0]['summary_text']
    else:
        return "Error summarizing text."

# Function to generate quiz questions from the summary
def generate_quiz(summary):
    # Split summary into sentences and generate questions
    sentences = summary.split('. ')
    questions = []
    for i, sentence in enumerate(sentences):
        question = f"What is the main idea of this sentence: '{sentence}'?"
        answer = "This is a sample answer."
        options = [answer, "Incorrect answer 1", "Incorrect answer 2", "Incorrect answer 3"]
        random.shuffle(options)
        questions.append({
            "question": question,
            "options": options,
            "answer": answer
        })
    return questions

# Function to handle chat responses
def chat_with_ai(message):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
    }
    payload = {
        "inputs": message,
    }
    response = requests.post("https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill", headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json().get('generated_text', "Sorry, I don't have a response.")
    else:
        return "Error chatting with AI."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    if file and (file.filename.endswith('.pdf') or file.filename.endswith('.pptx')):
        filename = file.filename
        file_path = os.path.join("uploads", filename)
        file.save(file_path)
        
        text = ''
        if filename.endswith('.pdf'):
            with open(file_path, "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                for page in reader.pages:
                    text += page.extract_text()
        
        summary = summarize_text(text)
        quiz = generate_quiz(summary)
        
        return jsonify({'summary': summary, 'quiz': quiz})
    else:
        return "Invalid file format", 400

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = chat_with_ai(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
