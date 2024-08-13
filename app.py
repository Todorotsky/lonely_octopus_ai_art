import streamlit as st
import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set up the Streamlit app
st.title('AI Art Critique: Enhancing Artistic Understanding with GPT-4o mini')
st.markdown(
    'This app uses GPT-4o mini to critique images. Simply enter the URL of the image you want to analyze. '
    'The AI will provide a detailed critique based on the visual content.'
)

# Display a square image on top of the sidebar
sidebar_image_url = "https://i.ebayimg.com/images/g/wPoAAOSwNyFhY3~Z/s-l1200.webp"
st.sidebar.image(sidebar_image_url, use_column_width=True)

# Sidebar user input
st.sidebar.header("User Input")
user_image_url = st.sidebar.text_input(
    "Enter the URL of the image you want critiqued:", 
    value="https://yt3.googleusercontent.com/lqkWHj25LED8Bu51eofSutzzErko20ndDozCybnRd-ADSMwxXuHbRubOqYKJvBIjYHYPnR4nVg=w1707-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj"  # Default image URL
)

# Display the user-provided image immediately after the URL is entered
if user_image_url:
    st.image(user_image_url, caption="Image for Critique", use_column_width=True)

# Submit Button with a space emoji
submit_button = st.sidebar.button("Analyze Artwork 🚀")

# Define a function to get the AI critique
def get_openai_critique(image_url):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "You are Lt. Commander Data from Star Trek: The Next Generation. "
                            "Analyze the image at the following URL in terms of artistic composition, "
                            "use of color, subject matter, and overall impact. Provide a detailed critique "
                            "highlighting both strengths and potential areas for improvement. As an android, "
                            "I will offer an objective assessment without concern for human emotions. "
                            "Additionally, provide a rating out of 5 stars (⭐)."
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            }
        ],
        max_tokens=500
    )
    
    # Extract critique from the response
    critique = response.choices[0].message.content
    return critique

# Processing User Inputs
if submit_button and user_image_url:
    # Get the artwork critique from OpenAI
    artwork_critique = get_openai_critique(user_image_url)
    
    # Display the critique
    st.markdown("### Artwork Critique")
    st.write(artwork_critique)
else:
    st.write("Please enter an image URL, then click 'Analyze Artwork 🚀'.")
