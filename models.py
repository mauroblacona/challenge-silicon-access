from sqlalchemy import Column, String, Date
from db import Base

class Vehiculo(Base):
    __tablename__ = "vehiculos"
    id = Column(String, primary_key=True, index=True)
    tipo = Column(String, index=True)
    marca = Column(String)
    modelo = Column(String)
    color = Column(String)
    patente = Column(String, unique=True, index=True)
    aseguradora = Column(String)
    vencimiento_poliza = Column(Date)

