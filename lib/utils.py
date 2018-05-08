from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import settings

def criar_sessao():
    engine = create_engine(settings.SQL_ALCHEMY_URI, echo=True)
    session = sessionmaker(bind=engine)
    sessao = session()
    return sessao
