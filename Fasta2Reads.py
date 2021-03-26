import random
import sys

#User input
input_file = "test.fasta"
#input_file = str(input("Enter the name of the input file : "))
loop = int(input("Enter the number of loops you want to run (the more loops the better and bigger the file): "))
loop = loop - 1

fasta = []
test = []
with open(input_file) as file_one:
    for line in file_one:
        line = line.strip()
        if not line:
           continue
        if line.startswith(">"):
            active_sequence_name = line[1:]
            if active_sequence_name not in fasta:
                test.append(''.join(fasta))
                fasta = []
            continue
        sequence = line
        fasta.append(sequence)

# Flush the last fasta block to the test list
if fasta:
    test.append(''.join(fasta))

#Run the code 100 times
seq = ''.join(fasta)
out =""
seq_len = len(seq)
for j in range(loop):
    start = 0
    end = 0
   
   #Add ">read"
    while (end < seq_len):
        x = random.randint(100,200)
        end = int(end + x)
        newline = ">read \n"
        out += newline
        read = str(seq[start:end])
        out += read
        out += "\n"
        start = int(start + x)

file_name = input_file[0:len(input_file)-6]
output_file = str(file_name + "_out.fasta")    
        
#Write to file
fasta_file = open(output_file , "w")
n = fasta_file.write(out)
fasta_file.close()
