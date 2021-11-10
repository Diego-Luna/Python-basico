def es_primo(numero):
    for i in range(1, numero + 1):
        valor = numero % i
        if i == 1 or i == numero:
            continue
        if valor == 0:
            return False
        else:
            return True


def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()
