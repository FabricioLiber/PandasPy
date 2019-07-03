import pandas as pd
import numpy as np

# Array unidimensional, uma lista de valores. 
notas = pd.Series([2,7,5,10,6])
print('Notas:\n{}\n'.format(notas))

notas = pd.Series([10,8,10], ["Fabrício", "Knalia", "Monitora"])
print('Índices das notas:\n{}\n'.format(notas.index))

print('Nota de Fabrício:\n{}\n'.format(notas["Fabrício"]))

# Média
print('Média:\n{}\n'.format(notas.mean()))

# Desvio Padrão
print('Desvio Padrão:\n{}\n'.format(notas.std()))

# Descrever as estatísticas dos dados
print('Describe:\n{}\n'.format(notas.describe()))

# Pode se aplicar expressões do NumPy
print('NumPy Log:\n{}'.format(np.log(notas)))