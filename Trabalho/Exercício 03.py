def transcribe(dna):
    dna = dna.upper()
    string = {}
    string['G'] = 'C'
    string['C'] = 'G'
    string['T'] = 'A'
    string['A'] = 'U'
    rna = ''
    for i in dna:
        if i in string:
            rna = rna + string[i]
    return print(rna)

transcribe('g c t a')