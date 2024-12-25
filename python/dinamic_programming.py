
pesos = [1, 2, 3, 5]  
valores = [1, 6, 10, 16] 
capacidade = 7 
n = len(pesos)

dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacidade + 1):
        if pesos[i-1] <= w:
            dp[i][w] = max(dp[i-1][w], valores[i-1] + dp[i-1][w - pesos[i-1]])
            incluir = valores[i-1] + dp[i-1][w - pesos[i-1]]
            nao_incluir = dp[i-1][w]
            dp[i][w] = max(nao_incluir, incluir)
            
            print(f"Analisando o item {i} com peso {pesos[i-1]} e valor {valores[i-1]}:")
            print(f"  Capacidade atual: {w}")
            print(f"  Incluindo o item: valor = {incluir}")
            print(f"  Não incluindo o item: valor = {nao_incluir}")
            print(f"  Valor escolhido para dp[{i}][{w}] = {dp[i][w]}\n")
        else:
            # Se o item não pode ser incluído, mantemos o valor anterior
            dp[i][w] = dp[i-1][w]
            print(f"Item {i} com peso {pesos[i-1]} não cabe na capacidade {w}.")
            print(f"  Valor mantido para dp[{i}][{w}] = {dp[i][w]}\n")

print(f"Valor máximo que pode ser carregado: {dp[n][capacidade]}")

for row in dp:
    print(row)
