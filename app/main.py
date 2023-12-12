from fastapi import FastAPI
from typing import List
from fastapi.params import Body
from fastapi import status, HTTPException, Response, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, get_db
from .config import settings

from routers import post,user,auth,vote
# import auth



# pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind=engine)


app = FastAPI()



        
#####################
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
###################

##referred as "path operation" or sometimes referred as "route"
@app.get("/")
def root():
    return {"message":"Hello World"}




