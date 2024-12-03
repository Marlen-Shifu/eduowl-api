from sqlalchemy import Column, Integer, String, ForeignKey
from db.base import Base

class CourseVideo(Base):
    __tablename__ = "course_videos"

    id = Column(Integer, primary_key=True, index=True)
    video_url = Column(String)
    title = Column(String)
    course_id = Column(Integer, ForeignKey("courses.id"))

# Pydantic models
from pydantic import BaseModel

class CourseVideoCreate(BaseModel):
    video_url: str
    title: str

class CourseVideoOut(BaseModel):
    id: int
    video_url: str
    title: str
    course_id: int

    class Config:
        orm_mode = True
