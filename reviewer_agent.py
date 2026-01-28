# reviewer_agent.py

class ReviewerAgent:
    def review(self, content):
        feedback = []

        explanation = content["explanation"]

        if len(explanation.split()) > 60:
            feedback.append("Explanation is too long for Grade 4 students.")

        if "180 degrees" in explanation:
            feedback.append("Straight angle concept is not explained but mentioned.")

        if not content["mcqs"]:
            feedback.append("No questions provided.")

        status = "pass" if not feedback else "fail"

        return {
            "status": status,
            "feedback": feedback
        }
