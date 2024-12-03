from typing import Optional, Type

from fastapi import HTTPException
from sqlalchemy.orm import Session

from domain.interfaces.repository import CourseRepositoryInterface
from domain.interfaces.repository import UserRepositoryInterface
from domain.interfaces.repository import VideoRepositoryInterface
from domain.models.course import Course
from domain.models.user import User
from domain.models.video import CourseVideo


class UserRepository(UserRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, email: str, hashed_password: str) -> User:
        new_user = User(username=username, email=email, hashed_password=hashed_password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user_by_email(self, email: str) -> Optional[Type[User]]:
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_username(self, username: str) -> Optional[Type[User]]:
        return self.db.query(User).filter(User.username == username).first()


class CourseRepository(CourseRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def create_course(self, course_name: str, description: str, author_id: int) -> Course:
        new_course = Course(course_name=course_name, description=description, author_id=author_id)
        self.db.add(new_course)
        self.db.commit()
        self.db.refresh(new_course)
        return new_course

    def get_course(self, course_id: int) -> Course:
        course = self.db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course

    def list_courses(self) -> list[Course]:
        return self.db.query(Course).all()

    def update_course(self, course_id: int, course_name: str, description: str) -> Course:
        course = self.get_course(course_id)
        course.course_name = course_name
        course.description = description
        self.db.commit()
        self.db.refresh(course)
        return course

    def delete_course(self, course_id: int) -> None:
        course = self.get_course(course_id)
        self.db.delete(course)
        self.db.commit()


class VideoRepository(VideoRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def create_video(self, course_id: int, video_url: str, title: str) -> CourseVideo:
        new_video = CourseVideo(course_id=course_id, video_url=video_url, title=title)
        self.db.add(new_video)
        self.db.commit()
        self.db.refresh(new_video)
        return new_video

    def get_video(self, video_id: int) -> CourseVideo:
        video = self.db.query(CourseVideo).filter(CourseVideo.id == video_id).first()
        if not video:
            raise HTTPException(status_code=404, detail="Video not found")
        return video

    def list_videos_for_course(self, course_id: int) -> list[CourseVideo]:
        return self.db.query(CourseVideo).filter(CourseVideo.course_id == course_id).all()

    def update_video(self, video_id: int, video_url: str, title: str) -> CourseVideo:
        video = self.get_video(video_id)
        video.video_url = video_url
        video.title = title
        self.db.commit()
        self.db.refresh(video)
        return video

    def delete_video(self, video_id: int) -> None:
        video = self.get_video(video_id)
        self.db.delete(video)
        self.db.commit()
