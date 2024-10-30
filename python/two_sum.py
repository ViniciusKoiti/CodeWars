def two_sum(arr, target):
    dict = {}

    for i in range(len(arr)):
        num = target - arr[i]

        if num in dict:
            return [dict[num], i + 1]

        dict[arr[i]] = i + 1

    raise ValueError("Nenhuma solução encontrada")

arr = [2, 7, 11, 15]
target = 9
resultado = two_sum(arr, target)
print(f"Índices: {resultado}")