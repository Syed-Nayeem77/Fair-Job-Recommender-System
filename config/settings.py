"""
Central configuration for the Fair Job Recommender System
"""

from pathlib import Path
import os
from datetime import datetime

class Config:
    # Model Configuration
    MODEL_VERSION = "1.0.0"
    MODEL_NAME = "two_tower_recommender"
    
    # Path Configuration
    BASE_DIR = Path(__file__).parent.parent
    MODEL_DIR = BASE_DIR / "models"
    DATA_DIR = BASE_DIR / "data"
    
    # File Paths
    MODEL_PATH = MODEL_DIR / f"{MODEL_NAME}_v{MODEL_VERSION.replace('.', '_')}.pkl"
    CANDIDATES_DATA = DATA_DIR / "candidates.csv"
    JOBS_DATA = DATA_DIR / "jobs.csv"
    
    # API Configuration
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", 8000))
    
    # Monitoring
    MONITORING_INTERVAL_HOURS = 24
    DRIFT_THRESHOLD = 0.15
    
    # Logging
    LOG_DIR = BASE_DIR / "logs"
    LOG_FILE = LOG_DIR / f"{datetime.now().strftime('%Y%m%d')}.log"

# Initialize configuration
settings = Config()

# Ensure directories exist
settings.MODEL_DIR.mkdir(exist_ok=True)
settings.LOG_DIR.mkdir(exist_ok=True)
