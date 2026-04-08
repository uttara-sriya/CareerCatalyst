from google.adk.agents import Agent

from ..prompts import resume_instruction,personal_growth_instruction,interview_prep_instruction
resume_agent = Agent(
    name="resume_agent",
    model="gemini-2.5-flash",
    description="Agent that transforms raw work history into quantified, STAR-method narratives, tailors resumes to specific job descriptions, and autonomously",
    instruction= resume_instruction,
    output_key="resume_agent_output"

)
personal_growth_agent = Agent(
    name="personal_growth_agent",
    model="gemini-2.5-flash",
    description="the agent acts as a neutral evaluator, identifying patterns in technical gaps or communication styles to provide a roadmap for iterative improvement.",
    instruction= personal_growth_instruction,
    output_key="personal_growth_output"

)
interview_prep_agent = Agent(
    name="interview_prep_agent",
    model="gemini-2.5-flash",
    description="the agent acts as a neutral evaluator, identifying patterns in technical gaps or communication styles to provide a roadmap for iterative improvement.",
    instruction= interview_prep_instruction,
    output_key="interview_prep_output"

)


# from google.adk.agents import Tool

def get_skill_taxonomy(category: str = "all") -> str:
    """
    Returns a comprehensive mapping of required skills and keywords 
    for various data engineering and AI roles.
    """
    taxonomy = """
    DATA_ENGINEERING:
        - Languages: Python, Java, Scala, SQL
        - Frameworks: Apache Spark (PySpark), Flink, Beam
        - Storage: Delta Lake, Apache Iceberg, HDFS, S3
        - Databases: AlloyDB, PostgreSQL, BigQuery, DynamoDB
    
    GENERATIVE_AI:
        - Frameworks: LangChain, Google ADK, CrewAI
        - Models: Gemini, Claude, GPT-4
        - Vector DBs: pgvector (AlloyDB), Pinecone, Weaviate
        - Techniques: RAG, Prompt Engineering, Agentic Workflows
    
    SYSTEM_DESIGN:
        - Concepts: Scalability, Latency, Throughput, CAP Theorem
        - Architecture: Microservices, Event-driven (Kafka), Lambda/Kappa
    """
    
    # Return the whole thing or a specific subset
    if category.lower() == "all":
        return taxonomy
    return f"Requested skills for {category}: " + (taxonomy if category.upper() in taxonomy else "Category not found.")

# skill_tool = Tool(
#     name="skill_taxonomy_search",
#     func=get_skill_taxonomy,
#     description="Provides a static list of industry-standard skills and keywords for technical roles."
# )