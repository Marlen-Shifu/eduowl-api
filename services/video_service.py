from domain.interfaces.repository import VideoRepositoryInterface
from domain.models.video import CourseVideoCreate

class VideoService:
    def __init__(self, video_repository: VideoRepositoryInterface):
        self.video_repository = video_repository

    def create_video(self, course_id: int, video_data: CourseVideoCreate):
        return self.video_repository.create_video(course_id, video_data.video_url, video_data.title)

    def list_videos_for_course(self, course_id: int):
        return self.video_repository.list_videos_for_course(course_id)

    def get_video(self, video_id: int):
        return self.video_repository.get_video(video_id)

    def update_video(self, video_id: int, video_data: CourseVideoCreate):
        return self.video_repository.update_video(video_id, video_data.video_url, video_data.title)

    def delete_video(self, video_id: int):
        return self.video_repository.delete_video(video_id)
