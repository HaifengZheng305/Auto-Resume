from db.client import user_collection
from services.auth.util.hashing import hash_password, verify_password
from models.users import UserCreate, UserLogin, UserOut, UserUpdatePassword
from bson import ObjectId
from fastapi import HTTPException, status, APIRouter
from services.auth.authController import *

import asyncio

auth_router = APIRouter()

@auth_router.post("/login")
async def login(user: UserLogin):
    userDB = await find_user_by_username(user.username)
    if not userDB:
        raise HTTPException(status_code=401, detail="User not found")
    stored_password = userDB["hashed_password"]
    if not verify_password(user.password, userDB["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid password")
        
    return {"message": "Login Successful", "success": True}

@auth_router.post("/register", response_model=UserOut)
async def registration(user: UserCreate):
    existing_user = await find_user_by_username(user.username)

    existing_email = await find_user_by_email(user.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Username Exist")
    if existing_email:
        raise HTTPException(status_code =400, detail="Email Exist")

    return await user_registration(user)

@auth_router.put("/updatePassword")
async def updatePassword(user: UserUpdatePassword):
    userDB = await find_user_by_username(user.username)

    if not verify_password(user.cur_password, userDB["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    return await user_update_password(userDB["_id"], user.new_password)

@auth_router.get("/users/{username}", response_model=UserOut)
async def get_user(username: str):
    user = await find_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_helper(user)


@auth_router.delete("/users/{username}")
async def delete(username: str):

    userDB = await find_user_by_username(username)

    #in a check in here in the future to make sure delte doesn't happen by acceident.

    if not userDB:
        raise HTTPException(status_code=401, detail="User not found")

    success = await user_delete(userDB["_id"])

    return success




