def conversion_moneda(valor_moneda, nombre_moneda):
    pesos = input("¿Cuantos pesos "+nombre_moneda+" tienes?: ")
    pesos = float(pesos)

    valor_dolar = valor_moneda

    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)

    print("Tienes $" + dolares + " dolares")


menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos 🇨🇴
2 - Pesos Argentinos 🇦🇷
3 - Pesos Mexicanos 🇲🇽

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversion_moneda(3875, "Colombianos")
elif opcion == 2:
    conversion_moneda(65, "Argentinos")

elif opcion == 3:
    conversion_moneda(20, "Mexicanos")
else:
    print("imgresa una opcion correcta")
