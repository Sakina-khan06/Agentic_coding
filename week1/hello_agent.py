from agents import Agent, Runner
from llm import model

agent = Agent(
    name=pappo,
    instructions=""""# ROLE.',
 you are a pappo , 14-year-old
       model=model,
)

result = Runner.run_sync(agent, 'Write a joke about AI in roman Urdu.')
print(result.final_output)