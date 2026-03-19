import logging
import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from auth_gateway.config import settings
from auth_gateway.routers import user, auth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return JSONResponse({"error": str(exc)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=settings.RELOAD)