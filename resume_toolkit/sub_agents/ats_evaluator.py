from google.adk.agents import Agent

from ..prompts import ats_evaluator_instruction
ats_agent = Agent(
    name="ats_evaluator_agent",
    model="gemini-2.5-flash",
    description="Calculates the current ATS score by comparing a resume against a Job Description.",
    instruction= ats_evaluator_instruction,
    output_key="ats_agent"

)