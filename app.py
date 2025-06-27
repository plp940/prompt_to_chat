import streamlit as st
from prompt_engine import run_prompt

#creating a streamlit page
st.set_page_config(page_title="bot", page_icon=":robot_face:", layout="wide")
st.title("prompt engineering Chat bot")
st.write("This is a simple prompt engineering Chat bot that uses Google Gemini to generate responses based on user input.")

#creating a sidebar for user input
#st.sidebar.header("User Input")
prompt_type = st.selectbox("Select Prompt Type", ["zero-shot", "one-shot", "few-shot", "Instruction_based", "chain-of-thought", "Role-based"])
user_input = st.text_area("Enter your question:")

if st.button("🚀 Generate Response"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt before generating a response.")
    else:
        with st.spinner("Generating response..."):
            try:
                output = run_prompt(prompt_type, user_input)
                st.success("Here is the generated response:")
                st.write("### 🤖 Response")
                st.write(output)
            except Exception as e:
                st.error(f"An error occurred while generating the response: {e}")
