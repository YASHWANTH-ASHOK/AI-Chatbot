# AI-Chatbot
An intelligent conversational AI system that processes user queries using Natural Language Processing and generates context-aware responses. The chatbot is designed to simulate human-like interactions and can be extended for customer support, educational assistance, or automation tasks.

AI Chatbot Project(title)

This project is an intent-based AI chatbot developed using Python and Machine Learning.
The chatbot predicts user queries using TF-IDF vectorization and Logistic Regression, and returns appropriate responses based on predefined intents.
The system is designed to handle college-related queries such as admissions, courses, fees, placements, hostel information, scholarships, and contact details.

Technologies Used

Python
Flask
Scikit-learn
NLTK
HTML
CSS
JavaScript

Project Structure

AI-Chatbot/
│
├── backend/
│   ├── app.py
│   ├── train.py
│   ├── intents.json
│   ├── chatbot_model.pkl
│   └── vectorizer.pkl
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── README.md

How It Works

User sends a message through the frontend interface.
The Flask backend receives the request.
The message is transformed using TF-IDF vectorization.
Logistic Regression predicts the intent.
A response is selected from the matched intent and returned to the user.

Installation and Setup

1. Clone the Repository
git clone https://github.com/your-username/AI-Chatbot.git
cd AI-Chatbot/backend

3. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

4. Install Dependencies
pip install flask scikit-learn nltk

5. Train the Model
python train.py

This will generate:
chatbot_model.pkl
vectorizer.pkl

6. Run the Application
python app.py

Open frontend/index.html in your browser to interact with the chatbot.

Customization

To add new intents:
Edit intents.json
Add new tags, patterns, and responses
Retrain the model using:
python train.py
Restart the Flask server

Future Enhancements

Deployment to cloud platforms
Integration with database
Improved NLP preprocessing
Deep learning-based intent classification
