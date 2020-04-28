from FechaHora import FechaHora

def Salir(fecha):
    pass
def Sumar(fecha):
    a = int(input("Ingrese horas a sumar: "))
    fecha = fecha + a
    fecha.controla()
    print("La fecha cambió a: {}".format(fecha.Mostrar()))

def Restar(fecha):
    a = int(input("Ingrese horas a restar: "))
    fecha = fecha - a
    fecha.controla()
    print("La fecha cambió a: {}".format(fecha.Mostrar()))

def mayor(fe):
    print ("Ingreso de otra fecha") 
    anio = int(input("Ingrese año: "))
    mes = int(input("Ingrese mes: "))
    dia = int(input("Ingrese dia: "))
    hora = int(input("Ingrese hora: "))
    mins = int(input("ingrese minutos: "))
    seg = int(input("Ingrese segundos: "))
    fecha1 = FechaHora(dia, mes, anio, hora, mins, seg)
    if fecha > fecha1:
        print("La Hora de {} es mayor que la hora de  {}".format(fecha.Mostrar(), fecha1.Mostrar()))


switcher = {
    0: Salir,
    1: Sumar,
    2: Restar,
    3: mayor,
}

if __name__ == '__main__':
    opcion=1
    anio = int(input("Ingrese año: "))
    mes = int(input("Ingrese mes: "))
    dia = int(input("Ingrese dia: "))
    hora = int(input("Ingrese hora: "))
    mins = int(input("ingrese minutos: "))
    seg = int(input("Ingrese segundos: "))
    fecha = FechaHora(dia, mes, anio, hora, mins, seg)
    while opcion != 0:
        print(" 1. Sumar Hora \n 2. Restar hora \n 3. Mayor hora \n 0. Salir")
        opcion= int(input("Ingrese una opción: "))
        switcher.get(opcion, lambda: print("Opción incorrecta"))(fecha)