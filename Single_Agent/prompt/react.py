REACT_PROMPT = """Answer the following questions as best you can. You have access to the following tools:
{tool_descs}
Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin! 
Question: {query}"""



# "注意: 你应该在下文中查找问题答案是否存在，如果这个问题的答案已经存在,返回较为精炼的答案即可。否则, 执行上述过程。"