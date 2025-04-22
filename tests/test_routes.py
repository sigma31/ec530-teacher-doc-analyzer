import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_upload_and_grade():
    # Simulated student answer
    student_data = {
        "student_name": "Test Student",
        "student_id": "T001",
        "answers": [
            {
                "question_id": 1,
                "question": "What is an API?",
                "student_answer": "An API lets apps communicate."
            }
        ]
    }

    # Save as JSON and send as file upload
    import io, json
    json_file = io.BytesIO(json.dumps(student_data).encode("utf-8"))
    json_file.name = "test.json"

    response = client.post("/api/grade", files={"file": ("test.json", json_file, "application/json")})
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "results" in response.json()


def test_get_all_results():
    response = client.get("/api/results")
    assert response.status_code == 200
    assert "results" in response.json()
