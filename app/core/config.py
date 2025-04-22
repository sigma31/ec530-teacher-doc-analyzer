from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    database_url: str = "sqlite:///./graded_results.db"  # Default

    class Config:
        env_file = ".env"  # Automatically load the class key from .env file


settings = Settings()