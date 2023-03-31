# Langchain Tutorial - Building a Modular Reasoning, Knowledge and Language (MRKL) application



As of March 2023, LLM's like ChatGPT still have a knowledge cutoff date. In order to overcome this limitation, you can use a technique called Prompt chaining which links another source of information to the LLM for retrieval. The internet is a great example to supercharge an LLM with up to date information. This repository uses an application that provides text-davinci-003 witha ccessw to the internet using Langchain. For deomnstration purposes, we limit this app to just search, however, you can certainly build more integrations such as Wol



You have the ability 
[1] Ensure that you install langchain in order to have the latest working version. You can do this by simply opening a new Terminal window and executing the following command: 
pip3 install langchain

[2] Update your environment files with your OpenAI and SerpAI API Keys

[3] Run and Debug the app to view the new query results.


**OpenAI Playground Testing**

- Use the playground_prompt.txt file as the prompt for the text-davinci-003 model
- Set a Stop sequennce word of "Observation" because we want to stop the prompt to show the action the model wants to take (which is Search)





Helpful Tip: You can very well add stop breaks during your deubugging code to look at each script that runs within Langchain as the agents are communicating with the LLM and facilitating the retrieval process. The files you wuld look at are: 

langchain_chat.py
google_serper.py



**Under the Hood: High Level Architecture**

A query from the user asking for recent information. Langchain provides an agent that takes the query and provides a set of instruction to the LLM. If the LLM needs to query the internet, then it will do so 
