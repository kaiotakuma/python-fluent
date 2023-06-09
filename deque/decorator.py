import time

# Define nosso decorator
def calcula_duracao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        print(f'Tempo de execução é {tempo_final - tempo_inicial} ')

    return wrapper

# Decora a função com o decorator
@calcula_duracao
def perde_tempo():
    for n in range(0, 100000000000000000):
        pass

# Executa a função main
perde_tempo()