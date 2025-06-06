from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    email: EmailStr
    password: Optional[str] = None  # Hashed password for regular login
    provider: Optional[str] = None  # Authentication provider (e.g., "google" or None for local)
    provider_id: Optional[str] = None  # OAuth provider ID
    name: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}