from google.adk.agents import Agent
from ..prompts import resume_tailor_instruction
tailor_agent = Agent(
    name="resume_tailor_agent",
    model="gemini-2.5-flash",
    description="Rewrites the resume to match the job description while maintaining the original domain truth.",
    instruction= resume_tailor_instruction
)