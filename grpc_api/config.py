import os
from dotenv import load_dotenv

try:
    load_dotenv()
except:
    pass

HOST = os.getenv(key="HOST", default='[::]')
PORT = os.getenv(key="PORT", default='50051')