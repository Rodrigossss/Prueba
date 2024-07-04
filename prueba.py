

from os import system
import os
import csv
import time

system("cls")


ventas = 0
piso_5= 100000
piso_4= 60000
piso_3= 30000
cliente = [["nombre","rut","entrada","salida"],]
habitaciones=[
["piso 1 habitacion 1","Disponible"],["piso 1 habitacion 2","Disponible"],["piso 1 habitacion 3","Disponible"],["piso 1 habitacion 4","Disponible"],["piso 1 habitacion 5","Disponible"],["piso 1 habitacion 6","Disponible"],["piso 1 habitacion 7","Disponible"],["piso 1 habitacion 8","Disponible"],
["piso 2 habitacion 1","Disponible"],["piso 2 habitacion 2","Disponible"],["piso 2 habitacion 3","Disponible"],["piso 2 habitacion 4","Disponible"],["piso 2 habitacion 5","Disponible"],["piso 2 habitacion 6","Disponible"],["piso 2 habitacion 7","Disponible"],["piso 2 habitacion 8","Disponible"],
["piso 3 habitacion 1","Disponible"],["piso 3 habitacion 2","Disponible"],["piso 3 habitacion 3","Disponible"],["piso 3 habitacion 4","Disponible"],["piso 3 habitacion 5","Disponible"],["piso 3 habitacion 6","Disponible"],["piso 3 habitacion 7","Disponible"],["piso 3 habitacion 8","Disponible"],
["piso 4 habitacion 1","Disponible"],["piso 4 habitacion 2","Disponible"],["piso 4 habitacion 3","Disponible"],["piso 4 habitacion 4","Disponible"],["piso 4 habitacion 5","Disponible"],["piso 4 habitacion 6","Disponible"],["piso 4 habitacion 7","Disponible"],["piso 4 habitacion 8","Disponible"],
["piso 5 habitacion 1","Disponible"],["piso 5 habitacion 2","Disponible"],["piso 5 habitacion 3","Disponible"],["piso 5 habitacion 4","Disponible"],["piso 5 habitacion 5","Disponible"],["piso 5 habitacion 6","Disponible"],["piso 5 habitacion 7","Disponible"],["piso 5 habitacion 8","Disponible"],
]
while True:
    try:
        opcion = int(input("""                           
=====HOTEL=====
1) Reservar habitacion
2) Buscar habitacion
3) Ver Estado
4) Ventas Diarias
5) Guardar
6) Salir                                                     
Ingrese una opcion >>>"""))
    except: print(f"Ingresa una opcion valida{ValueError}")

    if opcion == 1:
        print("*RECORDATORIO*")
        print("""Las habitaciones del piso 5 son premium y tienen un costo de 100.000 pesos diarios. Las habitaciones del piso 4 cuestan $60.000 y el resto de las habitaciones cuestan $30.000.""")
        habitacion = (input("Ingrese la habitacion que quiere reservar(EJ: piso 1 habitacion 1) >>"))
        cliente.append(input("Ingrese su nombre y apellido >>>"))
        cliente.append(input("Ingrese su rut >>>"))
        cliente.append(input("Ingrese su hora de entrada >>>"))
        cliente.append(input("Ingrese su hora de salida >>>"))
        print(cliente)
        if habitacion == [4]:
            ventas= ventas + piso_4
        elif habitacion == [5]:
            ventas= ventas + piso_5
        else:
            ventas = ventas + piso_3
        #La información de cada habitación se compone de los datos: Número de habitación, 
        # estado de reserva, valor diario de la reserva, nombre, apellido, rut, fecha:hora de entrada y fecha:hora de salida.
    if opcion == 2:
        try:
            buscar = input("Ingrese la habitacion que desea buscar(EJEMPLO :piso 1 habitacion 1) >>")
        except:
            print(f"**Ingreso un caracter invalido**{ValueError}")
        for fila in range(5):
            for colu in range(8):
                print("")
                habitaciones[fila][colu][buscar]= "Disponible"
    if opcion ==3:
        print(habitaciones)
    elif opcion ==4:
        for fila in range(5):
            for colu in range(8):
                habitaciones[fila][colu] = "ocupado"
                print(f"El total de las ventas hoy fue{ventas}")
    if opcion == 5:
        with open("habitaciones.csv","w",newline="")as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(([habitaciones]))
    if opcion ==6:
        system("cls")
        print("Saliendo del menu...")
        time.sleep(1)
        break