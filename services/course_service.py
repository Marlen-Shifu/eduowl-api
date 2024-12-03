from domain.interfaces.repository import CourseRepositoryInterface
from domain.models.course import CourseCreate

class CourseService:
    def __init__(self, course_repository: CourseRepositoryInterface):
        self.course_repository = course_repository

    def create_course(self, course: CourseCreate, user_id: int):
        return self.course_repository.create_course(course.course_name, course.description, user_id)

    def list_courses(self):
        return self.course_repository.list_courses()

    def get_course(self, course_id: int):
        return self.course_repository.get_course(course_id)

    def update_course(self, course_id: int, course_data: CourseCreate):
        return self.course_repository.update_course(course_id, course_data.course_name, course_data.description)

    def delete_course(self, course_id: int):
        return self.course_repository.delete_course(course_id)
