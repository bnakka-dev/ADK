import os
from dotenv import load_dotenv
from __future__ import annotations
from google.adk.agents import Agent
load_dotenv()
model_name = os.getenv("ADK_MODEL")
# ADK always looks for a variable named 'root_agent'
root_agent = Agent(
    name="BusinessAnalyst",
    model=model_name,
    instruction="""You are an expert AI & Data Engineer assistant. 
    Your goal is to help users identify business pain points and 
    suggest RPA or ML solutions. Keep answers crisp and technical."""
)
