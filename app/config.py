from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO-URI")

DATABASE_NAME = os.getenv("DATABASE-NAME")

JWT_SECRET = os.getenv("JWT-SECRET")

JWT_ALGORITHM = os.getenv("JWT-ALGORITHM")

TOKEN_EXPIRE_MINUTES = int(
    os.getenv("TOKEN-EXPIRE-MINUTES", 60)
)