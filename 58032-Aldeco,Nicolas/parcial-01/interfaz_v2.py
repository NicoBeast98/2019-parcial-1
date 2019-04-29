import os
from dec_to_hex import decimal_to_hexa
from hex_to_dec import hexadecimal_to_decimal

def main():
    os.system('clear')
    print('\tCONVERTIDOR DE UNIDADES')
    print('\tHexadecimal<>Decimal')
    print('Selecione una conversion:\n1 - DECIMAL>>HEXADECIMAL\n2 - HEXADECIMAL>>DECIMAL\n3 - SALIR\n')
    op = input('>> ')
    if op == '1':
        os.system('clear')
        print('Decimal>>Hexadecimal')
        dec = input('Ingrese un numero decimal>> ')
        res = dec_hex_ch(dec)    #progama de decimal a hexadecimal
        print(res)
        input('Presione cualquier tecla para volver...')
        main()
    elif op == '2':
        os.system('clear')
        print('Hexadecimal>>Decimal')
        hexa = input('Ingrese un numero en haxadecimal>> ')
        res = hex_dec_ch(hexa)    #programa de hexadecimal a decimal
        print(res)
        input('Presione cualquier tecla para volver...')
        main()
    elif op == '3':
        os.system('clear')
        print('Adios!')
        quit()
    else:
        print('Opcion fuera de rango selecione una correcta')
        input('Presione cualquier tecla para volver...')
        main()

def dec_hex_ch(dec):
    if not dec:
        return('ERROR - No ingreso nada')    
    elif dec.isdecimal() == False:
        return('ERROR - Debe ingresar solo numeros')
    else:
        resp = decimal_to_hexa(int(dec))
        return(f'El numero {dec} es {resp} en hexadecimal.')


def hex_dec_ch(hexa):

    if not hexa:
        return('ERROR - No ingreso nada')   
    hexa = hexa.upper()
    ct = 1
    n = 0
    if hexa.find(' ') != -1:
        return('ERROR - No puede ingresar espacios')
    if (hexa.isalnum() and hexa.isdecimal()) == False:
        for n in range(len(hexa)):
            if hexa[n].find('A') != -1:
                ct += 1
            elif hexa[n].find('B') != -1:
                ct += 1
            elif hexa[n].find('C') != -1:
                ct += 1
            elif hexa[n].find('D') != -1:
                ct += 1
            elif hexa[n].find('E') != -1:
                ct += 1
            elif hexa[n].find('F') != -1:
                ct += 1
            elif hexa[n].isdecimal() == False:
                ct = 0
    if ct == 0:
        return ('ERROR - El numero que ingreso no tiene las letras correctas')
    else:
        resp = hexadecimal_to_decimal(hexa)
        return(f'El numero {hexa} es {resp} en decimal')
    


#main()