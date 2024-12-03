from fastapi import FastAPI
from api import auth, course, video
from db.session import engine
from db.base import Base

# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the routers
app.include_router(auth.router, prefix="/api/auth")
app.include_router(course.router, prefix="/api")
app.include_router(video.router, prefix="/api")
