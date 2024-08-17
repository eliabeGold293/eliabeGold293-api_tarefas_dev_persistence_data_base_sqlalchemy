from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(name = nome).first()

        try:
            response = {
                'nome': pessoa.name,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }

        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(name = nome).first()
        dados = request.json

        if 'nome' in dados:
            pessoa.name = dados['nome']
        elif 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()

        response = {
            'mensagem': 'Nome mudado com sucesso! confira os dados:',
            'id': pessoa.id,
            'nome': pessoa.name,
            'idade': pessoa.idade
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(name = nome).first()
        pessoa.deletar()
        mensagem = "Pessoa {} excluida com sucesso".format(pessoa.name)
        response = {
            "status": "sucesso", 'mensagem': mensagem
        }
        return response

class ListarPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': p.id, 'nome': p.name, 'idade': p.idade} for p in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(name = dados['nome'], idade = dados['idade'])
        pessoa.save()

        response = {
            'mensagem': 'Você foi inserido com sucesso',
            'id': pessoa.id,
            'nome': pessoa.name,
            'idade': pessoa.idade
        }

        return response

class ListarAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id_atividade': at.id, 'nome': at.name, 'id_pessoa_responsavel': at.pessoa_id} for at in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(name = dados['pessoa']).first()
        atividade = Atividades(name = dados['nome'], pessoa = pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.name,
            'nome': atividade.name,
            'id_atividade': atividade.id
        }
        return response

# rotas:
api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListarPessoas, '/pessoas/')
api.add_resource(ListarAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)