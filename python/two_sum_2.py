def two_sum_2(arr, target):
    dic = {}

    for i in range(len(arr)):
        num = target - arr[i]

        if  num in dic:
            return [dic[num], i + 1]

        dic[arr[i]] = i + 1

arr = [2, 7, 11, 15]
target = 9
resultado = two_sum_2(arr, target)
print(f"Índices: {resultado}")