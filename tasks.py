from crewai import Task
from tools import tool 
from agents import Blog_Researcher,Blog_writer

# Research Task 

research_task=Task(
    description=(
        "Identify the video {}."
        "Get detailed information about the video from the channel."
    ),
    expected_output="A comprehensive 3 Paragraphs long report based on the {topic} of the video"
    tools=[yt_tool],
    agent=Blog_Researcher,
)

# Writing Task with language model Config.

write_task=Task(
    description=(
        "get the info from the youtube channel on the topic {topic} and create the content for the blog "
    ),
    expected_output="Summarize the info from the youtube channel video on the topic {topic} of the video"
    tools=[yt_tool],
    agent=Blog_writer,
    async_execution=False,  #async Execution means that if we set async-execution =True, then it means that both the process run parallely 
    output_file="new-blog-post.md" # Example of the output customisation
)