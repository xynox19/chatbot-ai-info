import streamlit as st
import openai
import re
import difflib
import os

# Load API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Predefined Q&A
qa_dict = {
    "what is ai": "Artificial Intelligence (AI) is a branch of computer science focused on creating systems capable of performing tasks that typically require human intelligence, such as learning, reasoning, and problem-solving.",
    "what is machine learning": "Machine Learning (ML) is a subset of AI that enables systems to learn from data and improve their performance over time without being explicitly programmed.",
    "what is deep learning": "Deep Learning is a type of machine learning that uses neural networks with many layers to model and understand complex patterns in data.",
    "what is a neural network": "A neural network is a computational model inspired by the human brain, made up of interconnected nodes (neurons) that process information and learn patterns from data.",
    "what is natural language processing": "Natural Language Processing (NLP) is a field of AI that enables machines to understand, interpret, and generate human language.",
    "what is reinforcement learning": "Reinforcement Learning is a type of machine learning where an agent learns to make decisions by interacting with an environment and receiving feedback in the form of rewards or penalties.",
    "what is gpt": "GPT (Generative Pre-trained Transformer) is a type of large language model developed by OpenAI that can generate human-like text based on the input it receives.",
    "what is a large language model": "A Large Language Model (LLM) is a type of AI trained on vast amounts of text data to understand and generate natural language. It can perform tasks like summarization, translation, and question answering.",
    "what is ai hallucination": "An AI hallucination occurs when a language model generates a response that is fluent and confident but factually incorrect or nonsensical.",
    "what are the ethical concerns of ai": "Ethical concerns of AI include bias and fairness, transparency, privacy, job displacement, and the potential for misuse or harm if not properly regulated.",
    "is ai dangerous": "AI is not inherently dangerous, but it can be misused or produce harmful outcomes if not designed and managed responsibly.",
    "will u take over the world": "No. I am just a chatbot designed to answer questions.",
    "is ai bad": "AI has many benefits, like improving healthcare and automation, but it also poses risks such as bias, surveillance, and environmental costs if not managed carefully."
}

# Helpers
def clean_input(text):
    return re.sub(r"[^\w\s]", "", text).lower()

def recognize_typo(user_input):
    cleaned_input = clean_input(user_input)
    closest = difflib.get_close_matches(cleaned_input, qa_dict.keys(), n=1, cutoff=0.6)
    if closest:
        return qa_dict[closest[0]]
    return None

def ask_llm(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that explains AI concepts."},
                {"role": "user", "content": question}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

def answer_question(question):
    cleaned = clean_input(question)
    if cleaned in qa_dict:
        return qa_dict[cleaned]
    typo_answer = recognize_typo(question)
    if typo_answer:
        return typo_answer
    return ask_llm(question)

# UI
st.set_page_config(page_title="AI Chatbot")
st.title("AI Chatbot")

user_input = st.text_input("Ask a question about AI:")

if user_input:
    response = answer_question(user_input)
    st.markdown("**Answer:**")
    st.write(response)
