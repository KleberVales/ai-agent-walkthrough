from agents.math_agent import create_math_agent


def main():
    agent = create_math_agent()

    questions = [
        "What is 42 plus 58?",
        "What is 15 times 8 and then divide the result by 3?",
        "A rectangle has a width of 12 and a height of 7. What is its area and what is the square root of the area?",
    ]

    for question in questions:
        print("\n" + "=" * 60)
        print(f"Question: {question}")

        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question,
                    }
                ]
            }
        )

        print(f"Answer: {result['messages'][-1].content}")


if __name__ == "__main__":
    main()