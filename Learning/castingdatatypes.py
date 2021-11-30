a = input ('Enter A Number:')
b = input ('Now Enter Another Number: ')

sum = a+b
print('\nData Type sum :', sum, type(sum))

sum = int(a) + int (b)
print('Data Type sum :', sum, type(sum))

sum = float(sum)
print('Data Type sum :', sum, type(sum))

sum = chr(int(sum))
print('Data Type sum :', sum, type(sum))

sum = hex(int(a)) + hex(int(b))
print('Data Type sum :', sum, type(sum))


sum = oct(int(a)) + oct(int(b))
print('Data Type sum :', sum, type(sum))
