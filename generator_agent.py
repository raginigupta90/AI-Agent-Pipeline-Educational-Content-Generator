class GeneratorAgent:
    def generate(self, input_data, feedback=None):
        grade = input_data["grade"]
        topic = input_data["topic"]

        explanation = (
            "An angle is formed when two lines meet at a point. "
            "There are different types of angles. "
            "A right angle is exactly 90 degrees. "
            "An acute angle is less than 90 degrees. "
            "An obtuse angle is more than 90 degrees but less than 180 degrees."
        )

        # If reviewer gave feedback, simplify language
        if feedback:
            explanation = (
                "An angle is made when two lines meet. "
                "A right angle is like the corner of a book. "
                "An acute angle is smaller than a right angle. "
                "An obtuse angle is bigger than a right angle."
            )

        mcqs = [
            {
                "question": "Which angle is exactly 90 degrees?",
                "options": ["Acute angle", "Right angle", "Obtuse angle", "Straight angle"],
                "answer": "Right angle"
            },
            {
                "question": "Which angle is smaller than 90 degrees?",
                "options": ["Right angle", "Obtuse angle", "Acute angle", "Straight angle"],
                "answer": "Acute angle"
            }
        ]

        return {
            "explanation": explanation,
            "mcqs": mcqs
        }
