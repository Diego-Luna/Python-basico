def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #     continue # se salta al siguiente siclo
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break # sale del bucle

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()
