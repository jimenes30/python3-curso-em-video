# Programa principal
from ex108 import moeda
p = float(input("Digite o Preço: R$ "))
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p))}')
print(f'Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(p))}')
