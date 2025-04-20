🌱 Project Overview
This project is a web application built with Python and Streamlit that helps users track challenges, reflect on their experiences, and celebrate their achievements, fostering a growth mindset
 🛠️ Prerequisites
Ensure you have the following installed:
 Python 3x
 Visual Studio Code (VS Cod)
 Streamlit libray
To install Streamlit, run:
```bas
pip install streamlt

 🧱 Step-by-Step Guide
 1. **Set Up Your Project Directory**
Create a new directory for your project and navigate into it:
```bah
mkdir growth_mindset_app
cd growth_mindset_pp

2. **Create the Application Script**
In your project directory, create a file named `app.py` and open it in VS Code. Add the following code:
```pythn
import streamlit as st
# Title of the app
st.title("Growth Mindset Tracker")
# Sidebar for user input
st.sidebar.header("Your Growth Journey")
# Challenge input
challenge = st.sidebar.text_area("Describe a challenge you're facing:")
# Reflection input
reflection = st.sidebar.text_area("What did you learn from this experience?")
# Effort input
effort = st.sidebar.text_area("How did you persist through difficulties?")
# Celebrate input
celebration = st.sidebar.text_area("Celebrate your effort! What did you achieve?")
# Display inputs on the main page
if st.sidebar.button("Reflect"):
    st.subheader("Your Growth Journey Reflection")
    st.write(f"**Challenge:** {challenge}")
    st.write(f"**Reflection:** {reflection}")
    st.write(f"**Effort:** {effort}")
    st.write(f"**Celebration:** {celebration}")
 Inspirational quote
st.markdown("""
> "The only limit to our realization of tomorrow is our doubts of today."
> – Franklin D. Roosevelt
"")

3. **Run the Application**
In the terminal, navigate to your project directory and run:
```bah
streamlit run apppy
This will start the Streamlit server and open the application in your default web browsr. 📦 Optional: Share Your Applicatin
To share your application with others, you can deploy it using services like [Streamlit Cloud](https://streamlit.io/cloud) or [Heroku](https://www.heroku.co/).
 📚 Additional Resources
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Growth Mindset Training by Microsoft](https://learn.microsoft.com/en-us/training/modules/develop-growth-mindset/)
- [Panaversity Learn Modern AI Python Repository](https://github.com/panaversity/learn-modern-ai-python)
