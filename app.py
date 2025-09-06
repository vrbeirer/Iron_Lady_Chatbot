from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend (index.html) to call backend

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_KEY"

# Predefined FAQ responses
faq = {
    "programs": "Iron Lady offers leadership programs for women, focusing on confidence, career growth, and leadership skills.",
    "duration": "The programs usually range from 6 weeks to 3 months, depending on the track chosen.",
    "mode": "The programs are conducted online with live interactive sessions.",
    "certificate": "Yes, certificates are provided upon successful completion of the program.",
    "mentors": "The mentors and coaches are industry leaders, experienced professionals, and certified trainers."
}

# Function to call OpenAI if no FAQ match
def ai_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant answering questions about Iron Lady leadership programs."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"⚠️ Error contacting AI service: {e}"

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    if "program" in user_input:
        reply = faq["programs"]
    elif "duration" in user_input:
        reply = faq["duration"]
    elif "online" in user_input or "offline" in user_input or "mode" in user_input:
        reply = faq["mode"]
    elif "certificate" in user_input:
        reply = faq["certificate"]
    elif "mentor" in user_input or "coach" in user_input:
        reply = faq["mentors"]
    else:
        reply = ai_response(user_input)  # Fallback to AI

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
