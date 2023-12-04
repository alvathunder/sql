import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Print loaded variables for debugging
print(os.getenv("HOST"))
print(os.getenv("PORT"))
print(os.getenv("USER_SQL"))
print(os.getenv("PASSWORD"))
print(os.getenv("DATABASE"))