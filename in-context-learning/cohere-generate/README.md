**In-context learning for Natural Language Understanding with Cohere Medium Large Language Model**

This tutorial focuses on utilizing the Cohere Medium foundation model to achieve in-context learning. This involves leveraging the model's natural language understanding (NLU) capabilities to personalize user's responses and improve their performance. You will learn step-by-step how to perform NLU tasks using Cohere Medium. Specifically, you will learn how to engineer prompts that enable Cohere Medium to learn in-context and improve its performance, such as identifying named entities via few-shot learning. This will enhance the model's ability to infer context and answer questions, providing better responses to the user.

![Screen Shot 2023-03-30 at 8 48 14 PM](https://user-images.githubusercontent.com/11755966/229003092-756da4e0-6758-4c30-8bed-b3af986561c7.png)


**Prompting by Instruction: Zero Shot Learning**

*"This AI model is easy to use and has many helpful features. The text generation is especially accurate, which is important for people who are trying to stay creative."* What is the sentiment of the above review?


**Prompting by Instruction: Zero Shot Learning**

Please categorize the product reviews shown below as either positive, neutral, or negative.
*"[1] Absolutely love this AI Playground experience! It is easy to use and the model quality is outstanding."* 
*"[2] The topics covered in this introduction to LLM training were too deep and complex for me to understand."* 
*"[3] I need to investigate those performance claims by looking at the benchmarks on MLPerf."* 

**Prompting by Example 2: Few Shot Learning**

This program generates a startup idea and name given the industry.

Industry: Social entrepreneurship  
Startup Idea: A platform that helps the homeless locate warm and safe places to call home.
Startup Name: SafeHaven   
,,  

Industry: Home Decor  
Startup Idea: An app that calculates the most optimal position of your indoor succulents. 
Startup Name: Plant Buddy  
,,  

Industry: Recreation  
Startup Idea: Long distance micro ear plgus that help you coach your child while on the field, court, or mats
Startup Name: CopilotPlugs  
,, 

Industry: Education  
Startup Idea: Online curriculum that encourages the use of LLM's and GenerativeAI
Startup Name: NextGen AI  
,,  

Industry: Productivity  
Startup Idea:"""
