def promedios(vec, promedio):
    vecMayoresAlPromedio = []
    vecMenoresAlPromedio = []

    for i in range(0, len(vec)):
        if vec[i] >= promedio:
            vecMayoresAlPromedio.append(vec[i])
        else:
            vecMenoresAlPromedio.append(vec[i])
    print("Los datos mayores al promedio estandar (" + str(promedio) + ") son: " + str(vecMayoresAlPromedio))
    print("Los datos menores al promedio estandar (" + str(promedio) + ") son: " + str(vecMenoresAlPromedio))

vector = [4,5,3,3.6,2]
promedioEstandar = 3.5

promedios(vector, promedioEstandar)
