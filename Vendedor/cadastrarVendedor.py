def cadastrarVendedor (meuBanquinho):
    minhaColuna = meuBanquinho.vendedor
    nome = input (str('Qual nome Vendedor? '))
    rua = input(str('Qual rua Vendedor? '))
    bairro = input(str ('Qual cep Vendedor? '))
    numero = input(str ('Qual cidade Vendedor? '))
    estado = input(str ('Qual estado Vendedor? '))
    cnpj = input(str ('Qual cnpj Vendedor? '))
    nomeProduto = input(str ('Qual nome do Produto que o Vendedor vende? '))
    valorProduto = input(str ('Qual valor do Produto? '))
    meuDicionario = { "nome": nome,
        "end": {
        "rua": rua,
        "bairro": bairro,
        "numero": numero,
        "estado": estado,         
    },
        "cnpj": cnpj,
        "produtos": {
        "nome": nomeProduto,
        "valor": valorProduto
    },}

    x =  minhaColuna.insert_one(meuDicionario)

    print(x.inserted_id)