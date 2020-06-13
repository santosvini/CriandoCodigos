print("Declaração Imposto de Renda - 2020\n")

sal = float(input("Informe seu salario R$ "))

print("""Faixa Salarial:\n
    1. Até 1.903,98 - Sem dedução
    2. De 1.903,99 a 2.826,55 - dedução de 7.5%
    3. De 2.826,56 a 3.751,05 - dedução de 15%
    4. De 3.751,06 a 4.664,68 - dedução de 22,5%
    5. Acima de 4.664,68 - dedução de 27.5%
    """)

lista = [1, 5]

if sal <= 1903.98:
    print("O seu salário está na faixa 1!\n")
    print(f"Não haverá dedução")
elif (sal >= 1903.99) and (sal <= 2826.55):
    desc = sal * (7.5/100) - 142.80
    print("O seu salaéio está na faixa 2!\n")
    print(str(f"O valor descontado é de {desc:.2f}"))
elif (sal >= 2826.56) and (sal <= 3751.05):
    desc = sal * (15/100) - 354.80
    print("O seu salário está na faixa 3!\n")
    print(str(f"O valor descontado é de {desc:.2f}"))
elif (sal >= 3751.06) and (sal <= 4664.68):
    desc = sal * (22.5/100) - 636.13
    print("O seu salário está na faixa 4!\n")
    print(str(f"O valor descontado é de {desc:.2f}"))
elif sal >= 4664.68:
    desc = sal * (27.5 / 100) - 869.36
    print("O seu salário está na faixa 5!\n")
    print(str(f"O valor descontado é de {desc:.2f}"))