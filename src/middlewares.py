from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware


middlewares = [Middleware(CORSMiddleware, allow_origins=["*"])]
