from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.entities.Base import Base

class Recurso(Base):
    __tablename__ = "Recurso"

    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String(50), nullable=False)
    quantidade = Column("quantidade", Integer, nullable=False)
    pontoapoio_id = Column("pontoapoio_id",Integer, ForeignKey("PontoApoio.id"), nullable=False)

    PontoApoio = relationship("PontoApoio", back_populates="Recurso")
