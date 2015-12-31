# practice creating a docstring and a line comment

def give_me_three():
    '''returns the number three
    that is all
    '''
    return 3 # this is where we return the number 3

print('hi')

# practice creating blocks of code

# block
a_number = 3
another_number = 4 * a_number
some_number = 5
if another_number > 3:

    a_third_number = 4
    a_fourth_number = another_number + a_third_number

    if a_fourth_number < 4:

        print('Yeah!')some_number = 10
another_number = 4

# create an if statement that checks if some_number is greater than 4, then print "Yeah!" if True
if some_number > 4:
    print('Yeah!')

# create an if statement that checks if some_number is equal to or greater than another_number, then print "Yeah!" if True
if some_number >= another_number:
    print('Yeah!')

# create an if statement that checks if some_number is less than 11 or another_number > 0, then print "Yeah!" if True
if some_number < 11 or another_number > 0:
    print('Yeah!')

# create an if statement that checks if some_number is between 3 and 20, then print "Yeah!" if True
if 3 < some_number < 20:
    print('Yeah!')


some_word = "cow"
another_word = "fish"
# create an if statement that checks if some_word is equal to 'cow' and another_wprd is not equal to "cat", then print "Yeah!" if True
if some_word == 'cow' and another_word != 'cat':
    print('Yeah!')

# create an if statement that checks if some_word is equal to 'cow' and some_number is less than 11, then print "Yeah!" if True
if some_number == 'cow' and some_number < 11:
    print('Yeah!')

# create a block of code that loops while i is less than 10
# increment i in the code block
# create a block of code that iterates from 0 to 9
# print the iterated value in the block
i = 0
while i < 10:
    print('i =',i)
    i = i + 1  # or i += 1


# create a block of code that iterates through the list of names
# print each name in the block of code
names = ['Jefferson', 'Josh', 'Autumn', 'Emily', 'Daniel', 'Nicholas']
for name in names:
    print(name)


# define and call a function that asks for your name and then prints it
def me_luv_name():
    name = input('what name is u? ')
    print(name)

me_luv_name()


# define and call a function that asks for two numbers, then prints the sum of these numbers
def i_need_numberz():
    number_1 = int(input('give numberz 1 , pleeze? '))
    number_2 = int(input('give numberz 2 , pleeze? '))
    print('numberz 1 + numberz 2 =', number_1+number_2)

i_need_numberz()


# Define and call a function that takes a name as a parameter then prints the name
def i_print_paramz(name):
    print(name)

i_print_paramz(name)


# Define and call a function that takes two numbers as parameters then prints the sum of these numbers
def i_take_ur_numberz(number_1, number_2):
    print('numberz sum is',number_1+number_2)

i_take_ur_numberz(3,4)    

# Define and call a function that takes a name as a parameter then returns the name*2
# print the returned result
def u_get_tooz_namez(name):
    return name*2
    
print(u_get_tooz_names('Joe')


# Define and call a function that takes two numbers as parameters then returns the sum of these numbers
# print the returnedresult
def u_want_moor_numberz(number_1, number_2):
    return number_1 + number_2

print(u_want_moor_numberz(5, 6))
