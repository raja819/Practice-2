from dotenv import load_dotenv
import os
# Load variables from the .env file
load_dotenv()
# Access variables
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')
print(f'SECRET_KEY: {SECRET_KEY}')
print(f'DATABASE_URL: {DATABASE_URL}')