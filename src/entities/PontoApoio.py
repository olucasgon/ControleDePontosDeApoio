from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from src.entities.Base import Base

class PontoApoio(Base):
    __tablename__ = "PontoApoio"

    id = Column("id",Integer, primary_key=True)
    nome = Column("nome",String(100), nullable=False, unique=True)
    latitude = Column("latitude",DECIMAL(9, 6), nullable=False)
    longitude = Column("longitude",DECIMAL(9, 6), nullable=False)
    capacidade = Column("capacidade",Integer, nullable=False)

    Pessoa = relationship("Pessoa", back_populates="PontoApoio")
    Recurso = relationship("Recurso", back_populates="PontoApoio")
    Responsavel = relationship("Responsavel", back_populates="PontoApoio")
    RegistroEntrada = relationship("RegistroEntrada", back_populates="PontoApoio")