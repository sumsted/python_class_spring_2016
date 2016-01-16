# import the animals.py module
import animals

# ask the user for their favorite animal and store it in a variable called favorite
favorite = input('What is your favorite animal? ')

# using an if statement check to see if favorite is in the animals_dict
if favorite in animals.animals_dict:
    # if favorite is found print favorite and the value or definition of it
    print(favorite, animals.animals_dict[favorite])
else:
    # if favorite is not found print 'sorry, we can't find favorite'
    print('sorry, we can\'t find favorite')
    
    
# create a dictionary of your favorite movies, include a description

movies = {
    "Breakfast at Tiffany's":'Anyone who ever gave you confidence, you owe them alot.',
    'Cool Hand Luke':'What we got here is a failure to communicate.',
    'Jaws':'You\'re gonna need a bigger boat.'
    }

print(movies)


# pick a key and print out a item from movies dictionary

movies['Cool Hand Luke']

# use an if statement to check for a key in your dictionary

if 'Jaws' in movies:
    print('found:',movies['Jaws'])

# use a for loop to iterate through your dictionary
for k, v in movies.items():
    print(k,' : ',v)

