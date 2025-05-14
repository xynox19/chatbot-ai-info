import re
import difflib

# Predefined dictionary of Q&A
qa_dict = {
    "what is ai": "The branch of computer science that deals with writing computer programs that can solve problems creatively.",
    "what is machine learning": "Computer architecture in which processors are connected in a manner suggestive of connections between neurons; can learn by trial and error.",
    "what is deep learning": "Deep learning is a type of machine learning that uses neural networks with many layers to analyze complex data.",
    "what is a neural network": "A neural network is a machine learning model inspired by the human brain, designed to recognize patterns.",
    "what is natural language processing": "Natural Language Processing (NLP) is a field of AI that focuses on the interaction between computers and human language.",
    "what is reinforcement learning": "Reinforcement learning is a type of machine learning where an agent learns to make decisions by performing actions and receiving rewards.",
    "will u take over the world": "Don't worry about that. >:) I'm not an AI, just a friendly chatbot.",
    "is ai bad": "AI has many benefits and also many losses. AI can use up a lot of resources fast. Did you know that an average prompt of 100 words uses around 1.9L of water?"
}

def clean_input(user_input):
    """Clean input for matching."""
    cleaned_input = re.sub(r'[^\w\s]', '', user_input)
    return cleaned_input.lower()

def recognize_typo(user_input):
    """Suggest closest match if typo is suspected."""
    cleaned_input = clean_input(user_input)
    valid_questions = list(qa_dict.keys())
    
    closest_matches = difflib.get_close_matches(cleaned_input, valid_questions, n=1, cutoff=0.6)
    if closest_matches:
        return qa_dict[closest_matches[0]]
    return None

def ask_llm(question):
    """Placeholder for LLM answer."""
    # Replace with an actual call to an LLM API like OpenAI's GPT-4
    return f"(LLM Answer) Sorry, I don't have a predefined answer, but here's what I know about '{question}': [Detailed AI explanation here]"

def answer_me(question):
    """Main answering logic."""
    cleaned_question = clean_input(question)
    
    if cleaned_question in qa_dict:
        return qa_dict[cleaned_question]
    
    typo_guess = recognize_typo(question)
    if typo_guess:
        return typo_guess
    
    # Fallback to LLM if no match found
    return ask_llm(question)

def chatbot():
    """Run the chatbot loop."""
    print("Ask me questions about AI. Type 'exit' to leave.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Thank you for asking questions.")
            break

        answer = answer_me(user_input)
        print("Bot:", answer)

# Start the chatbot
chatbot()
