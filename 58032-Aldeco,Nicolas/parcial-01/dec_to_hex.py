def decimal_to_hexa(decimal):
    div = decimal
    count = str(decimal)
    hexa = ''
    ct = len(count)
    while ct != 0:
        rest = div%16
        mod = str(rest)
        div = int(div/16)
        if rest >= 10:
            if mod == '10':
                mod = 'A'
            if mod == '11':
                mod = 'B'
            if mod == '12':
                mod = 'C'
            if mod  == '13':
                mod = 'D'
            if mod == '14':
                mod = 'E'
            if mod == '15':
                mod = 'F'
        if div == 0:
            ct = 1
        hexa += mod
        ct -= 1
    result = hexa[::-1]

    return result