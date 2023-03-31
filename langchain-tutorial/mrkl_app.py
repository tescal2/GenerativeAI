import os
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool

os.environ["SERPER_API_KEY"] = "<YOUR_SERPER_API_KEY>"
os.environ["OPENAI_API_KEY"] = "<YOUR_OPENAI_API_KEY>"

# define your LLM which at the moment is GPT3.5
llm = OpenAI(temperature=0)
# define the the API for a goolg search
search = GoogleSerperAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for when you need to answer questions about current events. You should ask targeted questions"
    )
]

# provide the agent with access to the llm
mrkl = initialize_agent(tools, llm, agent="zero-shot-react-description")

query = "What were the most important takeaways from Jensen Huang's GTC keynote on March 21st, 2023?"

response = mrkl.run(query)
print(f"Query: {query}\n\nResponse: {response}")
