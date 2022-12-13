def procurarVendedor (meuBanquinho ) :
    minhaColuna = meuBanquinho.vendedor
    minhaBusca = {'nome': 'Natalia'}
    x = minhaColuna.find(minhaBusca)

    for a in x :
        print(a)

def procurarTodesVendedor (meuBanquinho):
    minhaColuna = meuBanquinho.vendedor

    for x in minhaColuna.find ():
        print(x)