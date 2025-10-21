import os 
from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
# Forming the tech-focused crew with some enhanced settings 
crew = Crew(
    agents = [blog_researcher, blog_writer],
    tasks = [research_task, write_task],
    process = Process.sequential,
    memory = True, 
    cache = True,
    max_rpm = 100, 
    share_crew = True
)

# Start the task execution with enhanced feedback 
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL VS Data Science'})
print(result)