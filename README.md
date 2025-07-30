# 🧪 LangChain SmolLM Demo

This project demonstrates a **LangChain pipeline using SmolLM (small language models)** — ideal for lightweight, efficient LLM experimentation. It showcases how to integrate small models into the LangChain agent framework with a Streamlit UI for interaction.

## 🚀 Features

- 🧠 Uses **SmolLM** for fast, low-resource inference
- 🔗 **LangChain** integration with agents/tools
- 💬 Streamlit-based chatbot interface
- 🧩 Modular setup — easy to plug in other models or tools


## 🧰 Tech Stack

- **Python 3.10+**
- **LangChain**
- **Streamlit**
- **SmolLM** (community-supported small LLM)
- **dotenv** for managing secrets


## 🧑‍💻 Installation

# 1. Clone the repo
git clone https://github.com/Kuntalsvyas/LangChain-Smollm-Demo.git
cd LangChain-Smollm-Demo

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your environment variables
# Inside a `.env` file:
API_KEY=your_api_key_if_needed

# 5. Run the app
streamlit run app.py

# 📈 How It Works
- User Input → Captured via Streamlit interface
- LangChain Agent → Processes input using SmolLM
- Tool Invocation → Use tools as needed based on the query
- Response → Displayed in chat interface

# 🧠 Use Cases
- Quick demos of LangChain workflows
- Lightweight chatbot development
- Testing agent-tool interactions with minimal overhead

# 📌 Future Enhancements
 - Add conversation memory
 - Multi-agent support
 - Plug-and-play custom tools
 - Comparison mode with Groq/OpenAI

# 🙌 Author
Created by Kuntal Vyas
Like it? ⭐ the repo and share your thoughts!
