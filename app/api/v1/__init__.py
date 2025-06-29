from fastapi import APIRouter
from app.domain.task.routes import router as task_router
from app.domain.user.routes import router as user_router

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(task_router, prefix="/tasks", tags=["Tasks"])
