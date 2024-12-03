from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from services.course_service import CourseService
from db.repository import CourseRepository
from domain.models.course import CourseCreate
from core.security import get_current_user

router = APIRouter()

# Dependency to provide the CourseService
def get_course_service(db: Session = Depends(get_db)):
    course_repository = CourseRepository(db)
    return CourseService(course_repository)

@router.post("/courses")
def create_course(course: CourseCreate, user=Depends(get_current_user), course_service: CourseService = Depends(get_course_service)):
    return course_service.create_course(course, user.id)

@router.get("/courses")
def list_courses(course_service: CourseService = Depends(get_course_service)):
    return course_service.list_courses()

@router.get("/courses/{course_id}")
def get_course(course_id: int, course_service: CourseService = Depends(get_course_service)):
    return course_service.get_course(course_id)

@router.put("/courses/{course_id}")
def update_course(course_id: int, course_data: CourseCreate, user=Depends(get_current_user), course_service: CourseService = Depends(get_course_service)):
    return course_service.update_course(course_id, course_data)

@router.delete("/courses/{course_id}")
def delete_course(course_id: int, user=Depends(get_current_user), course_service: CourseService = Depends(get_course_service)):
    return course_service.delete_course(course_id)
