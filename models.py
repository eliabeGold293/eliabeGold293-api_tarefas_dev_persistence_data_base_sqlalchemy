import sqlalchemy.orm
# models.py é onde vão estar as nossas classes que vão referenciar uma tabela do banco de dados.
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

# criando um sqlite. O nome do banco se chama atividades.db
# convert_unicode =True é usado para não haver problemas com acentuação.
engine = create_engine('sqlite:///atividades.db')

# cria a seção. para poder fazer as alterações e consultas.
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = sqlalchemy.orm.declarative_base()
Base.query = db_session.query_property()

# criando as tabelas

# Tabela Pessoa
class Pessoas(Base):
    __tablename__='pessoas' # nome da minha tabela

    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa: {}, Idade: {}>'.format(self.name, self.idade)

    # função para salvar as informações
    def save(self):
        # add(self) vai adicionar o prórpio objeto
        db_session.add(self)
        db_session.commit()

    def deletar(self):
        db_session.delete(self)
        db_session.commit()

# Tabela Atividades
class Atividades(Base):
    __tablename__='atividades' # nome da minha tabela

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id')) # cria a chave estrangeira
    pessoa = relationship("Pessoas") # relaciona the Class Atividades with Class Pessoas

    def save(self):
        # add(self) vai adicionar o próprio objeto
        db_session.add(self)
        db_session.commit()

# função que vai criar meu banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()