usuarios = [{'Gustavo' : 'Esnupu12', 'Alfredo' : '3930'},
            {'Matias' : '123'}]

usuarios[0]['Olivare'] = usuarios[0].pop('Gustavo')

for lista in usuarios:
    for n, c in lista.items():
        print(n)
