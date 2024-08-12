# folha para realizar as consultas
from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(name= 'Eliabe', idade = 21)
    #print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(name = 'Eliabe').first()
    print(pessoa)

    #Este laço for ajuda a encontrar as pessoas existentes no banco
    #for p in pessoa:
     #   print(p)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(name='Eliabe').first()
    pessoa.idade = 22
    pessoa.name = 'João'
    pessoa.save()

def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(name='Eliabe').first()
    pessoa.deletar()

if __name__=='__main__':
    insere_pessoas()
    #altera_pessoa()
    #excluir_pessoa()
    consulta_pessoas()
