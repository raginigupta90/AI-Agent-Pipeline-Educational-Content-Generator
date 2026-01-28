# AI Agent Pipeline – Educational Content Generator

## Overview

This project implements a lightweight agent-based AI pipeline to generate and review educational content for school students.

It demonstrates how multiple AI agents can collaborate in a controlled workflow using structured inputs and outputs, without relying on heavy frameworks.

The system consists of:
- A **Generator Agent** that creates draft educational content
- A **Reviewer Agent** that evaluates the generated content
- A **Command-Line UI** that triggers the agent pipeline and displays each stage clearly

The project is built using pure Python and is designed to run on Windows via Command Prompt (CMD).

---

## Agent Architecture

User (CLI UI)
↓
Generator Agent
↓
Reviewer Agent
↓
(Optional Refinement Pass)
↓
Final Output Display


---

## Agents Description

### 1. Generator Agent

**Responsibility:**  
Generates draft educational content based on grade and topic.

#### Input (Structured)

```
{
  "grade": 4,
  "topic": "Types of angles"
}
Output (Structured)
{
  "explanation": "Text explanation...",
  "mcqs": [
    {
      "question": "Question text",
      "options": ["A", "B", "C", "D"],
      "answer": "Correct option"
    }
  ]
}
```
## Key Features
Language adjusted to the student’s grade level

Correct academic concepts

Deterministic JSON structure

### 2. Reviewer Agent

**Responsibility:**
Evaluates the Generator Agent’s output.
Evaluation Criteria
Age appropriateness
Conceptual correctness
Clarity of explanation

####Output (Structured)
```
{
  "status": "pass | fail",
  "feedback": [
    "Specific feedback messages"
  ]
}
```
## Refinement Logic
If the Reviewer Agent returns fail, the Generator Agent is re-run once

Reviewer feedback is embedded into the second generation

Only one refinement pass is allowed, as per requirements

## User Interface (CLI)
The project includes a command-line interface that:

Triggers the agent pipeline

## Displays:

Generator output

Reviewer feedback

Refined output (if applicable)

Clearly shows the agent flow

No external UI frameworks are used.

## Project Structure
```
AI agent pipeline/
│
├── generator_agent.py   # Generator Agent logic
├── reviewer_agent.py    # Reviewer Agent logic
├── main.py              # CLI UI and agent pipeline
└── README.md
```
## How to Run (Windows CMD)
Step 1: Open Command Prompt
Win + R → cmd → Enter
Step 2: Navigate to Project Folder
cd "C:\college\internship\INTERNSHIP TASK\AI agent pipeline"
Step 3: Run the Program
python main.py
Sample Output Flow

Generator creates educational content

Reviewer evaluates the content

If issues are found, refinement is triggered

Final results are displayed in the terminal

## Technologies Used
Python 3.x

Standard Python libraries (json)

Command Line Interface (CMD)

## Why This Design
Keeps the system simple and transparent

Clearly demonstrates agent responsibilities

Follows structured input/output contracts

Meets all requirements of the AI agent assessment

## Notes
No external AI frameworks were used

The focus is on agent logic and interaction, not model training

The project is intentionally lightweight and easy to extend

## Possible Extensions
Support for multiple grades and topics

Web UI using Streamlit or Flask

Logging and scoring metrics

REST API integration

## Author
Ragini Gupta
