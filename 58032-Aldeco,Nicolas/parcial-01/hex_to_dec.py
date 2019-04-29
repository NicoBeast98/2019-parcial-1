def hexadecimal_to_decimal(hexadec):
    dec = 0
    decimal_number = 0
    n = 0
    hexadec = hexadec[::-1]
    count = len(hexadec)
    for n in range(count):
        if hexadec[n].isdecimal() == True:
            dec = int(hexadec[n])
        if hexadec[n].isalpha() == True:
            if hexadec[n] == 'A':
                dec = 10
            elif hexadec[n] == 'B':
                dec = 11
            elif hexadec[n] == 'C':
                dec = 12
            elif hexadec[n] == 'D':
                dec = 13
            elif hexadec[n] == 'E':
                dec = 14
            elif hexadec[n] == 'F':
                dec = 15
            else:
                dec = 0
                decimal_number = 0
        decimal_number += dec*pow(16,n)
        
    return str(decimal_number)