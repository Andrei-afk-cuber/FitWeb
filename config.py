from dataclasses import dataclass
import os
import dotenv

dotenv.load_dotenv()


@dataclass
class DBConfig:
    HOST: str = os.getenv("DB_HOST")
    PORT: int = os.getenv("DB_PORT")
    USER: str = os.getenv("POSTGRES_USER")
    PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    NAME: str = os.getenv("POSTGRES_DB")
