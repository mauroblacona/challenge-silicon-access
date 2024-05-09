from db import Base
from sqlalchemy import Column, Integer, String, Date

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    tipo = Column(String,nullable=False)
    marca = Column(String,nullable=False)
    modelo = Column(String,nullable=False)
    color = Column(String,nullable=False)
    patente = Column(String,nullable=False, unique=True)
    aseguradora = Column(String,nullable=False)
    vencimiento_poliza = Column(Date, nullable=False)
