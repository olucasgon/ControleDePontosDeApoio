from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.entities.Base import Base

class Responsavel(Base):
    __tablename__ = "Responsavel"

    id = Column("id", Integer, primary_key=True)
    codigo = Column("codigo", String(25), nullable=False ,unique=True)
    pessoa_id = Column("pessoa_id", Integer, ForeignKey("Pessoa.id"), nullable=False)
    pontoapoio_id = Column("pontoapoio_id",Integer, ForeignKey("PontoApoio.id"), nullable=False)

    Pessoa = relationship("Pessoa", backref="Responsavel")
    PontoApoio = relationship("PontoApoio", back_populates="Responsavel")
    