import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

password = os.getenv("HASLO")

engine = create_engine(
    f"postgresql://postgres:{password}@localhost:5432/postgres"
)