# ----------------------------
## FUNDAMENTOS
## Estudar os fundamentos e boas práticas
# ----------------------------

# Tipos básicos
nome = "Thiago"
idade = 34
altura = 1.80
ativo = True

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Ativo? {ativo}")

# Listas e dicionários
numeros = [10, 20, 30, 40]
usuario = {"nome": nome, "idade":idade}

# Estruturas de controle
for n in numeros:
    if n > 25:
        print(f"{n} é maior que 25")
    else:
        print(f"{n} é menor ou igual a 25")

# Funções
def saudacao(nome):
    return f"Olá, {nome}!"

mensagem = saudacao("Thiago")
print(mensagem)

# List comprehension
dobrados = [n*2 for n in numeros if n > 15]
print("Números dobrados:", dobrados)

# Organização
def media(lista):
    return sum(lista) / len(lista)

print("média:", media(numeros))

#--------------------------------------
# Mais exemplos de FOR e LIST COMPREHENSION
idades = [15, 20, 32, 17, 45, 32, 21, 16]
maiores = []

for idade in idades:
    if idade >= 18:
        maiores.append(idade)

print(maiores)

# List
maiores = [idade for idade in idades if idade >= 18]
print (maiores)

#--------------------------------------
# Outro exemplo

notas = [5.5, 7.2, 8.1, 9, 5.9]
notas_aprovadas =[]

for nota in notas:
    if nota >= 7:
        notas_aprovadas.append(nota * 10)

print(notas_aprovadas)

# List

notas_aprovadas = [nota * 10 for nota in notas if nota >= 7]

print(notas_aprovadas)

#--------------------------------------
# Outro exemplo

usuarios = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 17},
    {"nome": "Carlos", "idade": 30}
]

maiores =[]

for usuario in usuarios:
    if usuario["idade"] >= 18:
        maiores.append(usuario["nome"])

print(maiores)


# List
maiores = [u["nome"] for u in usuarios if u["idade"] >= 18]
print(maiores)


#--------------------------------------
# Outro exemplo
valores = [100, 125, 132, 87, 56, 32, 65, 12, 25, 165, 180, 95, 105]
dolar = 5.22

maior_dolar = []

for convertido in valores:
    if convertido/dolar >= 20:
        maior_dolar.append(convertido/dolar)

print(maior_dolar)

# List
maior_dolar = [convertido/dolar for convertido in valores if convertido/dolar >= 20]
print(maior_dolar)
