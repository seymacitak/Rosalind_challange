with open (filename) as f:
    sequences = f.read()
    sequences = list(sequences)
    f.close


#our integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
print(sequences.count('A'), sequences.count('C'), sequences.count('G'), sequences.count('T'))