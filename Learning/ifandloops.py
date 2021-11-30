# If Statements
################################################################################

num = int(input('Please Enter A Number: '))

# Single expression (condition)
if num > 5 :
    print('Number Exceeds 5')
elif num < 5 :
    print('Number is Less Than 5')
else :
    print('Number Is 5')
# Multiple expressions (Conditions)
if num > 7 and num < 9 :
    print('Number is 8')
if num == 1 or num == 3 :
    print('Number Is 1 or 3')

print('')
print('')

# Loops - While
################################################################################
i = 1
while i < 4 :
    print( '\nOuter Loop Iteration:' , i )
    i += 1
    j = 1
    while j < 4 :
        print('\tInner Loop Iteration:' , j )
        j += 1

# Loops - over
################################################################################
chars = ['A' , 'B', 'C']
fruit = ('Apple', 'Banana', 'Cherry')
dict = {'name' : 'Mike' , 'ref' : 'Python' , 'sys' : 'Win'}

print('\nElements:\t' , end = ' ')
for item in chars :
    print(item , end = ' ' )
print('\nEnumerated:\t' , end = ' ')
for item in enumerate(chars) :
    print(item , end = ' ')
print('\nZipped:\t' , end = ' ')
for item in zip(chars , fruit) :
    print(item , end = ' ')
print('\nPaired:')
for key , value in dict.items() :
    print( key , '=' , value )

# Loops - breaking
################################################################################
for i in range( 1, 4 ) :
    for j in range( 1, 4 ) :
        print('Running i=' , i , ' j=' , j )
        
