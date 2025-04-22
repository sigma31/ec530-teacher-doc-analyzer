from sqlalchemy.orm import Session
from app.db import models

def save_graded_answers(db: Session, student_name: str, student_id: str, results: list):
    for result in results:
        entry = models.GradedAnswer(
            student_name=student_name,
            student_id=student_id,
            question_id=result["question_id"],
            question=result["question"],
            student_answer=result["student_answer"],
            score=result["score"],
            feedback=result["feedback"]
        )
        db.add(entry)
    db.commit()

def get_all_results(db: Session):
    return db.query(models.GradedAnswer).all()

def get_results_by_student_id(db: Session, student_id: str):
    return db.query(models.GradedAnswer).filter(models.GradedAnswer.student_id == student_id).all()