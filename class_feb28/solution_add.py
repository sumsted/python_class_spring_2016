
result = 0

infile = open('numbers.dat','r')

outfile = open('sum.dat','w')

for line in infile:
    number = int(line)
    result = result + number

outfile.write(str(result))

infile.close()
outfile.close()

