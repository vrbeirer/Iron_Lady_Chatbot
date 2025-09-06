# Iron Lady Chatbot 🤖

A simple chatbot built with **Flask (Python backend)** and a **frontend chat UI (HTML/CSS/JS)**.  
The chatbot answers FAQs about **Iron Lady leadership programs** and can also use **OpenAI GPT-3.5** for more interactive responses.

---

## 🚀 Features
- Predefined FAQ answers (programs, duration, mode, certificates, mentors)  
- Fallback to **OpenAI GPT-3.5** when no FAQ match is found  
- Simple, clean frontend chat UI  
- Flask backend with REST API  
- CORS enabled for frontend-backend communication  

---

## 📂 Project Structure
iron-lady-chatbot/
│
├── app.py # Flask backend (FAQ + OpenAI integration)
├── index.html # Frontend chat UI
└── README.md # Documentation



---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/iron-lady-chatbot.git
cd iron-lady-chatbot


**install Dependencies:**

pip install flask flask-cors openai


**Set OpenAI API Key**

# Mac/Linux
export OPENAI_API_KEY="your_api_key_here"

# Windows
set OPENAI_API_KEY=your_api_key_here


**Then in app.py:**

import os
openai.api_key = os.getenv("OPENAI_API_KEY")



**Running the project:**

Start the backend  - python app.py (Server will run at: http://127.0.0.1:5000)
Open the index.html in your browser directly or serve it with : (python -m http.server 8000
)


💡 Example Questions

What programs does Iron Lady offer?

Is the program online or offline?

Who are the mentors?

Are certificates provided?

(Any other question → answered by AI)
