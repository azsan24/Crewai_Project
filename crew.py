from crewai import Crew,Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,  # Optional: Sequential task execution is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

## Start the task execution process with enhanced feedback
print("## Kicking off the Blog Generation Crew...")
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL vs Data Science'})
print("\n\n########################")
print("## Crew Work Completed!")
print("########################\n")
print(result)

# The blog post will also be saved to 'new-blog-post.md'
print("\nCheck 'new-blog-post.md' for the generated blog content.")