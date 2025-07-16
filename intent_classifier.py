import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load intents dataset
df = pd.read_csv("intents.csv")

# Vectorize text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['intent']

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, 'intent_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model and vectorizer saved.")


