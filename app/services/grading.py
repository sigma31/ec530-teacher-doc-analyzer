import openai
from app.core.config import settings

openai.api_key = settings.openai_api_key


async def grade_student_answers(data: dict) -> list:
    student_name = data.get("student_name", "Unknown")
    student_id = data.get("student_id", "Unknown")
    answers = data.get("answers", [])

    graded_results = []

    for answer in answers:
        question = answer.get("question")
        student_answer = answer.get("student_answer")
        question_id = answer.get("question_id", -1)

        if not question or not student_answer:
            continue  # Skip incomplete entries

        prompt = f"""
You are a grading assistant.

Grade the following student's answer on a scale of 0 to 10.

Question:
"{question}"

Student's Answer:
"{student_answer}"

Respond in this JSON format:
{{
  "score": <number from 0-10>,
  "feedback": "<brief feedback on answer quality>"
}}
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful grading assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
            )

            raw_output = response['choices'][0]['message']['content']
            result = eval(raw_output) if raw_output.startswith("{") else {}
            graded_results.append({
                "question_id": question_id,
                "score": result.get("score", 0),
                "feedback": result.get("feedback", "No feedback provided."),
                "question": question,
                "student_answer": student_answer
            })

        except Exception as e:
            graded_results.append({
                "question_id": question_id,
                "score": 0,
                "feedback": f"Grading failed: {str(e)}",
                "question": question,
                "student_answer": student_answer
            })

    return graded_results
