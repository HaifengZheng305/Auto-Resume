from typing import Optional, List
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)

class Education(BaseModel):
    school: str
    degree: str
    major: str
    minor: Optional[str]
    start_date: datetime
    end_date: datetime
    gpa: Optional[float]
    location: Optional[str]

class Experience(BaseModel):
    company: str
    position: str
    start_date: datetime
    end_date: datetime
    location: Optional[str]
    Achievement: Optional[str]

class Extracurricular(BaseModel):
    title: str
    date: datetime
    description: str

class Skill(BaseModel):
    name: str
    level: Optional[str]

class PersonalInfo(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str]
    location: Optional[str]
    linkedin: Optional[str]
    github: Optional[str]
    portfolio: Optional[str]
    summary: Optional[str]
    profile_picture: Optional[str]

class AccessResume(BaseModel):
    id: PyObjectId = Field(alias="_id")
    user_id: PyObjectId = Field(alias="user_id")
    personal_info: Optional[PersonalInfo]
    education: Optional[List[Education]]
    experience: Optional[List[Experience]]
    Extracurricular: Optional[List[Extracurricular]]
    skills: Optional[List[Skill]]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


    
