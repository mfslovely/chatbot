# chatbot

# 💬 LangChain Chatbot using Streamlit

A simple and powerful chatbot built with [LangChain](https://www.langchain.com/), [Streamlit](https://streamlit.io/), and OpenAI or Ollama models. You can ask questions and get intelligent responses using LLMs like `gpt-3.5-turbo` or local models via `Ollama`.

---

## 🚀 Features

- ✨ Natural language conversation
- 🤖 Uses OpenAI GPT-3.5 or local Ollama models
- 🧠 LangChain prompt templates and chaining
- 🖥️ Built with Streamlit UI
- 🔐 Environment variable management with `.env`
- ⚙️ FastAPI-compatible backend setup (optional for APIs)

---

## 📸 Demo

![Demo Screenshot](screenshot.png)

---

## 🧱 Tech Stack

- **Python 3.10+**
- [LangChain](https://python.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [OpenAI API](https://platform.openai.com/)
- [Ollama](https://ollama.com/) *(for local LLMs like LLaMA, Mistral, etc.)*
- [FastAPI](https://fastapi.tiangolo.com/) *(optional)*
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langchain-chatbot.git
cd langchain-chatbot
````

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Create `.env` file

```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name
```

> ⚠️ **Do not share or commit your `.env` file.** It is added to `.gitignore` for safety.

---

## 🧪 Running the App

### ✅ With Streamlit

```bash
streamlit run app.py
```

---

## 🧠 Using Ollama (Optional)

Install [Ollama](https://ollama.com/) and pull a model:

```bash
ollama run llama3
```

In your code, replace OpenAI with:

```python
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")
```

---

## 📁 Project Structure

```
├── app.py                 # Main Streamlit app
├── .env                  # Environment variables (ignored by git)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore rules
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

Made with ❤️ by [Lovely Gupta](mailto:lovelygupta016@example.com)

```

---

```

