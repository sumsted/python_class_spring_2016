Files
=====

What are files?

Files are blocks of content stored in secondary storage on a computer.
Files hold things like text, images, documents, applications.of
Using python we can read files and do cool stuff with the content. 
We can also create new files.


Types of files

Text - a series of lines of text, usually human readable, stored on a computer drive
Binary - computer readable only data stored in secondary storage, like a drive


Operations

In Python you...

1. Open a file
2. Either read or write to a file
3. Close a file

A file may be opened for read, write or for both read and write.

    # read text
    f = open('file name','r')
    
    # read binary 
    f = open('file name','rb')
    
    # write text
    f = open('file name','w')
    
    # write binary
    f = open('file name','wb')
    
    # read and write text
    f = open('file name','r+')
    
    # read and write text
    f = open('file name','r+b')

There are several statements that may be used to read or write to a file.

    # read a single line of text
    line = f.readline()
    
    # read all contents of a file, either text or binary
    all_of_file = f.read()
    
    # write a line of text to a file, the \n represent a line separator
    f.write('this is a line\n')

    # write a block of text or binary data to a file
    f.write(data)

Finally you must close the file after you finish reading and writing to it. 
You do this with the close function. If you do not close a file, it may not be available
for other programs to use.

    f.close()

Examples

Read one line of a text file. 

    f = open('sample','r')
    first_line = f.readline()
    print('first line:', first_line)
    f.close()

Iterate through all lines of a text file.

    f = open('sample','r')
    for line in f:
        print('line:', line)
    f.close()


Read the entire file in a single text call.

    f = open('sample','r')
    entire_file = f.read()
    print('entire file:', entire_file)
    f.close()


Using 'with'

The with statement lets you close an open file implicitly on purpose or
if an error is encountered.

    with open('sample','r') as f:
        for line in f:
            print('line:',line)

