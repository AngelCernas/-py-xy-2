import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')


print('head',iris.head())
print('')


print('Lista')
list_from_csv = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',names = ['sl','sw','pl','pw','class'])
datalist = list_from_csv.pl.to_list()
print(datalist)

print('Diccionario')
dict_from_csv = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',usecols = ['sepal width']).to_dict()
print(dict_from_csv)



print('Tupla')
#print(irisTUP["sepal length"])
irisTUP = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',usecols = ['sepal length'])
dataTUP = []
for i in irisTUP.index:
    dataTUP.append(tuple(irisTUP.values[i]))
allnodes = tuple(dataTUP)
print(allnodes)
