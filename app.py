@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_text = data.get("question", "")
    user_lang = data.get("lang", "en")

    from deep_translator import GoogleTranslator

    # Translate to English
    translated = GoogleTranslator(source=user_lang, target="en").translate(user_text).lower()

    # Find answer
    faq = {
        "what is cgpa": "CGPA is Cumulative Grade Point Average, calculated across semesters.",
        "library timing": "The library is open from 9 AM to 6 PM on weekdays.",
        "placement cell": "The placement cell helps students with internships and jobs."
    }

    response = "Sorry, I don’t know. Assigning to staff..."
    for q, ans in faq.items():
        if q in translated:
            response = ans
            break

    # Translate back
    final_response = GoogleTranslator(source="en", target=user_lang).translate(response)

    return jsonify({"answer": final_response})
