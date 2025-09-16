from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Simple knowledge base
faq = {
    "what is cgpa": "CGPA is Cumulative Grade Point Average, calculated across semesters.",
    "library timing": "The library is open from 9 AM to 6 PM on weekdays.",
    "placement cell": "The placement cell helps students with internships and jobs."
}

@app.route("/")
def home():
    return "Campus Assistant Backend is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_text = data.get("question", "")
    user_lang = data.get("lang", "en")

    # Translate to English
    translated = GoogleTranslator(source=user_lang, target="en").translate(user_text).lower()

    # Find answer
    response = "Sorry, I don’t know. Assigning to staff..."
    for q, ans in faq.items():
        if q in translated:
            response = ans
            break

    # Translate back
    final_response = GoogleTranslator(source="en", target=user_lang).translate(response)

    return jsonify({"answer": final_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
