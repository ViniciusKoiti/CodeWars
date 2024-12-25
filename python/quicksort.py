# -*- coding: utf-8 -*-

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