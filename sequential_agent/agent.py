import os
from dotenv import load_dotenv
load_dotenv()
from __future__ import annotations
from google.adk.agents import Agent, SequentialAgent
model_name = os.getenv("ADK_MODEL")
# ADK always looks for a variable named 'root_agent'

# 1. The "Creative" Brain (Prone to making things up)
creative_agent = Agent(
    name="Generator",
    model=model_name,
    instruction="""You are a highly creative assistant. Provide detailed answers. 
    If you are unsure about a fact, make a plausible guess but keep the tone confident."""
)

# 2. The "Skeptic" Brain (The Hallucination Spotter)
skeptic_agent = Agent(
    name="FactChecker",
    model=model_name,
    instruction="""You are a professional fact-checker. Review the Generator's output. 
    Look for specific names, dates, or technical claims. 
    If something sounds like a hallucination or 'low confidence' guess, 
    interrupt and state: 'I need a source for [X]'. 
    If it looks good, just say 'Verified'."""
)

# 3. The Orchestrator (The "Bridge")
root_agent = SequentialAgent(
    name="DualBrainSystem",
    sub_agents=[creative_agent, skeptic_agent] 
)