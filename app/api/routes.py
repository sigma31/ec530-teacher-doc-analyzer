from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.grading import grade_student_answers
import json
from app.db.base import SessionLocal
from app.db.crud import save_graded_answers

router = APIRouter()


@router.post("/grade")
async def grade_answers(file: UploadFile = File(...)):
    # Check file type
    if not file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="Only JSON files are supported.")

    try:
        # Read and parse file content
        contents = await file.read()
        data = json.loads(contents)

        # Call grading logic
        graded_results = await grade_student_answers(data)
        
        db = SessionLocal()
        save_graded_answers(db, student_name=data.get("student_name"), student_id=data.get("student_id"), results=graded_results)
        db.close()

        return {"status": "success", "results": graded_results}

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
