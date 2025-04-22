# create_tables.py (run this once manually)

from app.db.base import Base, engine
from app.db import models

Base.metadata.create_all(bind=engine)
print("Tables created ✅")
