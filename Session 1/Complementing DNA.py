dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

complement = dna.replace("A","t").replace("T","a").replace("G","c").replace("C","g")

#ATTENTION: it turns out, the replace function is pretty case sensetive
complement = complement.upper()

print(complement)
