from __future__ import annotations
from google.adk.agents import Agent
import os
from dotenv import load_dotenv
load_dotenv()
model_name = os.getenv("ADK_MODEL")
from .tools import get_exchange_rate  # Import your new tool

root_agent = Agent(
    name="FinanceAssistant",
    model=model_name,
    instruction="You are a helpful finance assistant. Use the exchange rate tool for currency queries and provide a clear and concise response.",
    tools=[get_exchange_rate]  # <-- Register the tool here
)