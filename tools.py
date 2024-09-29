# https://docs.crewai.com/ - Visit this for the documentation of crewAI

#our tool for this is Youtube Channel RAG Search 

from crewai_tools import YoutubeChannelSearchTool


# Initialize the tool with a specific Youtube channel handle to target your search
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')