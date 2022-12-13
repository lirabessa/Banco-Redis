import Usuario.buscarUsuario as buscarUsuario
import Usuario.atualizarUsuarior as atualizar
from bson.json_util import dumps
from bson.objectid import ObjectId
import json

def inserirRedis(banquinhoRedis, meuBanquinho):
    nome = buscarUsuario.procurarUsuario(meuBanquinho)
    minhaColunaUsuario = meuBanquinho.Usuario
    minhaColuna = meuBanquinho.produtos
    nome = minhaColunaUsuario.find_one(ObjectId('6398a6bd2dc8a6726c6e8a34'))
    prod =  minhaColuna.find_one(ObjectId('6334323724e8529553ab4eea'))
    del prod['_id']
    prod = json.dumps(prod)

    banquinhoRedis.rpush('favorito:' + nome.get("nome"), prod)
    x = banquinhoRedis.lrange('favorito:'+ nome.get("nome") ,0 ,-1)
    print(x)

def adicionarFav(banquinhoRedis, meuBanquinho):
    nome = buscarUsuario.procurarUsuario(meuBanquinho)
    favoritos = banquinhoRedis.lrange('favorito:'+ nome.get("nome") ,0 ,-1)
    listaFavoritos = []
    for favorito in favoritos:
        favorito = json.loads(favorito.decode())

        listaFavoritos.append(favorito)

    atualizar.atualizarFavorito(meuBanquinho, listaFavoritos)
    banquinhoRedis.delete('favorito:'+ nome.get("nome"))
