from bson.objectid import ObjectId
import Produto.buscarProduto as buscarProduto

def atualizarProduto (meuBanquinho) :
    minhaColuna = meuBanquinho.produtos
    
    buscarProduto.procurarTodes(meuBanquinho)
    id = input(str('Qual o ID do produto você quer atualizar? '))
    nome = input (str('Qual nome do produto? '))
    qtde =input(str ('Qual quantidade do produto? '))

    meuDicionario = { "$set":  {
       "nomeProdutos": [
        {
        "nome": nome,
        "qtde": qtde          
    },]}}

    minhaColuna.update_one({'_id':ObjectId(id)}, meuDicionario)

    for x in minhaColuna.find():
        print(x)
