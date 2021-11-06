def conversacion(mensaje):
    print("Hola")
    print("Como estás")
    print("Elegiste la opcion " + mensaje)
    # return ## retorna un resultado


opcion = input("Elige una opcion (1,2,3): ")

if opcion == "1":
    conversacion("1")
elif opcion == "2":
    conversacion("2")
elif opcion == "3":
    conversacion("3")
else:
    print("escribe la opcion correcta")
