def procurarProduto(meuBanquinho):
    minhaColuna = meuBanquinho.produtos
    minhaBusca = {'nomeProduto': 'Gin'}
    x = minhaColuna.find_one(minhaBusca)

    return(x)

def procurarTodesProduto (meuBanquinho):
    minhaColuna = meuBanquinho.produtos

    for x in minhaColuna.find():
        print(x)