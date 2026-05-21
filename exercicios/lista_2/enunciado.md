🧠 Lista de Exercícios – Python (while, for, id, try/except, etc.)
#### 🟢 Bloco 1 – try / except (tratamento de erros)


## Exercício 1 – Entrada de usuário segura - OK

Crie um programa que:

Peça um número inteiro ao usuário

Caso o usuário digite algo inválido, exiba uma mensagem de erro

Continue pedindo até que um número válido seja digitado

💡 Isso simula validação de entrada em sistemas reais.



## Exercício 2 – Divisão segura - OK

Crie um programa que:

Peça dois números

Tente dividir o primeiro pelo segundo

Trate:

divisão por zero

entrada inválida

Exiba o resultado apenas se a operação for válida

### 🟢 Bloco 2 – Variáveis, constantes e identidade (id)


## Exercício 3 – Identidade na memória - OK

Crie um script que:

Atribua o mesmo valor a duas variáveis

Mostre o id() de cada uma

Depois altere uma delas e mostre novamente os id()

📌 Objetivo: entender quando o Python reaproveita objetos na memória.


## Exercício 4 – Mutável vs imutável 

Crie:

Uma variável com uma string

Uma variável com uma lista

Copie cada uma para outra variável

Altere a cópia

Observe o que acontece com a original

✍️ Escreva em comentário o que você percebeu.

🟢 Bloco 3 – is, is not e None

## Exercício 5 – Checagem correta de None

Crie uma função chamada buscar_usuario() que:

Retorne None se o usuário não for encontrado

Retorne um dicionário se for encontrado

Depois:

Faça a verificação correta usando is None

Não use == None

💡 Isso é padrão profissional em Python.

Exercício 6 – Comparação perigosa

Crie duas variáveis com o valor 256
Compare usando:

==


Depois repita com o valor 257
Anote o comportamento e reflita: por que isso acontece?

🟢 Bloco 4 – while, break e continue
Exercício 7 – Sistema de login simples

Crie um sistema que:

Peça senha ao usuário

Permita no máximo 3 tentativas

Use while

Use break quando a senha estiver correta

Exercício 8 – Pular valores inválidos

Crie um loop que:

Percorra números de 1 a 20

Ignore números pares (continue)

Pare o loop ao chegar no número 15 (break)

Exiba apenas os números ímpares até esse ponto

🟢 Bloco 5 – while aninhado
Exercício 9 – Tabela de multiplicação

Crie um programa que:

Use while dentro de while

Gere a tabuada de 1 até 5

Exemplo de saída esperada:

1 x 1 = 1
1 x 2 = 2
...

🟢 Bloco 6 – while / else (ponto clássico de dúvida)
Exercício 10 – Busca em lista

Dada uma lista de nomes:

nomes = ["Ana", "João", "Carlos", "Maria"]


Use while para procurar um nome digitado

Se encontrar, use break

Se não encontrar, o else do while deve exibir:

"Nome não encontrado"

🎯 Esse exercício fixa o conceito do while/else.

🟢 Bloco 7 – Iterando strings com while
Exercício 11 – Contador de letras

Crie um programa que:

Receba uma frase

Conte quantas vezes cada letra aparece

Ignore espaços

💡 Isso é base para análise de texto, logs, NLP básico.

🟢 Bloco 8 – for, range e intervalos
Exercício 12 – Sistema de parcelas

Crie um programa que:

Receba o valor total de uma compra

Receba o número de parcelas

Use for + range

Mostre o valor de cada parcela numerada

Exemplo:

Parcela 1: R$ 100.00
Parcela 2: R$ 100.00
...

🟢 Bloco 9 – Como o for funciona por baixo dos panos
Exercício 13 – Iterável manual

Sem usar for, faça:

Uma lista

Use iter()

Use next()

Capture o erro quando o iterador acabar

🎯 Isso te faz entender profundamente o for.

🧩 Desafio Final (nível estágio/júnior)
Exercício 14 – Mini sistema de validação

Crie um sistema que:

Peça idade do usuário

Valide entrada com try/except

Use while para repetir até ser válido

Use if/else

Se idade for None ou inválida, trate corretamente

Exiba:

"Menor de idade"

"Maior de idade"