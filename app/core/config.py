import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "Bullet Journal"
    PROJECT_VERSION: str = "0.0.1"

    ATLAS_URI: str = os.getenv("ATLAS_URI")
    DB_NAME: str = os.getenv("DB_NAME")

settings = Settings()