import Blocks

image_file = 'heartsun.jpg'

out_file = 'myfile.jpg'


with open(image_file, 'rb') as infile:
    file_contents = infile.read()

    new_contents = Blocks.start(file_contents)
    with open(out_file,'wb') as outfile:
        outfile.write(new_contents)
