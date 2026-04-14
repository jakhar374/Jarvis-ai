from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="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")

@app.route("/")
def home():
    return "Jarvis AI is running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    prompt = data.get("message")

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a Jarvis-like assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
