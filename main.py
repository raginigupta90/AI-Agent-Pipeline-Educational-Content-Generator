# main.py

from generator_agent import GeneratorAgent
from reviewer_agent import ReviewerAgent
import json

def main():
    print("\n=== AI Agent-Based Educational Content Generator ===\n")

    user_input = {
        "grade": 4,
        "topic": "Types of angles"
    }

    generator = GeneratorAgent()
    reviewer = ReviewerAgent()

    # First generation
    generated_content = generator.generate(user_input)

    print("Generator Output:")
    print(json.dumps(generated_content, indent=2))

    review_result = reviewer.review(generated_content)

    print("\n Reviewer Feedback:")
    print(json.dumps(review_result, indent=2))

    # Refinement logic (ONLY ONE PASS)
    if review_result["status"] == "fail":
        print("\n Refining content based on feedback...\n")
        refined_content = generator.generate(
            user_input,
            feedback=review_result["feedback"]
        )

        print("Refined Generator Output:")
        print(json.dumps(refined_content, indent=2))

    print("\n=== End of Agent Flow ===\n")

if __name__ == "__main__":
    main()
