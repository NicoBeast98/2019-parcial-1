import os
from dec_to_hex import decimal_to_hexa


def main():
    os.system('clear')
    print('\tCALCULADORA DECIMAL TO HEXADECIMAL')
    print('Ingrese un numero')
    num = input('>> ')
    res = check(num)
    os.system('clear')
    if res.find(' ') == -1:
        print('El numero ',num,' es ',res,' en hexadecimal')
        input('Presione una tecla para volver...')
        main()
    else:
        print (res)
        input('Presione una tecla para volver...')
        main()

def check(num):
    if not num:
        return 'ERROR -- Ingreso vacio'
    if num.isdigit() == False :
        return 'ERROR -- No puede ingresar palabras'
    else:
        resp = decimal_to_hexa(int(num))
    return resp

main()