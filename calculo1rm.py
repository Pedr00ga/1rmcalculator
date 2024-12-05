def calcula1rm (carga, reps, rpe):
    #Repetições em reserva
    rir = 10 - rpe
    #Coeficiente do calculo
    coef = 0.03

    #Calculo de RM
    primeiro = (36 / (37 - reps)) 
    segundo = carga * primeiro
    terceiro = rir * coef
    quarto = 1 - terceiro
    rmestimado = (segundo + 6) / quarto

    return round(rmestimado, 2)

#Chama função e coloca os inputs para as variaveis
resultado = calcula1rm(carga = int(input("Digite a carga levantada (em kg): ")),
reps = int(input("Digite o número de repetições realizadas: ")),
rpe = float(input("Digite o RPE (de 4 a 10): ")))

#Mostra resultado em kg
print(f"Parabens seu nome 1 REP MAX é: {resultado} kg")