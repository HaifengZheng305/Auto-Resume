from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.authRoutes import auth_router

app = FastAPI()


app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])