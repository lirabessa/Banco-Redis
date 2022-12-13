def cadastrarProduto (meuBanquinho):
    minhaColuna = meuBanquinho.produtos
    nomeProduto = input(str('Qual nome do Produto? '))
    preco = input(str('Qual preço do Produto? '))
    qtde = input(str('Qual qtde do Produto? '))
    nomeVendedor = input(str('Qual nome do Vendedor do Produto? '))
    emailVendedor = input(str('Qual email do Vendedor do Produto? '))
    meuDicionario = {"nomeProduto": nomeProduto,
        "preco": preco,
        "qtde": qtde,
        "vendedor": {
        "nomeVendedor": nomeVendedor,
        "emailVendedor": emailVendedor
    },}

    x =  minhaColuna.insert_one(meuDicionario)

    print(x.inserted_id)