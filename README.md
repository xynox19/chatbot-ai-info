AI Chatbot – Streamlit Frontend
===============================

This project is a simple AI chatbot built using Python and Streamlit. It can answer questions about artificial intelligence using a predefined knowledge base. If a question isn't found in the dictionary, it falls back to an OpenAI GPT model (if API access is configured).

Features:
---------
- Fast responses for common AI questions using a local dictionary
- Typo tolerance and fuzzy matching
- Dynamic fallback to OpenAI GPT-4 for unknown questions
- Clean Streamlit web interface

Requirements:
-------------
- Python 3.8+
- OpenAI API key (for GPT fallback)
- Internet connection (for API access)

Installation:
-------------
1. Clone or download this repository.
2. Install dependencies:
   pip install streamlit openai

3. Set your OpenAI API key as an environment variable:
   On Linux/macOS:
   export OPENAI_API_KEY=your_key_here

   On Windows:
   set OPENAI_API_KEY=your_key_here

Running the App:
----------------
streamlit run chatbot_app.py

Then open the local URL printed in the terminal (usually http://localhost:8501).

File Overview:
--------------
- chatbot_app.py : Main Streamlit app
- README.txt     : Project overview and usage instructions

Customization:
--------------
You can edit the `qa_dict` dictionary inside `chatbot_app.py` to add more predefined Q&A pairs, or modify the behavior of the fallback GPT function.

Author:
-------
Saanvi Sethi
