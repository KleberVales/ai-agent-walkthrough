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

Contains the functions that the agent can invoke.

The project currently provides:

| Tool | Description |
|---|---|
| `add` | Adds two numbers |
| `multiply` | Multiplies two numbers |
| `divide` | Divides one number by another |
| `square_root` | Calculates the square root of a number |

The division tool prevents division by zero, while the square-root tool rejects negative numbers.

### `src/config`

Contains application configuration loaded from environment variables.

The project reads:

```text
OPENAI_API_KEY
MODEL_NAME
```

If `MODEL_NAME` is not defined, the application defaults to `gpt-5.5`.

### `src/main.py`

Provides the application entry point and sends a series of mathematical questions to the agent.

---

## 🛠️ Technologies

- [Python](https://www.python.org/)
- [LangChain](https://www.langchain.com/)
- [LangChain OpenAI](https://python.langchain.com/)
- [OpenAI](https://openai.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [pytest](https://pytest.org/)

---




