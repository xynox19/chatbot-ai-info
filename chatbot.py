import re
import difflib
import openai
import os

# Option 1: Get key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Option 2 (if you prefer hardcoding — NOT recommended)
# openai.api_key = "your-api-key"

qa_dict = {
    "what is ai": "Artificial Intelligence (AI) is a branch of computer science focused on creating systems capable of performing tasks that typically require human intelligence, such as learning, reasoning, and problem-solving.",

    "what is machine learning": "Machine Learning (ML) is a subset of AI that enables systems to learn from data and improve their performance over time without being explicitly programmed.",

    "what is deep learning": "Deep Learning is a type of machine learning that uses neural networks with many layers to model and understand complex patterns in data.",

    "what is a neural network": "A neural network is a computational model inspired by the human brain, made up of interconnected nodes (neurons) that process information and learn patterns from data.",

    "what is natural language processing": "Natural Language Processing (NLP) is a field of AI that enables machines to understand, interpret, and generate human language.",

    "what is reinforcement learning": "Reinforcement Learning is a type of machine learning where an agent learns to make decisions by interacting with an environment and receiving feedback in the form of rewards or penalties.",

    "will u take over the world": "No worries! I'm just a chatbot designed to answer questions, not to conquer the world. :)",

    "is ai bad": "AI has both benefits and challenges. While it can improve efficiency and innovation, it also raises concerns around bias, job displacement, and environmental impact—like energy and water usage in large models."
}

def clean_input(user_input):
    return re.sub(r'[^\w\s]', '', user_input).lower()

def recognize_typo(user_input):
    cleaned_input = clean_input(user_input)
    valid_questions = list(qa_dict.keys())
    closest = difflib.get_close_matches(cleaned_input, valid_questions, n=1, cutoff=0.6)
    if closest:
        return qa_dict[closest[0]]
    return None

def ask_llm(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that explains artificial intelligence concepts."},
                {"role": "user", "content": question}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Sorry, I had trouble reaching the AI model: {str(e)}"

def answer_me(question):
    cleaned = clean_input(question)
    
    if cleaned in qa_dict:
        return qa_dict[cleaned]
    
    typo_answer = recognize_typo(question)
    if typo_answer:
        return typo_answer
    
    return ask_llm(question)

def chatbot():
    print("Ask me questions about AI. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Thank you! See you next time.")
            break

        answer = answer_me(user_input)
        print("Bot:", answer)

# Start the chatbot
chatbot()
