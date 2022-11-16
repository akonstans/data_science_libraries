def clean(currency):
    '''Takes a currency considered an int and turns it into a clean float
        rounded to two decimal places'''
    x = x.replace('$', '')
    x = x.replace(',', '')
    x = round(float(x), 2)
    return x