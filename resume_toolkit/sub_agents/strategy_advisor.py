from google.adk.agents import Agent
from ..prompts import strategy_advisor_instruction
strategy_agent = Agent(
    name="strategy_advisor_agent",
    model="gemini-2.5-flash",
    description="Analyzes the resume and provides concrete suggestions to improve the ATS score.",
    instruction=strategy_advisor_instruction)