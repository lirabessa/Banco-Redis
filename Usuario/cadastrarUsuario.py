def cadastrarUsuario (meuBanquinho):

    minhaColuna = meuBanquinho.Usuario
    nome = input (str('Qual seu nome? '))
    rua = input(str('Qual sua rua? '))
    numero = input(str ('Qual seu numero? '))
    cep = input(str ('Qual seu cep? '))
    cidade = input(str ('Qual sua cidade? '))
    estado =input(str ('Qual seu estado? '))
    meuDicionario = {"nome": nome,
        "endereco": {
        "Rua": rua,
        "numero":numero,
        "cep":cep,
        "cidade":cidade,
        "estado":estado       
        },
        "favoritos": [
        
        ]
    }

    x =  minhaColuna.insert_one(meuDicionario)

    print(x.inserted_id)
