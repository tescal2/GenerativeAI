# Langchain Tutorial
**Building a Modular Reasoning, Knowledge and Language (MRKL) application**

![Screen Shot 2023-03-31 at 6 50 42 PM](https://user-images.githubusercontent.com/11755966/229252064-73092168-ce65-40e6-b1af-4f5549c9fa00.png)

As of March 2023, LLM's like ChatGPT still have a knowledge cutoff date. In order to overcome this limitation, you can use a technique called Prompt chaining which links another source of information to the LLM for retrieval. The internet is a great example to supercharge an LLM with up to date information. This repository uses an application that provides `text-davinci-003` witha ccessw to the internet using Langchain. For deomnstration purposes, we limit this app to just search, however, you can certainly build more integrations such as WolframAlpha, a private database, etc. 

**Execution:**

1. Ensure that you install [langchain](https://python.langchain.com/en/latest/#) in order to have the latest working version. You can do this by simply opening a new Terminal window and executing the following command: 
`pip3 install langchain`

2. Update your environment files with your OpenAI and SerpAI API Keys

3. Run and Debug the app to view the new query results.

Helpful Tip: You can very well add stop breaks during your deubugging code to look at each script that runs within Langchain as the agents are communicating with the LLM and facilitating the retrieval process. The files you wuld look at are:

`langchain_chat.py`
`google_serper.py`
`agent.py`




**Under the Hood: High Level Architecture**

![Screen Shot 2023-03-31 at 6 54 14 PM](https://user-images.githubusercontent.com/11755966/229252072-5febf65a-20ad-444a-b0e6-9d6bad9bff98.png)

A query from the user asking for recent information that an LLM was not trained on. Langchain provides an agent that takes the query and provides a set of instruction to the LLM. If the LLM needs to query the internet, then it will do so 

**OpenAI Playground Instruction Testing**

The OpenAI playground will allow us to better understand the prompting instructions derived from the agents. Through debugging the `mrkl_app.py` and stopping it prior to the response, we are able to view the instructions from the agents. That instruction has been copied and uploaded as part of the repository.

1. Use the `playground_prompt.txt` file as the prompt for the `text-davinci-003 model` with the OpenAI Playground
2. Set the temperature to 0 and the maxium length to ~1000
3. Set a Stop sequennce word of "Observation" because we want to stop the prompt as it reached its observation. We do this to show the action the model wants to take (which is Search).

![Screen Shot 2023-03-31 at 7 14 29 PM](https://user-images.githubusercontent.com/11755966/229255720-b2995a22-0313-4b52-8fbb-3a84a0230d17.png)

The LLM understands that it should first do a search in order to find out what the most important takeaways were. Given the instruction prompt, it provides an `Action: Search` and `Action Input: Jensen Huang GTC keynote March 21st 2023`. The agent assumes this responsiblity through a python script that runs the search using the Serper API tool. The agent will then parse the API response from the internet and amend the instruction prompt with the search result. The agent sends this updated insuctrion prompt back to the LLM in which the final response is generated back to the user. 






