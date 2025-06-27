import google.generativeai as genai
from dotenv import load_dotenv
import os
#configure gemini api key

#gemini_api_key = ""
#genai.configure(api_key=gemini_api_key)
load_dotenv()##load all the environtment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.0-flash-001")

#create a function to define the prompt
def run_prompt(prompt_type,user_input):
    if prompt_type == "zero-shot":
        prompt = f"Answer the following question: {user_input}"
    elif prompt_type == "one-shot":
        prompt = (
            "Question: What is the capital of France?\n"
            "Answer: Paris\n"
            f"Question: {user_input}\n"
            "Answer: "
        )
    elif prompt_type == "few-shot":
        prompt = (
            "Question: What is the capital of France?\n"
            "Answer: Paris\n"
            "Question: What is the capital of Germany?\n"
            "Answer: Berlin\n"
            f"Question: {user_input}\n"
            "Answer: "
        )
    elif prompt_type == "Instruction_based":
        prompt = (
            f"Please provide a detailed summary to the following question : {user_input}"
        )
    elif prompt_type == "chain-of-thought":
        prompt = (
            "solve the neural network backpropagation problem step by step.\n"
            f"{user_input}"
        )
    elif prompt_type == "Role-based":
        prompt = (
            "You are a helpful assistant. Answer the following question as if you were an expert in the field.\n"
            f"{user_input}"
        )
    else:
        prompt = user_input


    response = model.generate_content(prompt)    
    return response.text.strip() or response.candidates[0].content.strip()