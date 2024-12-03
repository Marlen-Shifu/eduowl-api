from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from services.video_service import VideoService
from db.repository import VideoRepository
from domain.models.video import CourseVideoCreate
from core.security import get_current_user

router = APIRouter()

# Dependency to provide the VideoService
def get_video_service(db: Session = Depends(get_db)):
    video_repository = VideoRepository(db)
    return VideoService(video_repository)

@router.post("/courses/{course_id}/videos")
def create_video(course_id: int, video_data: CourseVideoCreate, user=Depends(get_current_user), video_service: VideoService = Depends(get_video_service)):
    return video_service.create_video(course_id, video_data)

@router.get("/courses/{course_id}/videos")
def list_videos_for_course(course_id: int, video_service: VideoService = Depends(get_video_service)):
    return video_service.list_videos_for_course(course_id)

@router.get("/courses/{course_id}/videos/{video_id}")
def get_video(course_id: int, video_id: int, video_service: VideoService = Depends(get_video_service)):
    return video_service.get_video(video_id)

@router.put("/courses/{course_id}/videos/{video_id}")
def update_video(course_id: int, video_id: int, video_data: CourseVideoCreate, user=Depends(get_current_user), video_service: VideoService = Depends(get_video_service)):
    return video_service.update_video(video_id, video_data)

@router.delete("/courses/{course_id}/videos/{video_id}")
def delete_video(course_id: int, video_id: int, user=Depends(get_current_user), video_service: VideoService = Depends(get_video_service)):
    return video_service.delete_video(video_id)
