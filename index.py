import time

def criarFila():
    fila = []
    return fila

def vazia(fila):
    return len(fila) == 0

def enfileirar(fila, item):
    fila.append(item) 

def desenfileirar(fila):
    if vazia(fila):
        return "Fila vazia!"
    return fila.pop(0)

# Criação das filas
filaEspecial = criarFila()
filaComum = criarFila()

# Leitura do arquivo fichamento.txt
with open('fichamento.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        paciente = linha.strip().split()
        nome = paciente[0]
        idade = int(paciente[1])
        prioridade = None
        if len(paciente) > 2:
            prioridade = paciente[2]
        if prioridade in ['G', 'L', 'D'] or idade > 65:
            enfileirar(filaEspecial, nome)
        else:
            enfileirar(filaComum, nome)

# Chamada dos pacientes
while not vazia(filaEspecial) or not vazia(filaComum):
    if not vazia(filaEspecial):
        print("Chamando paciente da fila especial:", desenfileirar(filaEspecial), "chamado!")
        time.sleep(2)

    if not vazia(filaEspecial):
        print("Chamando paciente da fila especial:", desenfileirar(filaEspecial), "chamado!")
        time.sleep(2)

    if not vazia(filaComum):
        print("Chamando paciente da fila comum:", desenfileirar(filaComum), "chamado!")
        time.sleep(2)
