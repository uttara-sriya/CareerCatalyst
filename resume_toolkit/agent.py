from google.adk.agents import Agent
from .sub_agents.ats_evaluator import ats_agent
from .sub_agents.strategy_advisor import strategy_agent
from .sub_agents.resume_tailor import tailor_agent
from .prompts import orchestrator_instruction
root_agent = Agent(
    name="orchestrator_agent",
    model="gemini-2.5-flash",
    description="The main orchestrator that manages the resume optimization pipeline.",
    instruction=orchestrator_instruction,
    sub_agents=[
        ats_agent,
        strategy_agent,
        tailor_agent,

    ],
    output_key="root_agent"
)