from db.client import user_collection
from services.auth.util.hashing import hash_password, verify_password
from models.users import UserCreate, UserUpdatePassword, UserLogin
from bson import ObjectId
from fastapi import HTTPException, status
import asyncio


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
    }

#get user
async def find_user_by_username(username):
    return user_collection.find_one({"username": username})

async def find_user_by_email(email):
    return user_collection.find_one({"email": email})

#only works with local login
#post new user
async def user_registration(user: UserCreate):

    hashed_password = hash_password(user.hashed_password)
    user.hashed_password = hashed_password

    result = user_collection.insert_one(user.model_dump())

    return user_helper(user_collection.find_one({"_id": result.inserted_id}))


#update user password
async def user_update_password(user_id:str, password:str):
        
    hashed_password = hash_password(password)
    user_collection.update_one(
        {"_id": user_id},
        {"$set": {"hashed_password": hashed_password}}
        )

    return {"message": "Password Updated", "success": True}


#delete user
async def user_delete(user_id: str):

    result = user_collection.delete_one({"_id": user_id})
    
    return {"success": result.deleted_count > 0}

