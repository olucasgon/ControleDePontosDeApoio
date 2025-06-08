from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.entities.Base import Base

class Pessoa(Base):
    __tablename__ = "Pessoa"

    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String(100), nullable=False)
    cpf = Column("cpf", String(14), nullable=False, unique=True)
    telefone = Column("telefone", String(15), nullable=True)
    pontoapoio_id = Column("pontoapoio_id", Integer, ForeignKey("PontoApoio.id"))

    PontoApoio = relationship("PontoApoio", back_populates="Pessoa")
    RegistroEntrada = relationship("RegistroEntrada", back_populates="Pessoa")
