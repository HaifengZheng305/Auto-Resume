from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

print("Starting MongoDB connection process...")

# Load environment variables
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    print("ERROR: MONGO_URI is not set in environment variables")
    exit(1)

# Check URI format

client = MongoClient(mongo_uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"Connection Error: {str(e)}")
    print("Error Type:", type(e).__name__)
except Exception as e:
    print(f"Connection Error: {str(e)}")
    print("Error Type:", type(e).__name__)

    
