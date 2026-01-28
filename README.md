# AI Agent Pipeline – Educational Content Generator

A lightweight **agent-based AI pipeline** implemented in Python that generates and reviews educational content for school students.  
The project demonstrates **agent collaboration**, **structured input/output**, and a **review–refine workflow**, all exposed through a simple **command-line interface (CLI)**.

---

##  Features

- Two clearly defined AI agents:
  - **Generator Agent** – creates educational content
  - **Reviewer Agent** – evaluates content quality
- Structured JSON-based communication between agents
- One-pass refinement logic based on reviewer feedback
- Simple and transparent CLI-based UI
- No external frameworks required

---

##  Agent Architecture

User (CLI)
↓
Generator Agent
↓
Reviewer Agent
↓
(Optional Refinement)
↓
Final Output


---

##  Agents Description

### Generator Agent

**Responsibility:**  
Generates draft educational content for a given grade and topic.

**Input (Structured):**
```json
{
  "grade": 4,
  "topic": "Types of angles"
}
Output (Structured):

{
  "explanation": "Explanation text",
  "mcqs": [
    {
      "question": "Question text",
      "options": ["A", "B", "C", "D"],
      "answer": "Correct option"
    }
  ]
}

##Key Characteristics:

Grade-appropriate language

Conceptually correct content

Deterministic output structure

Reviewer Agent

##Responsibility:
Evaluates the generated content for quality and suitability.

Evaluation Criteria:

Age appropriateness

Conceptual correctness

Clarity of explanation

**Output (Structured):**

{
  "status": "pass | fail",
  "feedback": [
    "Specific feedback messages"
  ]
}

##Refinement Logic

If the Reviewer Agent returns fail, the Generator Agent is re-run once.

Reviewer feedback is embedded into the second generation.

Only one refinement pass is allowed.

##Command-Line UI

The CLI:

Triggers the full agent pipeline

Displays:

Generator output

Reviewer feedback

Refined output

Makes the agent flow explicit and easy to follow

📁 Project Structure
AI-agent-pipeline/
│
├── generator_agent.py   # Generator Agent logic
├── reviewer_agent.py    # Reviewer Agent logic
├── main.py              # CLI UI and agent pipeline
└── README.md

##How to Run (Windows CMD)

1️⃣ Open Command Prompt
Win + R → cmd → Enter
2️⃣ Navigate to Project Directory
cd "C:\college\internship\INTERNSHIP TASK\AI agent pipeline"
3️⃣ Run the Program
python main.py
Sample Execution Flow
Generator Agent produces educational content

Reviewer Agent evaluates the content

Refinement is triggered if issues are found

Final results are displayed in the terminal

##Technologies Used
Python 3.x

Standard Python libraries (json)

Windows Command Prompt (CMD)

 ##Design Rationale
Keeps the system simple and interpretable

Clearly separates agent responsibilities

Demonstrates structured agent communication

Fully aligns with agent-based AI assessment requirements

##Possible Extensions
Support for multiple grades and topics

Web-based UI using Streamlit or Flask

Logging and scoring mechanisms

REST API version of the agent pipeline

##Author
Ragini Gupta
