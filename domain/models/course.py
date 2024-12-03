from sqlalchemy import Column, Integer, String, ForeignKey
from db.base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, index=True)
    description = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))

# Pydantic models
from pydantic import BaseModel

class CourseCreate(BaseModel):
    course_name: str
    description: str

class CourseOut(BaseModel):
    id: int
    course_name: str
    description: str

    class Config:
        orm_mode = True
