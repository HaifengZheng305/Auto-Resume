import user_collection from db.client
from util.hashing import hash_password, verify_password
from models.users import UserCreate, UserResponse, UserUpdate
from bson import ObjectId
from fastapi import HTTPException, status


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
    }

async def user_registation(user: UserCreate):
    
