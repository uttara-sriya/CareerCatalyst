# Resume Toolkit

Core orchestration layer for the CareerCatalyst resume optimization pipeline.

## Overview

The toolkit coordinates three specialized sub-agents through a sequential workflow:
1. **Ingestion** - Collect resume and job description
2. **Assessment** - Evaluate ATS compatibility
3. **Strategy** - Generate improvement recommendations
4. **Execution** - Tailor resume to target role
5. **Output** - Save optimized resume

## Key Components

- `agent.py` - Main orchestrator agent (Gemini 2.5 Flash)
- `prompts.py` - Instruction templates for orchestrator and sub-agents
- `sub_agents/` - Specialized agent implementations
- `tools/` - Document processing utilities

## Usage

```python
from resume_toolkit.agent import root_agent

# The orchestrator handles the full workflow
```

## Dependencies

- google-adk >= 1.14.0
- langchain-community >= 0.3.27
