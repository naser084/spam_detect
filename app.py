import joblib
import streamlit as st

# Load the pre-trained model and vectorizer
model = joblib.load('ed.h5')  # Ensure this model file path is correct
vec = joblib.load('vectorizer.h5')  # Ensure this vectorizer file path is correct

# Function to predict whether the text is spam or ham
def predict_spam(text):
    text_vector = vec.transform([text])  # Vectorize the input text
    prediction = model.predict(text_vector)  # Predict using the loaded model
    return prediction[0]

# Custom CSS for title color
st.markdown(
    """
    <style>
    .title {
        color: #4CAF50;  /* Customize color here */
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        font-family: Arial, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with custom CSS class
st.markdown("<h1 class='title'>Smart Spam Identifier by Naser</h1>", unsafe_allow_html=True)

# Sidebar for login
st.sidebar.title("Login here")
email = st.sidebar.text_input("Mail")  # Store the input for further use if needed
password = st.sidebar.text_input("Password", type="password")
if st.sidebar.button("Submit"):  # Ensure this button is at the correct level
    st.sidebar.write("Login submitted!")

# Main input and button for prediction
user_input = st.text_area("Enter text to classify as Spam or Ham")
if st.button("Predict"):  # Ensure this is at the correct indentation level
    result = predict_spam(user_input)
    if result == 1:  # Assuming '1' means spam
        st.error("This text is classified as Spam.")
    else:  # Assuming '0' means ham (not spam)
        st.success("This text is classified as Ham.")

# Additional rating feature
st.header("Rate my website")
rating = st.select_slider("Rating", ["Worst", "Bad", "Good", "Excellent"])

# Define the color based on the rating
if rating == "Worst":
    color = "yellow"
elif rating == "Bad":
    color = "orange"
elif rating == "Good":
    color = "green"
elif rating == "Excellent":
    color = "blue"

# Display the selected rating with the corresponding color
st.markdown(
    f"<h3 style='color: {color};'>Your rating: {rating}</h3>",
    unsafe_allow_html=True
)

# Submit button for rating
if st.button("Submit Rating"):  # Unique label to avoid conflicts
    st.success("Rating submitted successfully!")
    st.snow()  # Shows snow effect on successful submission
