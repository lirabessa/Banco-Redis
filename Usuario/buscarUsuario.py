def procurarUsuario (meuBanquinho ) :
    minhaColuna = meuBanquinho.Usuario
    minhaBusca = {'nome': 'jj'}
    x = minhaColuna.find(minhaBusca)

    for a in x :
        return(a)
        

def procurarTodesUsuario (meuBanquinho):
    minhaColuna = meuBanquinho.Usuario

    for x in minhaColuna.find ():
        return(x)