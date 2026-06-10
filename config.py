from dataclasses import dataclass
import os
import dotenv

dotenv.load_dotenv()


# SQL databse config
@dataclass
class DBConfig:
    HOST: str = os.getenv("DB_HOST")
    PORT: int = os.getenv("DB_PORT")
    USER: str = os.getenv("POSTGRES_USER")
    PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    NAME: str = os.getenv("POSTGRES_DB")


# Redis database config
@dataclass
class RedisConfig:
    PORT: int = os.getenv("REDIS_PORT")
    HOST: str = os.getenv("REDIS_HOST")