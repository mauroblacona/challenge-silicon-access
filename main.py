from fastapi import FastAPI, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
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

@app.get("/vehiculos", status_code=status.HTTP_200_OK)
def listar_vehiculos(db: Session = Depends(get_db)):
    return db.query(Vehiculo).all()

@app.post('/vehiculos', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreateVehiculo])
def crear_vehiculo(vehiculo:schemas.CreateVehiculo, db:Session = Depends(get_db)):
    
    # Verificamos si ya existe un vehiculo con la patente a crear
    if db.query(models.Vehiculo).filter(models.Vehiculo.patente == vehiculo.patente).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe un vehiculo con esta patente.")
    
    nuevo_vehiculo = models.Vehiculo(**vehiculo.dict())
    db.add(nuevo_vehiculo)
    db.commit()
    db.refresh(nuevo_vehiculo)

    return [nuevo_vehiculo]

@app.get('/vehiculos/{id}', response_model=schemas.CreateVehiculo, status_code=status.HTTP_200_OK)
def detalle_vehiculo(id:int ,db:Session = Depends(get_db)):

    id_vehiculo = db.query(models.Vehiculo).filter(models.Vehiculo.id == id).first()

    if id_vehiculo is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El vehiculo con id: {id} no existe en nuestra base de datos.")
    return id_vehiculo

@app.delete('/vehiculos/{id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar_vehiculo(id:int, db:Session = Depends(get_db)):

    vehiculo_eliminado = db.query(models.Vehiculo).filter(models.Vehiculo.id == id)

    if vehiculo_eliminado.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"El vehiculo con id: {id} no existe en nuestra base de datos.")
    vehiculo_eliminado.delete(synchronize_session=False)
    db.commit()
    
    return vehiculo_eliminado.first(), {"message": "Vehículo eliminado exitosamente"}
    
@app.put('/vehiculos/{id}', response_model=schemas.CreateVehiculo)
def actualizar_vehiculo(id: int, actualizar_vehiculo: schemas.VehiculoUpdate, db: Session = Depends(get_db)):

    vehiculo_actualizado = db.query(models.Vehiculo).filter(models.Vehiculo.id == id).first()

    if not vehiculo_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El vehiculo con id: {id} no existe en nuestra base de datos.")

    # Solo los campos actualizables
    for key, value in actualizar_vehiculo.dict().items():
        if value is not None:
            setattr(vehiculo_actualizado, key, value)

    db.commit()
    db.refresh(vehiculo_actualizado)

    return vehiculo_actualizado, {"message": "Vehículo modificado exitosamente"}