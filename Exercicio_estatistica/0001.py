'''
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2
'''
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Trazendo dados
gorjeta = sns.load_dataset('tips')
print(gorjeta)

'''


# Criando o grafico de dontagem e disperção

sns.jointplot(x = 'total_bill', y= 'tip', data=gorjeta)
sns.jointplot(x = 'total_bill', y= 'tip', data=gorjeta, kind='reg')
sns.jointplot(x = 'total_bill', y= 'tip', data=gorjeta, kind='hex')





'''
#Graficos de variaveis de acordo com o sexo

sns.pairplot(data=gorjeta, hue = 'sex')
plt.show()

# Funcão coringa

sns.catplot(x='day', y='total_bill', kind='bar', data=gorjeta)
plt.show()

# Criando o grafico de dontagem e disperção

sns.jointplot(x = 'total_bill', y= 'tip', data=gorjeta)
sns.jointplot(x = 'total_bill', y= 'tip', data=gorjeta, kind='reg')
sns.jointplot(x = 'total_bill', y= 'tip', data=gorjeta, kind='hex')

plt.show()