from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class GradedAnswer(Base):
    __tablename__ = "graded_answers"

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String)
    student_id = Column(String)
    question_id = Column(Integer)
    question = Column(String)
    student_answer = Column(String)
    score = Column(Float)
    feedback = Column(String)
