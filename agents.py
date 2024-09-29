from crewai import Agent
from tools import yt_tool
import os

from dotenv import load_dotenv
load_dotenv()

os.environ["OPEN_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

## Create a Senior Blog Content Researcher #1st Agent 

Blog_Researcher=Agent(
    role="Blog Researcher from Youtube Videos",
    goal="get the relevant video content for the topic {topic} from the Youtube Channel",
    verbose=True, # When set to True, it indicates that the "Blog Researcher" agent will provide detailed information during its process
    memory=True, # This suggests that the agent will store or retain information from previous interactions
    backstory=(
        "Expert in Understanding Videos in AI, Data Science, Machine Learning and Generative AI and providing Suggestion"
    ),
    tools=[yt_tool],
    llm= llm,
    allow_delegation=True  # will I be transfering the work to someone else After this??
    )

## Create a Senior Blog Writing Agent with YT Tool #2nd Agent 

Blog_writer=Agent(
    role="Blog Writer",
    goal="Narrate Tech Stories about the video {topic} ",
    verbose=True, # When set to True, it indicates that the "Blog Researcher" agent will provide detailed information during its process
    memory=True, # This suggests that the agent will store or retain information from previous interactions
    backstory=(
        "With a Flair for simplifying Complex topics, you craft"
        "Engaging with narratives that captivate and educate,bringing the new"
        "discoveries to light in an accessible manner"
    ),
    tools=[yt_tool],
    llm= llm,
    allow_delegation=False  # will I be transfering the work to someone else After this??
)
