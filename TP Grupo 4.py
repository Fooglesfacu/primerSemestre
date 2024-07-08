def ordenarListas (listaTiempo, listaTramo):
    largo = len (listaTiempo)
    ordenada = False
    while ordenada == False:
        ordenada = True
        for i in range (largo-1):
            if listaTiempo [i] < listaTiempo [i+1]:
                aux = listaTiempo [i]
                listaTiempo [i] = listaTiempo [i+1]
                listaTiempo [i+1] = aux
                aux = listaTramo [i]
                listaTramo [i] = listaTramo [i+1]
                listaTramo [i+1] = aux
                ordenada = False
                
def tiempoTotal (listaTiempo):
    total = 0
    largo = len (listaTiempo)
    for i in range (largo):
        total += listaTiempo [i]
    if total >= 60:
        horas = total // 60
        total -= (60*horas)
        minutos = total
        print("Tiempo total de viaje: ", horas, "horas con ", minutos, "minutos")        
    else:
        minutos = total
        print("Tiempo total de viaje: ", minutos, "minutos")
        
def cantidadTramos (listaTramo):
    tramos = len (listaTramo)
    return tramos

def tramoMasLargo (listaTiempo, listaTramo):
    tramoLargo = listaTramo [0]
    tiempo = listaTiempo [0]
    print("El tramo más largo fue el tramo ", tramoLargo, "con ", tiempo, "minutos")
    
def tiempoPromedio (listaTiempo):
    promedio = 0
    resto = 0
    largo = len (listaTiempo)
    for i in range (largo):
        promedio += listaTiempo[i]
    promedio /= largo
    if promedio % 1 != 0:
        resto = promedio % 1
        promedio //= 1
        resto *= 60
        resto //= 1
1    print("El tiempo promedio fue de ", promedio, "minutos con ", resto, "segundos")

#PROGRAMA PRINCIPAL

listaTiempo = []
listaTramo = []

tiempo = int(input("Ingresar cuanto tiempo tardo en llegar al destino del tramo o -1 para terminar: "))
tramo = 0

while tiempo == -1:
    print("No se ingresaron valores")
    tiempo = int(input("Ingresar cuanto tiempo tardo en llegar al destino del tramo o -1 para terminar: "))

while tiempo != -1:
    while tiempo < 0:
        print("El tiempo ingresado no puede ser negativo, ingresar uno válido")
        tiempo = int(input("Ingresar cuanto tiempo tardo en llegar al destino del tramo o -1 para terminar: "))
    listaTiempo.append(tiempo)
    tramo += 1
    listaTramo.append(tramo)
    tiempo = int(input("Ingresar cuanto tiempo tardo en llegar al destino del tramo o -1 para terminar: "))

print()
ordenarListas (listaTiempo, listaTramo)
tiempoTotal (listaTiempo)
tramos = cantidadTramos (listaTramo)

print ()
print("Hubo un total de ", tramos, "tramos")
print()

tramoMasLargo (listaTiempo, listaTramo)
print()

tiempoPromedio (listaTiempo)
print()

for i in range (len(listaTiempo)):
    print("Tramo ", listaTramo [i], ":", listaTiempo [i], "minutos")