import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
with open("intents.json", "r") as f:
    data = json.load(f)

patterns = []
tags = []

for intent in data["intents"]:
    for p in intent["patterns"]:
        patterns.append(p)
        tags.append(intent["tag"])

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

# Train classifier
model = LogisticRegression()
model.fit(X, tags)

# Save model
pickle.dump(model, open("chatbot_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Training completed!")
