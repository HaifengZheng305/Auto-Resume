from typing import Optional, List
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


# Custom class for Pydantic to handle MongoDB's ObjectId
class PyObjectId(ObjectId):
    @classmethod #method that be belong to class not instance
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)

#this is the base MongoDB User model
#pydantic for data validation and setting
class User(BaseModel):
    id: PyObjectId = Field(alias="_id")
    email: EmailStr
    username: str
    hashed_password: Optional[str] # Required for local login
    provider: Optional[str] = "local"
    oauth_id: Optional[str] # ID from OAuth provider
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    roles: Optional[List[str]] = Field(default_factory=lambda: ["user"])
    
    model_config = {
        "json_encoders": {ObjectId: str},
        "arbitrary_types_allowed": True, #allow model to accept fields with types Pydantic doesn't know
        "json_schema_extra": {
            "example": {
                "email": "user@example.com",
                "username": "johndoe",
                "hashed_password": "hashed_password_here",
                "provider": "local",
                "oauth_id": None,
                "roles": ["user"]
            }
        }
    }

# For input validation during registration internally
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    hashed_password: Optional[str] # Required for local login
    provider: Optional[str] = "local"
    oauth_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    roles: Optional[List[str]] = Field(default_factory=lambda: ["user"])

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "user@example.com",
                "username": "johndoe",
                "hashed_password": "password123",
                "provider": "local",
                "oauth_id": None
            }
        }
    }

# For responses
class UserResponse(BaseModel):
    id: PyObjectId
    email: EmailStr
    username: str
    provider: str
    roles: List[str]
    
    model_config = {
        "from_attributes": True
    }

class UserUpdatePassword(BaseModel):
    username: str
    new_password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserDelete(BaseModel):
    username: str
    password: str