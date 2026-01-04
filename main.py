from agno.agent import Agent
from agno.tools.browserbase import BrowserbaseTools
from decouple import config
import os
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

# Create scraping agent  
agent = Agent(
    name="Web Scraper",
    tools=[BrowserbaseTools(api_key=config("BROWSERBASE_API_KEY"), 
        project_id=config("BROWSERBASE_PROJECT_ID"))],
    instructions=[
        "Extract content clearly and format nicely",
        "Always close sessions when done"
    ],
    markdown=True,
)

# Scrape quotes
response = agent.run("""
    Go to https://www.airbnb.co.uk/s/Cape-Town--South-Africa/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJ1-4miA9QzB0Rh6ooKPzhf2g&location_bb=wgXilUGYCZDCCXBxQZJ1qA%3D%3D&acp_id=5588dd9b-91e9-431e-b093-70fd464a5cb9&date_picker_type=calendar&checkin=2026-01-15&checkout=2026-02-17&search_type=autocomplete_click and:
    Extract 2 properties from the page in the following format:
    [
        {"name": "string", "price": "number", "image": "string"}
    ]
""")

print(response.content)