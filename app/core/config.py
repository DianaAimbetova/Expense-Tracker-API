from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost/dbname"


settings = Settings()
