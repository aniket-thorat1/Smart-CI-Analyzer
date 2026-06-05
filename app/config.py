import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME", "SmartCIAnalyser")
    PORT = int(os.getenv("PORT", 5000))