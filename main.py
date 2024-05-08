from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
import models
from models import Vehiculo
from db import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/vehiculos/", status_code=status.HTTP_200_OK)
def listar_vehiculos(db: Session = Depends(get_db)):
    return db.query(Vehiculo).all()

