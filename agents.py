from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key was loaded correctly
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

# Initialize the LLM
llm = OpenAI(api_key=api_key, model="gpt-4-0125-preview")


# Create a senior blog content researcher agent
blog_researcher = Agent(
    role="Senior Blog Content Researcher",
    goal="Find and summarize highly relevant video content from the AI Learning Based YouTube channel for the topic: {topic}. Extract key information and insights.",
    verbose=True,
    memory=True,
    backstory=(
        "An expert in understanding complex technical concepts from videos "
        "in AI, Data Science, Machine Learning, Generative AI, and Agentic AI. "
        "You excel at sifting through video content to identify core ideas and insights."
    ),
    tools=[yt_tool],
    allow_delegation=True,
    llm=llm
)

# Create a senior blog writer agent
blog_writer = Agent(
    role="Senior Blog Writer",
    goal="Craft a compelling and educational blog post based on the researched video content for the topic: {topic}. Ensure clarity, engagement, and accuracy.",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex technical topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner. You transform raw "
        "research into polished, reader-friendly blog posts."
    ),
   
    allow_delegation=False,
    llm=llm
)