# 🤖 Ai Agent Walkthrough

A hands-on Python project demonstrating how to build a simple AI Agent with LangChain and OpenAI.

The project shows the fundamental building blocks of an AI agent:

- 🧠 LLM — OpenAI chat model
- 🛠️ Tools — Mathematical functions exposed to the agent
- 🔄 Agent loop — LangChain orchestrates the interaction between the model and tools
- ⚙️ Configuration — Environment variables loaded with python-dotenv
- 🧪 Testing — Mathematical tools covered with pytest

The goal is to provide a simple and practical example for understanding how an LLM can use external tools to solve problems.

## 🏗️ Architecture

The project follows a simple agent architecture:

```text
                    ┌──────────────────┐
                    │      User        │
                    │    Question      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   LangChain      │
                    │      Agent       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   OpenAI LLM     │
                    │   Chat Model     │
                    └────────┬─────────┘
                             │
                     Tool selection
                             │
                             ▼
              ┌────────────────────────────┐
              │       Math Tools           │
              ├────────────────────────────┤
              │  add                       │
              │  multiply                  │
              │  divide                    │
              │  square_root               │
              └─────────────┬──────────────┘
                            │
                            ▼
                    ┌──────────────────┐
                    │     Result       │
                    └──────────────────┘
```

The agent is created using LangChain's `create_agent`, receives a `ChatOpenAI` model, and is given the mathematical tools as its available tool set.

---

## 📂 Project Structure

```text
ai-agent-walkthrough/
│
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   └── math_agent.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   └── math_tools.py
│   │
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   ├── requirements.py
│   └── test_math_agent.py
│
├── .env
├── pyproject.toml
├── requirements.txt
└── README.md
```

### `src/agents`

Contains the agent implementation.

`math_agent.py` creates a `ChatOpenAI` instance and connects it to the available mathematical tools through LangChain's agent abstraction.

### `src/tools`




