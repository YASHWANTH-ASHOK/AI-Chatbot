import pickle
import json
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

# -----------------------------
# Initialize Flask App
# -----------------------------
app = Flask(__name__)
CORS(app)

# -----------------------------
# Load Trained Model & Files
# -----------------------------
model = pickle.load(open("chatbot_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

with open("intents.json", "r") as file:
    intents = json.load(file)

# -----------------------------
# Response Logic
# -----------------------------
def get_response(user_message):
    X = vectorizer.transform([user_message])
    prediction = model.predict(X)[0]

    for intent in intents["intents"]:
        if intent["tag"] == prediction:
            return np.random.choice(intent["responses"])

    return "Sorry, I didn't understand that."

# -----------------------------
# Chat Route
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    reply = get_response(user_message)
    return jsonify({"reply": reply})

# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)