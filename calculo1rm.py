def calcula1rm (carga, reps, rpe):
    rir = 10 - rpe
    coef = 0.03

    primeiro = (36 / (37 - reps)) 
    segundo = carga * primeiro
    terceiro = rir * coef
    quarto = 1 - terceiro
    rmestimado = segundo / quarto

    return rmestimado


resultado = calcula1rm(carga = int(input("Digite a carga levantada (em kg): ")),
reps = int(input("Digite o número de repetições realizadas: ")),
rpe = int(input("Digite o RPE (de 4 a 10): ")))

print(f"RM estimado: {resultado} kg")