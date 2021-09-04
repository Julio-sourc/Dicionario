#Utilizando os conceitos sobre list e dict, desenvolva um algoritmo que apresente para os dados abaixo:
#A Maior nota
#A Menor nota
#A Média das notas

alunos = []
alunos.append({'nome': 'Aluno 01', 'curso': 'Ciências da Computação', 'AV1':8 })
alunos.append({'nome': 'Aluno 02', 'curso': 'Sistemas de Informação', 'AV1':7 })
alunos.append({'nome': 'Aluno 03', 'curso': 'Sistemas de Informação', 'AV1':6 })
alunos.append({'nome': 'Aluno 04', 'curso': 'Sistemas de Informação', 'AV1':6 })
alunos.append({'nome': 'Aluno 05', 'curso': 'Sistemas de Informação', 'AV1':6 })
alunos.append({'nome': 'Aluno 06', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':7 })
alunos.append({'nome': 'Aluno 07', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':9 })
alunos.append({'nome': 'Aluno 08', 'curso': 'Ciências da Computação', 'AV1':10 })
alunos.append({'nome': 'Aluno 09', 'curso': 'Ciências da Computação', 'AV1':10 })
alunos.append({'nome': 'Aluno 10', 'curso': 'Ciências da Computação', 'AV1':4 })
alunos.append({'nome': 'Aluno 11', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':5 })
alunos.append({'nome': 'Aluno 11', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':5 })
alunos.append({'nome': 'Aluno 12', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':9 })
alunos.append({'nome': 'Aluno 13', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':9 })
alunos.append({'nome': 'Aluno 14', 'curso': 'Ciências da Computação', 'AV1': 7})
alunos.append({'nome': 'Aluno 15', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':7})
alunos.append({'nome': 'Aluno 16', 'curso': 'Ciências da Computação', 'AV1': 6})
alunos.append({'nome': 'Aluno 17', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':8 })
alunos.append({'nome': 'Aluno 18', 'curso': 'Ciências da Computação', 'AV1':4 })
alunos.append({'nome': 'Aluno 19', 'curso': 'Sistemas de Informação', 'AV1':2 })
alunos.append({'nome': 'Aluno 20', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':9 })


media = 0
max_notas = 0
for dicionario in alunos:
    if dicionario['AV1'] > max_notas:
        max_notas = dicionario['AV1']

min_notas = 10
for dicionario in alunos:
    if dicionario['AV1'] < min_notas:
        min_notas = dicionario['AV1']

notas = []
for dicionario in alunos:
    notas.append(dicionario['AV1'])
            
print('Notas Gerais')
print('A MAIOR nota é.....:', max_notas)
print('A MENOR nota é.....:', min_notas)
print('A MÉDIA das notas é:', sum(notas) / len(notas))
