def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " Chilenos tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $"+ dolares + " dólares")


def run():
    menu = """
    Bienvenido al conversor de monedas 💰 

    1 - Pesos Chilenos
    2 - Pesos Colombianos
    3 - Pesos Argentinos
    4 - Pesos Mexicanos 

    Elige una opción: """

    opcion = input(menu)

    if opcion == '1':
        conversor("Chilenos", 814.14)
    elif opcion == '2':
        conversor("Colombianos", 3766.87)
    elif opcion == '3':
        conversor("Argentinos", 99.68)
    elif opcion == '4':
        conversor("Mexicanos", 20.56)
    else:
        print('Ingresa una opción correcta por favor')
    conversor("Chilenos", 814.14)


if __name__ == '__main__':
    run()
