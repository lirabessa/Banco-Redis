import Usuario.buscarUsuario as buscarUsuario
from bson.json_util import dumps
from bson.objectid import ObjectId
import json

def inserirRedis(banquinhoRedis, meuBanquinho):
    nome = buscarUsuario.procurarUsuario(meuBanquinho)
    listaObjeto = json.dumps(nome.get('favoritos'))
    banquinhoRedis.set('usuario: ' + nome['nome'], listaObjeto)
    x = banquinhoRedis.get('usuario: ' + nome['nome'])
    print(x)

def adicionarFav(banquinhoRedis, meuBanquinho):
    minhaColuna = meuBanquinho.produtos
    prod =  minhaColuna.find_one(ObjectId('6334323724e8529553ab4eea'))
    nome = buscarUsuario.procurarUsuario(meuBanquinho)
    novoFavorito = banquinhoRedis.get('usuario: ' + nome['nome'])
    favoritosDecode = json.loads(novoFavorito.decode())
    favoritosFormatado = {'_id': prod.get('_id'), 'nome': prod.get('nome')}
    listaNovosFavoritos = [favoritosFormatado, * favoritosDecode]
    banquinhoRedis.set('usuario: ' + nome['nome'], dumps(listaNovosFavoritos))
    x = banquinhoRedis.get('usuario: ' + nome['nome'])
    print(x)