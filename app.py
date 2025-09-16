from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# Simple knowledge base (later we connect DB or curriculum)
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

    # Translate to English for processing
    translated = translator.translate(user_text, src=user_lang, dest="en").text.lower()

    # Find answer in knowledge base
    response = "Sorry, I don’t know. Assigning to staff..."
    for q, ans in faq.items():
        if q in translated:
            response = ans
            break

    # Translate answer back to user’s language
    final_response = translator.translate(response, src="en", dest=user_lang).text

    return jsonify({"answer": final_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
