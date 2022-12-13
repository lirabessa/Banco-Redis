from bson.objectid import ObjectId
import Usuario.buscarUsuario as buscarUsuario

def atualizarFavorito (meuBanquinho, favoritos):
    minhaColuna = meuBanquinho.Usuario
    usuario = buscarUsuario.procurarUsuario(meuBanquinho)
    minhaColuna.update_one({"_id": usuario.get("_id")}, {"$set":{"favoritos": favoritos}})

def atualizarUsuario (meuBanquinho) :
    minhaColuna = meuBanquinho.Usuario
    buscarUsuario.procurarTodesUsuario(meuBanquinho)

    id = input(str('Qual o ID você quer atualizar? '))
    nome = input (str('Qual nome do Usuario? '))
    rua = input(str('Qual rua do Usuario? '))
    numero = input(str ('Qual numero da casa do Usuario? '))
    cep = input(str ('Qual cep do Usuario? '))
    cidade = input(str ('Qual cidade do Usuario? '))
    estado = input(str ('Qual estado do Usuario? '))
    cel = input(str ('Qual telefone celular do Usuario? '))
    residencial = input(str ('Qual telefone residencialdo Usuario? '))
    meuDicionario = { "$set":  {"nome": nome,
        "endereco": {
        "Rua": rua,
        "numero":numero,
        "cep":cep,
        "cidade":cidade,
        "estado":estado       
    },
        "tel": {
        "celular": cel,
        "residencial": residencial
    },
    "favoritos":[]

    }}
    minhaColuna.update_one({'_id':ObjectId(id)}, meuDicionario)

    for x in minhaColuna.find():
        print(x)
