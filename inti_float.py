print('Here is all about integer and float number!')

# see the type of integer and float ..............................................
number1 = 10
number2 = 10.5

print(type(number1))
print(type(number2))

# arithmetic operators............................................................

number1 = 5
number2 = 2

print('Addition :', number1 + number2)
print('Subtraction :', number1 - number2)
print('Multiplication :', number1 * number2)
print('Division :', number1 / number2)
print('Floor division: ', number1 // number2)
print('Modulus :', number1 % number2)
print('Exponent :', number1 ** number2)


# using parenthesis ...............................................................

result = 7 + 3 * 5
print('Total is: ', result)
result = (7 + 3) * 5
print('Total is : ', result)

# increment operators ..............................................................

number1 = 5
result = number1 + 1
print(result)
result += 2
print(result)

# some built in functions ..........................................................

print(abs(-5))
print(round(5.79))
print(round(5.79, 1))

# comparisons ......................................................................

num_1 = 3
num_2 = 2

print('Equal to: ', num_1 == num_2)
print('Not equal: ', num_1 != num_2)
print('Greater than: ', num_1 > num_2)
print('Less than: ', num_1 < num_2)
print('Greater than or equal: ', num_1 >= num_2)
print('Less than or equal: ', num_1 <= num_2)

# type casting......................................................................

num_1 = 8
num_2 = '2'

total = num_1 + int(num_2)
print(type(total))


print('Total is: ', total)

total = str(num_1) + num_2
print(type(total))
print('Total is: ', total)

name = 'Hasnat'
age = 25
print('His name is {}. He is {} years old.'.format(name, age))
print(f'His name is {name}. He is {age} years old.')


