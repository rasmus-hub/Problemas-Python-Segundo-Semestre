clientes = {'Hernan' : '123', 'Gustavo' : '231'}

clientes['Leonardo'] = '4444'

for cliente in clientes.items():
    print(cliente)

clientes['Fernando'] = clientes.pop('Hernan')

clientes['Matias'] = '444'

print(clientes)

for cliente in clientes.items():
    print(cliente[0], cliente[1])