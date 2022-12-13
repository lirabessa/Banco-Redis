from bson.objectid import ObjectId
import Compra.buscarCompra as buscar

def deletarCompra (meuBanquinho):
    minhaColuna = meuBanquinho.Compra
    buscar.procurarTodesCompra(meuBanquinho)

    id = input(str('Qual o ID da Compra que você quer deletar? '))
    minhaColuna.delete_one({'_id':ObjectId(id)})
    print('Compra deletada')

