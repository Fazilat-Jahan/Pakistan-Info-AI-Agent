-
# 🇵🇰 Pakistan-Info AI Agent

This project is a **custom conversational AI assistant** designed specifically to **respond only to queries related to Pakistan**. It’s built using OpenAI's powerful **Agent SDK**, integrated with **Gemini 2.0 Flash** as the Large Language Model (LLM), and uses **Chainlit** to provide a simple and interactive chat interface.

---

## 💡 What It Does

* Read user messages through a Chainlit-powered interface.
* Sends the message to an AI agent built using the OpenAI Agent SDK.
* Uses **Gemini 2.0 Flash** (via API) as the underlying model to process the message.
* Filters responses:

  * If the message is about **Pakistan**, the agent replies intelligently.
  * If not, it returns a standard message:

    > *"I can only answer questions about Pakistan."*

---

## ⚙️ How It Works

* **Environment Configuration**:
  Loads the Gemini API key from a `.env` file using `python-dotenv`.

* **Gemini LLM Client**:
  Uses `AsyncOpenAI` (from the OpenAI Agent SDK) to communicate with the Gemini 2.0 Flash API endpoint.

* **OpenAI Agent SDK**:

  * The agent is created with specific instructions to restrict its knowledge and responses to Pakistan-related topics only.
  * A `Runner` is used to handle and route user input to the agent.

* **Chainlit Integration**:
  A message handler is created using Chainlit’s `@cl.on_message` decorator. It receives incoming messages and displays the AI's response in real time.

---

## 🧰 Technologies Used

| Tool/Library                 | Purpose                                      |
| ---------------------------- | -------------------------------------------- |
| **OpenAI Agent SDK**         | To define, run, and manage the AI agent      |
| **Gemini 2.0 Flash**         | LLM used for generating responses            |
| **Chainlit**                 | Provides real-time messaging and frontend UI |
| **dotenv (`python-dotenv`)** | Loads API keys securely from `.env` file     |
| **asyncio**                  | Handles asynchronous message processing      |

---

## 🧠 Agent Instructions

```text
"Only answer queries about Pakistan. If the question is not about Pakistan, say: 'I can only answer questions about Pakistan.'"
```

This ensures the assistant stays focused and consistent in its purpose.

---

## 📌 Use Case

This assistant can be used for:

* Educational purposes (e.g., students learning about Pakistan).
* Tourist support (answering travel-related questions about Pakistan).
* Cultural or historical Q\&A bots.
* Any platform needing a Pakistan-specific intelligent assistant.

---

