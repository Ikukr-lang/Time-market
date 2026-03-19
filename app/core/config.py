from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    bot_token: str
    webapp_url: str
    yookassa_shop_id: str
    yookassa_secret_key: str
    database_url: str
    secret_key: str = "change-me"

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

settings = Settings()
