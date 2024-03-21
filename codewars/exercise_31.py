def DNA_strand(dna):
    dna_ = []
    for i in dna:
        if i == 'A':
            dna_.append('T')
        elif i == 'C':
            dna_.append('G')
        elif i == 'T':
            dna_.append('A')
        elif i == 'G':
            dna_.append('C')
        else:
            dna_.append(i)
    return ''.join(dna_)


if __name__ == '__main__':
    print(DNA_strand('ATTGC'))
    print(DNA_strand('AAAA'))
    print(DNA_strand('GTAT'))
