from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI

agent = create_csv_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
    "employee-tech-stacks.csv",
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)


# Function to handle user input
def main():
    print("Welcome to the employee tech stack agent. Type 'quit' to exit.")
    while True:
        user_input = input("Enter your query: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        try:
            response = agent.run(user_input)
            print("Response:", response)
        except Exception as e:
            print("An error occurred:", e)

# Run the main function
if __name__ == "__main__":
    main()
