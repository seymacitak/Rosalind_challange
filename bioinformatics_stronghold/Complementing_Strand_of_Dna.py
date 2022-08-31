with open (filename) as f:
    strand = f.read()
    f.close

# The reason we write the complements of the bases in lowercase here is that if we capitalize them all on one line, the result is "ACCCCCAAAAA". 
# Because, for example, after A -> T, we would have done T-> A, and so the computer would convert all of these T's back to A after converting A bases to T. So T would be some loss.
strand = strand.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print(strand)