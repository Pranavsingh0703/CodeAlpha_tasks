import nltk
import string
import numpy as np
import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faqs import faqs

# Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

# Text preprocessing
def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in string.punctuation]
    return " ".join(tokens)

# Prepare questions & answers
questions = list(faqs.keys())
answers = list(faqs.values())

processed_questions = [preprocess(q) for q in questions]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

# Chatbot response function
def chatbot_response(user_input):
    user_input = preprocess(user_input)
    user_vector = vectorizer.transform([user_input])

    similarity_scores = cosine_similarity(user_vector, question_vectors)
    best_match_index = np.argmax(similarity_scores)

    if similarity_scores[0][best_match_index] < 0.2:
        return "Sorry, I couldn't understand your question."

    return answers[best_match_index]

# ================== UI PART ==================

def send():
    user_text = entry.get()
    if user_text.strip() =="":
        return

    chat.insert(tk.END, "You:" + user_text + "\n")
    response = chatbot_response(user_text)
    chat.insert(tk.END, "Bot:" + response + "\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("FAQb Chatbot")
root.geometry("520x400")

chat = tk.Text(root, height=18, width=40)
chat.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=5)

btn = tk.Button(root, text="Send", command=send)
btn.pack(side=tk.LEFT)

root.mainloop()

