import Blocks

# define a variable that contains the name of your image file
input_image_file = 'mountain_in.jpg'

#define a variable that contains the name of output file
output_image_file = 'mountain_out.jpg'

# open your input file for binary read with the 'with' statement
with open(input_image_file, 'rb') as infile:
    
    # read the contents of the file into a variable 
    file_contents = infile.read()
    
    # pass the contents to Blocks.start() as a parameter, the result should
    # be stored in a new variable
    new_contents = Blocks.start(file_contents)
    
    # open a file for binary write with the 'with' statement
    with open(output_image_file, 'wb') as outfile:
        
        # write the new contents to the output file 
        outfile.write(new_contents)