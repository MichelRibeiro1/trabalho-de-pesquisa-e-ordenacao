from db.models import ConsultaModel
from datetime import datetime

class Consulta:
    def __init__(self, paciente, exame):
        self.paciente = paciente
        self.exame = exame
        self.data = datetime.now().isoformat()

    def criar(self, sessao):
        consulta = ConsultaModel(
            paciente=self.paciente,
            exame=self.exame,
            data=self.data,
        )
        sessao.add(consulta)
        sessao.commit()

    @staticmethod
    def get_consultas(sessao, order_by='id'):
        query = sessao.query(ConsultaModel).order_by(order_by).all()
        return query
