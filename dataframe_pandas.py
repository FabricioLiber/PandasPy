import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'Aluno': ['Fabrício', 'Monitora', 'KNalia'],
        'Faltas': [10, 17, 8],
        'Prova': [8, 4, 7],
        'Seminário': [9, 6, 8]
    }
)
print('Dataframe:\n{}\n'.format(df))

# Apresentar os tipos de dados de compõe as colunas
print('Tipos de Dados:\n{}\n'.format(df.dtypes))

# Acessar Lista de Colunas
print('Lista de Colunas:\n{}\n'.format(df.columns))

# Acessar uma coluna específica
print('Acessar Coluna Aluno:\n{}\n'.format(df['Aluno']))

# Descrever as estatísticas dos dados
print('Describe:\n{}\n'.format(df.describe()))

# Ordenar por determinada coluna
print('Ordenar por Nome:\n{}\n'.format(df.sort_values(by='Aluno')))

# Selecionar linha por um index específico
print('Linha do Index 2:\n{}\n'.format(df.loc[2]))

# Selecionar de acordo com critérios condicionais (Boolean Indexing)
print('Alunos com a nota do seminário maior que 8:\n{}\n'.format(df[df['Seminário'] > 8]))

# Selecionar a partir de vários critérios condicionais de colunas diferentes
# Usa-se operadores Bitwise
print('Alunos com a nota da seminário e prova maior que 6:\n{}\n'.format(
    df[(df['Seminário'] > 6) & (df['Prova'] > 6)])
)

# Selecionar linha por um index específico levendo em consideração
# o número do índice como parada
print('Linhas até o índice 1:\n{}\n'.format(df.sort_values(by='Aluno').loc[:1]))

# Selecionar linha por um index específico levendo em consideração
# o quantidade de índices como parada
print('Apresentar 1 linha:\n{}\n'.format(df.sort_values(by='Aluno').iloc[:1]))


# Apresentar todos os valores de todas as linhas
print('Valores de todas as Linhas:\n{}\n'.format(df.sort_values(by='Aluno').iloc[:, :].values))