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


💡 Example Questions

What programs does Iron Lady offer?

Is the program online or offline?

Who are the mentors?

Are certificates provided?

(Any other question → answered by AI)
