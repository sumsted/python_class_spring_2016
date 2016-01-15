# Read one line of a text file. 
f = open('sample.txt','r')
first_line = f.readline()
print('first line:', first_line)
f.close()

# Iterate through all lines of a text file.
f = open('sample.txt','r')
for line in f:
    print('line:', line)
f.close()

# Read the entire file in a single text call.
f = open('sample.txt','r')
entire_file = f.read()
print('entire file:', entire_file)
f.close()

# Read using with
with open('sample.txt','r') as f:
    for line in f:
        print('with line:',line)