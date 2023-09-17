usuarios = [{'Gustavo' : 'Esnupu12', 'Alfredo' : '3930'},
            {'Matias' : '123'}]

nombre = input()

usuarios[0]['Olivare'] = usuarios[0].pop(nombre)

for lista in usuarios:
    for n, c in lista.items():
        print(n)
