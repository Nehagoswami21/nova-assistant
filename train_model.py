# train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import joblib
import os

# Load and prepare your data
data_file = "intents.csv"

if not os.path.exists(data_file):
    print(f"❌ {data_file} not found. Make sure it exists in the same folder.")
    exit()

df = pd.read_csv(data_file)

if 'text' not in df.columns or 'intent' not in df.columns:
    print("❌ CSV must have 'text' and 'intent' columns.")
    exit()

X = df['text']
y = df['intent']

# Vectorize text using TF-IDF
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LinearSVC()
model.fit(X_vectorized, y)

# Save both model and vectorizer
joblib.dump(model, "intent_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model and vectorizer saved as 'intent_model.pkl' and 'vectorizer.pkl'")
