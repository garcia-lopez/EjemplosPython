listaEst = []
resp = "Si"
while(resp.upper() != "NO"):
    nombres = input("Escriba el nombre del estudiante: ")
    listaEst.append(nombres)
    resp = input("Desea agregar otro nombre si/no: ")
    while(resp.upper() != "NO"):
        tam = len(listaEst)
        print("Elementos guardados: ", tam)
        nombres = input("Escriba el nombre del estudiante: ")
        listaEst.append(nombres)
        resp = input("Desea agregar otro si/no: ")
        resp.upper()

for est in listaEst:
    print(est)

