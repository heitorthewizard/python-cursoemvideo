# Manipulando cadeias de caractéries
string = 'Curso em Video Python'

# fatiamentos
print(string[9:14]) # do 9 ao 13
print(string[9:21]) # não recomendado
print(string[9:]) # melhor
print(string[0:14:2]) # pula de 2 em 2
print(string[:5]) # do início ao 4
print(string[9::3]) # do 9 ao fim pulando 3 em 3

# análise de strings
print(len(string)) # length = comprimento
print(string.count('o')) # contar quantos 'o' tem no text
print(string.count('o', 0, 14)) # contar com fatiamento do 0 ao 14
print(string.find('deo')) # encontrar index das caractéries no text
print(string.find('Android')) # procurando algo que não existe = -1
print('Curso' in string) # usando in para retornar boolean

# transformação
print(string.replace('Python', 'Android')) # sobrescreve caractéres
print(string.upper()) # ficar todas em maiúsculas
print(string.lower()) # ficar todas em minúsculas
print(string.capitalize()) # primeira letra da primeira palavra maiúscula
print(string.title()) # Basicamente um capitalize em todas as palavras
string_defeituosa = '   Aprenda Python  '
print(string_defeituosa.strip()) # remove espaços inúteis
print(string_defeituosa.rstrip()) # remove somente da direito
print(string_defeituosa.lstrip()) # remove somente da esquerda

# divisão
print(string.split()) # separa tudo onde tem espaços por padrão
virgula = 'Teste,de,virgulas'
print(virgula.split(',')) # separa onde o que colocou no argumento
splitted_string = string.split()
print('-'.join(splitted_string)) # junta strings com '-' entre elas
print(' '.join(splitted_string)) # junta strings com espaço entre elas

