from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class SentimentRequest(BaseModel):
    text: str

@app.get("/api/learning-path")
def get_path():
    return [
        {"id": 1, "title": "AI Quest", "description": "10 Random Questions", "status": "unlocked"},
        {"id": 2, "title": "Data Hunter", "description": "Levels 1-10 Mission", "status": "unlocked"},
        {"id": 3, "title": "Neural Architect", "description": "Build & Train Lab", "status": "unlocked"}
    ]

@app.get("/api/quiz/ai")
def get_quiz():
    q_bank = [
        {"q": "Father of AI?", "o": ["John McCarthy", "Elon Musk", "Bill Gates"], "a": "John McCarthy"},
        {"q": "What is NLP?", "o": ["Natural Language Processing", "Node Loop", "New Logic"], "a": "Natural Language Processing"},
        {"q": "What is an Outlier?", "o": ["Normal data", "Extreme Noise", "Correct value"], "a": "Extreme Noise"},
        {"q": "Neural Networks mimic what?", "o": ["Human Brain", "Car Engine", "Weather"], "a": "Human Brain"},
        {"q": "Python library for Data?", "o": ["Pandas", "Spotify", "Snapchat"], "a": "Pandas"},
        {"q": "Supervised Learning uses?", "o": ["Labels", "No Data", "Guesses"], "a": "Labels"},
        {"q": "What is Deep Learning?", "o": ["Multi-layer NN", "Basic math", "Storage"], "a": "Multi-layer NN"},
        {"q": "AI that sees is called?", "o": ["Computer Vision", "Talk Bot", "Smell AI"], "a": "Computer Vision"},
        {"q": "What is Overfitting?", "o": ["Memorizing data", "Generalizing", "Failing"], "a": "Memorizing data"},
        {"q": "Most used AI language?", "o": ["Python", "C++", "HTML"], "a": "Python"},
        {"q": "What is an Algorithm?", "o": ["Set of rules", "Screen", "Mouse"], "a": "Set of rules"},
        {"q": "Is AI sentient yet?", "o": ["No", "Yes", "Maybe"], "a": "No"},
        {"q": "What is Big Data?", "o": ["Massive datasets", "Small files", "Huge PC"], "a": "Massive datasets"},
        {"q": "What is a Neuron?", "o": ["Math function", "Hardware", "Battery"], "a": "Math function"},
        {"q": "What is Tuning?", "o": ["Adjusting parameters", "Deleting", "Fixing"], "a": "Adjusting parameters"}
    ]
    random.shuffle(q_bank)
    return q_bank[:10] # Forces exactly 10 random questions

@app.get("/api/leaderboard")
def get_leaderboard():
    return [
        {"name": "AI_Master", "score": 4500, "rank": 1},
        {"name": "Data_Guru", "score": 3800, "rank": 2},
        {"name": "Neural_Knight", "score": 3200, "rank": 3},
        {"name": "Pioneer_X", "score": 1500, "rank": 4}
    ]

@app.post("/api/predict")
async def predict(req: SentimentRequest):
    pos = ['good', 'great', 'happy', 'love', 'best', 'excellent', 'awesome']
    res = "Positive" if any(w in req.text.lower() for w in pos) else "Negative"
    return {"sentiment": res, "confidence": 0.94, "advice": "Great data!" if res=="Positive" else "Needs variety."}
# Add this at the bottom of backend/main.py

@app.get("/api/lessons")
def get_lessons():
    return [
        {
            "id": "intro",
            "title": "Introduction to AI",
            "content": "AI is the simulation of human intelligence by machines. It includes learning, reasoning, and self-correction.",
            "topics": ["History of AI", "Turing Test", "Modern Applications"]
        },
        {
            "id": "ml-basics",
            "title": "How ML Works",
            "content": "Machine Learning is a subset of AI that uses statistical techniques to give computers the ability to 'learn' from data.",
            "topics": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning"]
        },
        {
            "id": "neural-nets",
            "title": "Deep Learning & Neurons",
            "content": "Neural networks are inspired by the human brain. They consist of input, hidden, and output layers.",
            "topics": ["Weights and Biases", "Backpropagation", "Activation Functions"]
        }
    ]