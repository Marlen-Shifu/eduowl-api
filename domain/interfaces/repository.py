from abc import ABC, abstractmethod

from domain.models.course import Course
from domain.models.user import User
from domain.models.video import CourseVideo


class CourseRepositoryInterface(ABC):
    @abstractmethod
    def create_course(self, course_name: str, description: str, author_id: int) -> Course:
        pass

    @abstractmethod
    def get_course(self, course_id: int) -> Course:
        pass

    @abstractmethod
    def list_courses(self) -> list[Course]:
        pass

    @abstractmethod
    def update_course(self, course_id: int, course_name: str, description: str) -> Course:
        pass

    @abstractmethod
    def delete_course(self, course_id: int) -> None:
        pass


class VideoRepositoryInterface(ABC):
    @abstractmethod
    def create_video(self, course_id: int, video_url: str, title: str) -> CourseVideo:
        pass

    @abstractmethod
    def get_video(self, video_id: int) -> CourseVideo:
        pass

    @abstractmethod
    def list_videos_for_course(self, course_id: int) -> list[CourseVideo]:
        pass

    @abstractmethod
    def update_video(self, video_id: int, video_url: str, title: str) -> CourseVideo:
        pass

    @abstractmethod
    def delete_video(self, video_id: int) -> None:
        pass


class UserRepositoryInterface(ABC):
    @abstractmethod
    def create_user(self, username: str, email: str, hashed_password: str) -> User:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        pass
