# enter your own integer
my_int_number = 10
print(my_int_number)


# enter your own float
my_float_number = 4.0
print(my_float_number)

# what prints?
print('4 + 3 =',4 + 3)

print('4 - 3 =',4 - 3)

print('4 * 5 =',4 * 5)

print('4 * 5.0 =',4 * 5.0)

print('50 / 9 =',50 / 9)

print('50 // 9 =',50 // 9)

print('3 ** 2 =',3 ** 2)

print('+40 =',+40)

print('-40 =',-40)

# now you try

# add the numbers 3 and 9 then subtract 2 from the sum
# assign your answer to my_answer 
result = 3 + 9 - 2
my_answer = 10
print('3+9-2 =',result,'my_answer =', my_answer,my_answer==result)

# raise 10 to the 4th power and then divide it by 2
# assign your answer to my_answer 
result = 10**4 / 2
my_answer = 5000
print('10**4 / 2 =',result,'my_answer =', my_answer,my_answer==result)

# what is the result of this expression
# assign your answer to my_answer 
result = 2 + 4 * 3
my_answer = 14
print('2 + 4 * 3 =',result,'my_answer =', my_answer,my_answer==result)

# add 2 to 1 the using the power operator, raise the sum to the power of 3
# assign your answer to my_answer 
result = (2 + 1) ** 3
my_answer = 27
print('(2 + 1) ** 3 =',result,'my_answer =', my_answer,my_answer==result)

# what is the result of this expression
# assign your answer to my_answer 
result = 2 // 1 + 9 // 3
my_answer = 5
print('2 // 1 + 9 // 3 =',result,'my_answer =', my_answer,my_answer==result)

# what is the result of this expression
# assign your answer to my_answer 
result = -8 + 3 * 2
my_answer = -2
print('-8 + 3 * 2 =',result,'my_answer =', my_answer,my_answer==result)

# Assign an integer to a variable named my_favorite_number
my_favorite_number = 3

# multiple my_favorite_number by 3, store the result in a variable called three_favorites
three_favorites = my_favorite_number * 3

print(three_favorites)

# Assign your first name to the variable my_first_name
my_first_name = 'Frank'

# Assign you last name to the variable my_last_name
my_last_name = 'Stein'

# Add my_first_name to my_last_name. Add a space between the two. Assign it all to my_full_name.
my_full_name = my_first_name+' '+my_last_name

print("Hello,", my_full_name)

# Print the 2nd character of your last name.
print(my_last_name[1])

# Create a list with three numbers. Assign it to variable my_list.
my_list = [ 1, 2, 3]

print(str(my_list))

# Print the third number in my_list.
print(my_list[2] )

# Create a list that contains three strings. Assign the list to variable my_list.
my_list = ['Hi' ,'Bye' ,'Guy' ]

print(str(my_list))

# Print the second letter of the first string in the list.
print(my_list[0][1])

# Create a comparison of two numbers where the first number is less than the second number
print( 3 < 5 )

# Create a comparison to test if one number is between two others.
print( 3 < 4 < 5 )

# Assign a comparison to the variable yep where the value of the comparison of test_me is True
test_me = 5
yep = test_me == 5
print(yep)

# Test to see if the letter 'U' is in the word Uber.
name = "Uber"
is_in =  "U" in name
print(is_in)

# Create a comparison to test if your first and last names are not equal
print(my_first_name != my_last_name)

# Create a comparison where two comparisons are combined with 'or. The result should be True.
result =  3 < 4 or 'J' in 'John'
print(result)

# Create an input statement that asks for the day of the week.
day_of_week = input('What is the day of the week? ')

# Print the variable, day_of_week.
print(day_of_week)

# Print the string "Today is Sunday" using the list days_of_week
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("Today is %s" % days_of_week[0])
