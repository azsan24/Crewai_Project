from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

## Research Task
research_task = Task(
    description=(
        "Using the YoutubeChannelSearchTool, identify relevant videos on the AI Learning Youtube channel related to the topic: '{topic}'. "
        "Analyze the content of the identified videos to extract key concepts, definitions, comparisons, and important takeaways regarding '{topic}'. "
        "Focus on the main differences, applications, and evolution of AI, ML, DL, and Data Science as discussed in the videos."
    ),
    expected_output=(
        "A comprehensive 3-paragraph report summarizing the core information "
        "about '{topic}' found in the AI Learning YouTube videos. "
        "The report should clearly distinguish between AI, ML, DL, and Data Science, "
        "highlighting their relationships and unique aspects as presented in the video content."
    ),
    tools=[yt_tool],
    agent=blog_researcher,
)

# Writing task with language model configuration
write_task = Task(
    description=(
        "Using the research report provided by the 'Senior Blog Content Researcher' on '{topic}', "
        "write a compelling and informative blog post. "
        "The blog post should introduce the topic, clearly explain and differentiate AI, ML, DL, and Data Science, "
        "and provide engaging insights. Structure the blog post with an introduction, "
        "separate sections for each concept (or combined thoughtfully), and a conclusion. "
        "Ensure the language is accessible to a tech-savvy but non-expert audience."
    ),
    expected_output=(
        "A well-structured, engaging, and informative blog post of approximately 500-700 words "
        "about '{topic}'. The post should clearly differentiate AI, ML, DL, and Data Science, "
        "and be ready for publication. "
        "Format it using Markdown for headings and paragraphs."
    ),
    agent=blog_writer,
    # The writer doesn't need the yt_tool here, as it's consuming the researcher's output.
    tools=[],
    async_execution=False,
    output_file='new-blog-post.md'  # Example of output customization
)