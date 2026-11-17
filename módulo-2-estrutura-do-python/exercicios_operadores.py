#Seguem 5 exercícios para reforçar a aula "Tipos de Operadores com Python".

''' 1. Relógio em dias:
    Leia um total de segundos e mostre em dias, horas, minutos e segundos.
    Exemplo: 100000 → 1d 3h 46min 40s.

print("Conversor de Segundos\n")
segundos = int(input("Digite quantos segundos você deseja converter: \n"))

dias = segundos // 86400
segundos %= 86400  #Atualizamos o valor da variável, removendo a quantidade de dias com o operador %, que realiza uma divisão e mantém apenas o resto dela.

horas = segundos // 3600
segundos %= 3600 #Aqui se mantém a lógica que usamos para o valor dos dias.

minutos = segundos // 60
segundo_final = segundos % 60

print(f"A conversão é: {dias}d, {horas}h {minutos}min {segundo_final}s.")

    Para resolver esse desafio utilizamos dos operadores:
        // -> Realiza uma divisão mas procura apenas o valor inteiro da divisão;
        % -> Realiza uma divisão e armazena apenas o resto;
        %= -> Realiza a divisão e armazena apenas o resto já atribuindo o valor a uma variável'''

''' 2. Troco em cédulas:
    Leia um valor inteiro em reais e mostre a menor quantidade de cédulas de 100, 50, 20, 10, 5 e 2 que o formam.
    Se sobrar 1 real, mostre como moeda. 
    Exemplo: 289 → 2×100, 1×50, 1×20, 1×10, 1×5 e 2×2

print("Conversor de valores em cédulas\n")
valor_reais = int(input("Digite o valor que você precisa tranferir para cédulas(Apenas valores inteiros): R$"))

valor_original = valor_reais

cem_reais = valor_original // 100
valor_original %= 100

cinquenta_reais = valor_original // 50
valor_original %= 50

vinte_reais = valor_original // 20
valor_original %= 20

dez_reais = valor_original // 10
valor_original %= 10

cinco_reais = valor_original // 5
valor_original %= 5

dois_reais = valor_original // 2
valor_original %= 2

print(f"Para converter R${valor_reais} em cédulas, você precisará de: {cem_reais}×100, {cinquenta_reais}×50, {vinte_reais}×20, {dez_reais}×10, {cinco_reais}×5 e {dois_reais}×2")'''

''' 3. Previsão de resultados:
    Escreva a previsão de cada linha antes de rodar:
    10 / 4, 10 // 4, -10 // 4, 10 % 4, -10 % 4, 2 ** 3 ** 2, not 0 or 1 and 0, 5 > 3 > 1 .
    Depois explique cada resultado com suas palavras.
    
- 10 / 4 = 2.5 (Aqui será uma simples conta de divisão, no Python não precisamos declarar o tipo da variável.)
- 10 // 4 = 2 (Aqui ainda não declaramos o tipo da variável, mas o operador "//" realiza uma divisão e nos retorna apenas o número inteiro, descartando o que tiver após a vírgula.)
- -10 // 4 = -3 (Aqui o python irá arredondar o número.)
- 10 % 4 = 0 
    '''