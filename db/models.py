import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

BASE = declarative_base()

class ConsultaModel(BASE):
    ''' Definição do modelo para a tablea Consulta no BD '''
    __tablename__ = 'consulta'
    id = Column(Integer, primary_key=True)
    paciente = Column(String)
    exame = Column(String)
    data = Column(String)

    def __repr__(self):
        consulta = {
            "id": self.id,
            "paciente": self.paciente,
            "exame": self.exame,
            "data": self.data.isoformat(),
        }
        return json.dumps(consulta)

    def serialize(self):
        return {
            "id": self.id,
            "paciente": self.paciente,
            "exame": self.exame,
            "data": self.data.isoformat(),
        }
