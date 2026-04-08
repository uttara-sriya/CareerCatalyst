# Sub-Agents

Specialized agents that handle specific aspects of resume optimization.

## Agents

### ATS Evaluator Agent
- **Purpose**: Calculates ATS (Applicant Tracking System) compatibility score
- **Input**: Resume text + Job description
- **Output**: Structured JSON with scores and keyword gap analysis
- **Model**: Gemini 2.5 Flash

### Strategy Advisor Agent
- **Purpose**: Analyzes evaluation results and provides actionable improvement recommendations
- **Input**: ATS evaluation results
- **Output**: Concrete modification plan with priority guidance
- **Model**: Gemini 2.5 Flash

### Resume Tailor Agent
- **Purpose**: Rewrites resume content to match target role
- **Input**: Original resume + Strategy recommendations
- **Output**: Tailored resume maintaining factual accuracy
- **Model**: Gemini 2.5 Flash

## Workflow

Agents execute sequentially (not in parallel) to ensure data consistency:

```
ATS Evaluator → Strategy Advisor → Resume Tailor
```
