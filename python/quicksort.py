# -*- coding: utf-8 -*-
import random
import time

def quicksort(array, inicio=None, fim=None):
    if inicio is None:
        inicio = 0
    if fim is None:
        fim = len(array) - 1
        
    if inicio >= fim:
        return
    
    def particionar(inicio, fim):
        pivo = array[fim]
        i = inicio - 1
        
        for j in range(inicio, fim):
            if array[j] <= pivo:
                i += 1
                array[i], array[j] = array[j], array[i]
                
        array[i + 1], array[fim] = array[fim], array[i + 1]
        return i + 1
    
    pos_pivo = particionar(inicio, fim)
    quicksort(array, inicio, pos_pivo - 1)
    quicksort(array, pos_pivo + 1, fim)
    
def test_quicksort():
    array_pequeno = [64, 34, 25, 12, 22, 11, 90]
    print("Teste 1 - Array pequeno:")
    print("Original:", array_pequeno)
    quicksort(array_pequeno)
    print("Ordenado:", array_pequeno)
    print("Correto?", array_pequeno == sorted(array_pequeno.copy()))
    print()

    array_repetido = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Teste 2 - Array com elementos repetidos:")
    print("Original:", array_repetido)
    quicksort(array_repetido)
    print("Ordenado:", array_repetido)
    print("Correto?", array_repetido == sorted(array_repetido.copy()))
    print()

    tamanho = 10000
    array_grande = [random.randint(1, 10000) for _ in range(tamanho)]
    print(f"Teste 3 - Array grande ({tamanho} elementos):")
    inicio = time.time()
    quicksort(array_grande)
    fim = time.time()
    print(f"Tempo: {(fim - inicio)*1000:.2f}ms")
    print("Correto?", array_grande == sorted(array_grande.copy()))
    print()

    array_ordenado = list(range(500))
    print("Teste 4 - Array já ordenado (500 elementos):")
    inicio = time.time()
    quicksort(array_ordenado)
    fim = time.time()
    print(f"Tempo: {(fim - inicio)*1000:.2f}ms")
    print("Correto?", array_ordenado == sorted(array_ordenado.copy()))

test_quicksort()