#THIS IS A TEST TO MAKE SURE THAT THE ENV VARS CONTAIN THE RIGHT DATA

import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("HOST"))
print(os.getenv("PORT"))
print(os.getenv("USER_SQL"))
print(os.getenv("PASSWORD"))
print(os.getenv("DATABASE"))
