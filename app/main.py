from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Learning FastAPI | Integration with Databases")

# Endpoint
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI with Database Integration!"}