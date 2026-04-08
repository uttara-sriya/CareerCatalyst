# CareerCatalyst

An AI-powered resume optimization pipeline using multi-agent architecture. Analyzes resumes against job descriptions, provides improvement strategies, and tailors content for ATS compatibility.

## Features

- **ATS Evaluation**: Calculates compatibility scores by comparing resumes against job descriptions
- **Strategy Advisement**: Generates concrete improvement recommendations
- **Resume Tailoring**: Rewrites resumes to match target positions while maintaining accuracy
- **Document Processing**: Extracts text from PDF and DOCX files

## Quick Start

```bash
pip install -r requirements.txt
```

## Project Structure

- `resume_toolkit/` - Core agent orchestration and utilities
- `resume_toolkit/sub_agents/` - Specialized agents (ATS Evaluator, Strategy Advisor, Resume Tailor)
- `resume_toolkit/tools/` - Document processing utilities

See individual README files in each module for detailed documentation.