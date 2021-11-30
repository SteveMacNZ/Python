# Doing Maths

a = 8
b = 2

print ('Addition:\t', a, '+', b, '=', a + b)
print ('Subtraction:\t', a, '-', b, '=', a - b)
print ('Multiplication:\t' , a , 'x' , b , '=' , a * b )

print ('Division:\t' , a , '÷' , b , '=' , a / b )
print ('Floor Division:\t' , a , '÷' , b , '=' , a // b )

print ('Modulo:\t' , a , '%' , b , '=' , a % b )

print ('Exponent:\t' , a , '² = ' , a ** b , sep = '' )


# Assigning Values
a = 8
b = 4

print ('Assign Values:\t\t', 'a=', a, '\tb=', b)

a += b
print ('Add & Assign:\t\t', 'a=', a, '(8+4)')

a -= b
print( 'Subtract & Assign:\t' , 'a =' , a , ' (12 - 4)' )
a *= b
print( 'Multiply & Assign:\t' , 'a =' , a , '(8 x 4)' )

a /= b
print( 'Divide & Assign:\t' , 'a =' , a , '(32 ÷ 4)' )
a %= b
print( 'Modulo & Assign:\t' , 'a =' , a , '(8 % 4)' )