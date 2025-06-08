from db.client import user_collection
from services.auth.util.hashing import hash_password, verify_password
from models.users import UserCreate, UserResponse, UserUpdatePassword, UserLogin, UserDelete
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

#only works with local login
#post new user
async def user_registration(user: UserCreate):
    hashed_password = hash_password(user.hashed_password)
    user.hashed_password = hashed_password

    if(user_collection.find_one({"email": user.email})):
        return {'id': 'exist',
        'username': 'exist'}

    result = user_collection.insert_one(user.model_dump())
    return user_helper(user_collection.find_one({"_id": result.inserted_id}))

#get userlogin
async def user_login(user: UserLogin):
    userDB = await find_user_by_username(user.username)
    if not userDB:
        raise HTTPException(status_code=401, detail="User not found")
    stored_password = userDB["hashed_password"]
    if not verify_password(user.password, stored_password):
        raise HTTPException(status_code=401, detail="Invalid password")
        
    return {"message": "Login Successful", "success": True}

#update user password
async def user_update_password(user: UserUpdatePassword):
    
    userDB = await find_user_by_username(user.username)

    if not userDB:
        raise HTTPException(status_code=401, detail="User not found")
        
    hashed_password = hash_password(user.new_password)
    user_collection.update_one(
        {"_id": userDB["_id"]},
        {"$set": {"hashed_password": hashed_password}}
        )

    return {"message": "Password Updated", "success": True}


#delete user
async def user_delete(user: UserDelete):
    userDB = await find_user_by_username(user.username)

    if not userDB:
        raise HTTPException(status_code=401, detail="User not found")

    result = user_collection.delete_one({"_id": userDB["_id"]})
    return {"message": "User deleted successfully", "success": result.deleted_count > 0}

async def main():
    user = UserDelete(
        username="Andy27",
        password="yobpoo111",
    )

    result = await user_delete(user)
    print(result)
    print("testing")
    

if __name__ == "__main__":
    asyncio.run(main())
    
