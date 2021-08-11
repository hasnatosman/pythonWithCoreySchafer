print('Let\'s discuss about Sting!')

# now printing something by calling a variable..................................

greetings = 'Hello, Hasnat !'
print(greetings)

# using back slash in single quote..............................................
greetings2 = 'Hello, Osman! How\'s it going?'
print(greetings2)

# using double quote............................................................
greetings3 = "Oh! I am doing good!"
print(greetings3)

# to see how many characters in our string......................................
string = 'Hello, Mr. Hasnat!'
print('There are', len(string), 'characters!')

# to find total number of any character in the string...........................
print('The total number of H in the string is: ', string.count('H'))

# to find out a character using index number....................................
string = 'Hello man! Are you okay?'
print('The index of A in the string is: ', string[11])
print('The index of Are in the string is: ', string[11:14])
print('The last character is: ', string[-1])
print('The second last character is: ', string[-2])

# to find any word or character from string.....................................
print('The starting index of you in the string: ', string.find('you'))

# to replace a word or character from string....................................
replaced_string = string.replace('okay', 'good')
print(replaced_string)

# concatenate two string........................................................
greeting = 'Hello'
name = 'Hasnat'
print(greeting + name)
print(greeting + ', ' + name)
print(greeting + ', ' + name + '. How are you?')

# use formatted string instead of using + again and again.......................
message = '{}, {}. How are you bro?'.format(greeting, name)
print(message)

# f string instead of formatted string to make it easy .........................

message = f'{greeting}, {name.upper()}. That\'s look so cool!'
print(message)

# ******************************* some tricks **********************************

print(dir(name))
print(help(str))
print(help(str.lower))
