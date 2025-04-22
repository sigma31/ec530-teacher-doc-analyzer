#!/bin/bash

# Exit on any error
set -e

echo "✅ Setting PYTHONPATH to current directory..."
export PYTHONPATH=$(pwd)

echo "🛠️  Creating database tables..."
python3 app/db/create_tables.py

echo "🚀 Starting FastAPI server with uvicorn..."
uvicorn app.main:app --reload