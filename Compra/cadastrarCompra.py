def cadastrarCompra (meuBanquinho):
    minhaColuna = meuBanquinho.Compra
    nomeProduto = input (str('Qual nome do Produto? '))
    valorProduto = input (str('Qual valor do Produto? '))
    nomeVendedor = input (str('Qual nome do Vendedor '))
    emailVendedor = input (str('Qual email do Vendedor? '))
    nomeUsuario = input (str('Qual nome do Usuario? '))
    emailUsuario = input (str('Qual email do Usuario? '))
    meuDicionario = { "produtos": {
        "nome": nomeProduto,
        "preco": valorProduto
    },
    "vendedor": {
        "nome": nomeVendedor,
        "email": emailVendedor
    },
    "usuario": {
        "nome": nomeUsuario,
        "email": emailUsuario
    },}

    x =  minhaColuna.insert_one(meuDicionario)

    print(x.inserted_id)