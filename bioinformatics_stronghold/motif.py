with open (filename) as f:
    sequences= f.read().split("\n")
    seq= sequences[0]
    motif = sequences[1]
    seq = list(seq)
    motif = list(motif)

list_position = []
for i in range(len(seq)):
    if seq[i:i+len(motif)] == motif:
        list_position.append(i+1)
        i +=1
    else:
        i +=1

# Rosalind don't' accept the list as the true answer, so I changed the list to string 
listToStr = ' '.join(map(str, list_position))
print(listToStr)
