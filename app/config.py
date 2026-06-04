from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

DATABASE_NAME = os.getenv("DATABASE_NAME")

JWT_SECRET = os.getenv("JWT_SECRET")

JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

TOKEN_EXPIRE_MINUTES = int(
    os.getenv("TOKEN_EXPIRE_MINUTES", 60)
)