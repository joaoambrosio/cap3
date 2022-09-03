from cmath import atanh


man = []
other = []

with open('sketch.txt', 'r+') as file:
    file.seek(0)
    for line in file:
        try:
            (author, fala) = line.split(':', 1)
            fala = fala.strip()
            if author == 'Man':
                man.append(fala)
            elif author == 'Other Man':
                other.append(fala)

        except ValueError:
            pass

with open('athor.txt', 'w') as file_athor:
    file_athor.write("Frases ditas pelo ator principal: \n")
    for dados in man:
        file_athor.write(dados + '\n')

with open('otherathor.txt', 'w') as file_otherathor:
    file_otherathor.write("Frases ditas pelo ator coadjuvante: \n")
    for dados in other:
        file_otherathor.write(dados + '\n')

    #print("Falas do author: ", man)
    #print("Falas do outro author: ", other)
