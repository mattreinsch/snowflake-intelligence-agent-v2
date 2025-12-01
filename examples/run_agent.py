from snowflake_intelligence_agent.agent_core import Agent

def main():
    """
    Main function to run the Snowflake Intelligence Agent.
    """
    # Example usage:
    # 1. Instantiate the agent
    agent = Agent()

    # 2. Define a user request
    user_request = "What were the total sales for the last quarter?"

    # 3. Run the agent with the user request
    result = agent.run(user_request)

    # 4. Print the result
    print(result)

if __name__ == "__main__":
    main()
