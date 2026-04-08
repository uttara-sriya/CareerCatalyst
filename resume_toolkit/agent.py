from google.adk.agents import Agent
from .sub_agents.resume_agents import resume_agent,personal_growth_agent,interview_prep_agent,get_skill_taxonomy

from .prompts import user_goal_instruction
root_agent = Agent(
    name="user_goal_agent",
    model="gemini-2.5-flash",
    description="The main orchestrator that manages the resume optimization pipeline.",
    instruction=user_goal_instruction,
    sub_agents=[
        resume_agent,
        personal_growth_agent,
        interview_prep_agent,
    ],
    tools=[get_skill_taxonomy],
    output_key="root_agent"
)