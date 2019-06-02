def calcula_maior_produto(matriz):
    maior_produto = 0
    maior_diag = 1
    for i in range(0, 5):
        produto = 1
        for j in range(0, 5):
            produto *= matriz[i][j]
            if i == j:
                maior_diag *= matriz[i][j]
        if produto > maior_produto:
            maior_produto = produto

        if maior_produto < maior_diag:
            maior_produto = maior_diag

    return maior_produto
