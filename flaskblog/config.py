from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.getenv('EMAIL_USER')
    MAIL_PASSWORD=os.getenv('EMAIL_PASS')