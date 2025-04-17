from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.grading import grade_student_answers
import json

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

        return {"status": "success", "results": graded_results}

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
