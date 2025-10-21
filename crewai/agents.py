from crewai import Agent 
from tools import tool 
# Create a senior blog content researcher 
blog_researcher = Agent(
    role = 'Blog Researcher from Youtube Videos',
    goal = 'get the relevant video content for the topic {topic} from Youtube Channel',
    verbose = True,
    memory = True,
    backstory=(
        'Expert in understanding videos in Data Science and AI Data Science, Machine Learning and Gen AI and providing suggestion.'
    ),
    tools = [tool],
    allow_delegation = True
)

# Creating a Senior Blog Writer Agent with Yt Tool
blog_writer = Agent(
    role = 'Writer',
    goal = 'Narrate compelling tech stories about the video {topic} from Youtube Channel',
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplyfying complex tech topics, You craft engaging narratives that captivate readers and make technology accessible to all."
    ),
    tools = [tool],
    allow_delegation = False
)
