import argparse
import requests
import os
import json

API_URL = "http://localhost:8000/api/grade"

def upload_file(json_path):
    if not os.path.exists(json_path):
        print(f"File not found: {json_path}")
        return

    with open(json_path, "rb") as f:
        files = {"file": (os.path.basename(json_path), f, "application/json")}
        try:
            response = requests.post(API_URL, files=files)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error sending request: {e}")
            return

    data = response.json()
    print("Response from server:\n")

    print(json.dumps(data, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Upload student JSON answer sheet to grading API.")
    parser.add_argument("filepath", help="Path to JSON file with student answers")

    args = parser.parse_args()
    upload_file(args.filepath)

if __name__ == "__main__":
    main()
