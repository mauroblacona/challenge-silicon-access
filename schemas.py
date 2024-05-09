from pydantic import BaseModel
from datetime import date

class VehiculoBase(BaseModel):
    tipo: str
    marca: str
    modelo: str
    color: str
    patente: str
    aseguradora: str
    vencimiento_poliza: date

    class Config:
        orm_mode = True

class CreateVehiculo(VehiculoBase):
    class Config:
        orm_mode = True

class VehiculoUpdate(BaseModel):
    color: str
    aseguradora: str
    vencimiento_poliza: date