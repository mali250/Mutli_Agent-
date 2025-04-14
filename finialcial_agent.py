import os
from dotenv import load_dotenv

import openai
import phi
from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.playground import Playground, serve_playground_app
from phi.tools import Tool
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

# Load environment variables
load_dotenv()

# Set OpenAI and Phi API keys
openai.api_key = os.getenv("OPENAI_API_KEY")
phi.api = os.getenv("PHI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# ✅ Explicitly pass api_key to Groq
groq_model = Groq(
    id="llama3-70b-8192",
    api_key=groq_api_key
)

# Create Web Search Agent using DuckDuckGo
web_search_agent = Agent(
    name="Web Search Agent",
    role="search on web for information",
    model=groq_model,
    tools=[DuckDuckGo()],
    instruction="Always include Resources",
    show_tools_calls=True,
    markdown=True,
)

# Create Finance Agent using YFinanceTools
finance_agent = Agent(
    name="Finance Agent",
    role="provide financial data",
    model=groq_model,
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
            # key_financials_ratios=True,  # Uncomment if needed
        )
    ],
    instruction="Use Tables to Display Data",
    show_tools_calls=True,
    markdown=True,
)


multi_ai_agent = Agent(
    model=Groq(id="llama3.1-70b-versatile"),
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)
    

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True)



