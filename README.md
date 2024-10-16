# Vervathon-2023

## Submission Instruction:
  1. Fork this repository
  2. Create a folder with your Team Name,Team leader name and your problem statement number
  3. Upload all the code and necessary files in the created folder
  4. Upload a **README.md** file in your folder with the below mentioned informations.
  5. Generate a Pull Request with your Team Name. (Example: XYZ_Adhi_1)

## README.md must consist of the following information:

#### Team Name - Solvents
#### Problem Statement - Educarion with ai and engagment
#### Team Leader Email -tharunm.engineer@gmail.com

## A Brief of the Prototype:
This prototype is a PDF Summarizer and Quiz Generator web application, enhanced with an AI-powered chat feature. Here's a brief summary of the functionality:

Features:
PDF Upload and Summarization:

Users can upload a .pdf or .pptx file.
The content is extracted and sent to Hugging Face's summarization model (e.g., facebook/bart-large-cnn).
A summarized version of the text is returned and displayed to the user.
Quiz Generation:

From the summarized text, the system automatically generates quiz questions.
Each question asks about the key idea of sentences from the summary.
Multiple choice options are provided for each quiz question.
Users can select their answers to the quiz.
AI Chat Box:

After completing the quiz, users can chat with an AI model using Hugging Face's Blenderbot model.
The chat feature responds to user messages with AI-generated responses related to the uploaded content.
Front-End Features:

The interface includes a clean, minimal design for file upload, quiz interaction, and chat functionalities.
The UI is powered by HTML and CSS, while JavaScript is used to handle interactions like file upload, displaying quiz questions, and sending/receiving messages from the AI.
Components:
Flask is the backend framework used to handle file uploads, summarize content, generate quizzes, and handle chat requests.
Hugging Face API is used to process the summarization and chat functionality.
JavaScript manages the front-end interactions, including form submissions and dynamically displaying quiz and chat responses.
This prototype integrates various AI models for practical purposes, like understanding PDF content, generating educational quizzes, and offering interactive AI conversations.
  
## Tech Stack: 

### Tech Stack

1. **Frontend:**
   - **HTML:** For structuring the web pages.
   - **CSS:** For styling the web application and making it visually appealing.
   - **JavaScript:** For handling user interactions, form submissions, and dynamic content updates (e.g., displaying quiz questions and chat responses).

2. **Backend:**
   - **Flask:** A lightweight web framework for Python that handles routing, request/response handling, and serves the web application.
   - **PyPDF2:** A Python library used for reading and extracting text from PDF files.

3. **APIs:**
   - **Hugging Face API:** 
     - **Summarization Model:** For summarizing the text extracted from uploaded PDFs. (e.g., `facebook/bart-large-cnn`)
     - **Chat Model:** For generating AI responses to user queries. (e.g., `facebook/blenderbot-400M-distill`)

4. **File Handling:**
   - **Flask-Uploads:** To manage file uploads, ensuring that users can upload PDF and PPTX files.

5. **Development Tools:**
   - **Python 3.x:** The programming language used for backend development.
   - **VS Code or any other code editor:** For writing and managing the code.
   - **Local Environment (Flask Development Server):** For testing the application during development.

### Additional Tools (Optional):
- **Git:** For version control and managing changes to the codebase.
- **Postman:** For testing API endpoints separately from the frontend.

This tech stack combines popular frameworks and libraries to create a functional and interactive web application that leverages AI for summarization and chat functionalities.
## What I Learned:
   Here's a summary of what you've learned while building the PDF Summarizer and Quiz Generator application:

### Learning Outcomes

1. **Web Development Basics:**
   - Understanding how to structure a web application using HTML for layout and CSS for styling.
   - Utilizing JavaScript to enhance user experience by handling dynamic interactions.

2. **Flask Framework:**
   - Learning to set up a Flask application and create routes to handle different user requests (e.g., uploading files, generating summaries, and handling chat).
   - Using Flask to render templates and serve static files.

3. **File Handling:**
   - Implementing file upload functionality to allow users to upload PDFs and PPTX files.
   - Using the `PyPDF2` library to extract text from PDF documents.

4. **API Integration:**
   - Working with external APIs, specifically the Hugging Face API, to utilize AI models for text summarization and chat.
   - Understanding how to format requests and handle responses from APIs.

5. **Data Handling:**
   - Learning how to process the extracted text to create summaries and generate quiz questions based on the summaries.
   - Using JSON to send data back and forth between the frontend and backend.

6. **Quiz Generation Logic:**
   - Creating logic to generate quiz questions from summarized text, including answer choices and correct answers.

7. **Chatbot Functionality:**
   - Implementing a basic chatbot feature that interacts with users and provides responses based on the uploaded content.

8. **Debugging and Troubleshooting:**
   - Gaining experience in debugging issues related to API integration, JavaScript functionality, and Flask routing.

9. **User Interface Design:**
   - Learning how to create a user-friendly interface that allows users to interact seamlessly with the application.

10. **Project Management:**
    - Managing the development of a multi-featured application and integrating various components to work together smoothly.

These skills will be beneficial as you continue to explore web development, AI integration, and Python programming.
