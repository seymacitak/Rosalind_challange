mutation = 0

with open ("/Users/seymacitak/desktop/codes/rosalind/rosalind_hamm.txt") as f:
    sequences = f.read().split("\n")
    seq1= sequences[0]
    seq2 = sequences[1]
    f.close

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        mutation += 1
        i +=1
    else:
        mutation = mutation

print(mutation)


