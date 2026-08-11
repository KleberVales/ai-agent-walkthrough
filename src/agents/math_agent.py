from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from config.settings import MODEL_NAME
from tools.math_tools import MATH_TOOLS


def create_math_agent():
    """Create and configure the math agent."""

    model = ChatOpenAI(
        model=MODEL_NAME,
    )

    agent = create_agent(
        model=model,
        tools=MATH_TOOLS,
    )

    return agent