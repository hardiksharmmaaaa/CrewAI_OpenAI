from crewai import crew,Process
from agents import Blog_Researcher,Blog_writer
from tasks import research_task,write_task

# Forming the tech Focused crew with some enhanced configurations 

crew= crew(
    agents=[Blog_Researcher,Blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential, #optional: Sequential task execution is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
)

# Start the task execution process with the enhanced Feedback

result=crew.kickoff(inputs={"Roadmap To Crack Your First Data Science Job"})

print(result)