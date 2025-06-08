from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.entities.Base import Base

class RegistroEntrada(Base):
    __tablename__ = "RegistroEntrada"

    id = Column("id", Integer, primary_key=True)
    pessoa_id = Column("pessoa_id",Integer, ForeignKey('Pessoa.id'), nullable=False)
    pontoapoio_id = Column(Integer, ForeignKey('PontoApoio.id'), nullable=False)
    entrada = Column("entrada", DateTime)
    saida = Column("saida",DateTime)

    Pessoa = relationship("Pessoa", back_populates="RegistroEntrada")
    PontoApoio = relationship("PontoApoio", back_populates="RegistroEntrada")
