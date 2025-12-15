"""
Configuration settings for the application
"""
import os

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Upload settings
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS = {'pdf'}
    
    # Database settings
    DATABASE_PATH = 'resume_analyzer.db'
    
    # API settings
    API_BASE_URL = os.environ.get('API_BASE_URL') or 'https://resume-analyse-backend.onrender.com/'
    
    # CORS settings
    CORS_ORIGINS = [
        "https://clever-cv.vercel.app",
        "http://localhost:3000/"
    ]

