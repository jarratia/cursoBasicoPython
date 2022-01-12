# pesos = input('¿Cuántos pesos colombianos tienes?: ')
# pesos = float(pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
#print("Tienes $" + dolares + " dólares")

def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuántos pesos" + tipo_pesos + "tienes?: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

#Transformar el código con condicionales
menu = """
    Bienvenido al conversor de monedas💹💲💰
    1.- Pesos chilenos
    2.- Pesos colombianos
    3.- Bolívares
"""

opcion = int(input(menu))
if opcion == 1:
    conversor("chilenos", 900)
elif opcion == 2:
    conversor("colombianos", 3875)
elif opcion == 3:
    conversor("venezolanos", 5)
else: 
    print("Ingresa una opción correcta por favor...")

    