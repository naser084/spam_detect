
import joblib
import streamlit as st

# Load the pre-trained model and vectorizer
model = joblib.load('ed.h5')  # 'ed.h5' should be a pre-trained model file
vec = joblib.load('vectorizer.h5')  # 'vectorizer.h5' should be the corresponding vectorizer file

# Function to predict whether the text is spam or ham
def predict_spam(text):
    text_vector = vec.transform([text])  # Vectorize the input text
    prediction = model.predict(text_vector)  # Predict using the loaded model
    return prediction[0]

# Streamlit app
st.title("Spam Detection System by naser")

st.sidebar.title("Login here")
st.sidebar.text_input("Mail")
st.sidebar.text_input("Password")
st.sidebar.button("submit")

# Text input from the user
user_input = st.text_area("Enter text to classify as Spam or Ham")

# Predict button
if st.button("Predict"):
    result = predict_spam(user_input)
    if result == 1:  # Assuming '1' means spam
        st.error("This text is classified as Spam.")
    else:  # Assuming '0' means ham (not spam)
        st.success("This text is classified as Ham.")

import streamlit as st

st.header("Rate my website")
rating = st.select_slider("Rating", ["Worst", "Bad", "Good", "Excellent"])

if st.button("Submit"):
    st.success("Submitted successfully!")
    st.balloons()
