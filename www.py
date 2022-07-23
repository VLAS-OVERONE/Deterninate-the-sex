import pandas as pd

dfru = pd.read_csv('...\\FileRus.csv')
dfen = pd.read_csv('...\\FileEng.csv')

rumalenames = set(dfru[dfru['Gender'] == 'male']['GivenName'])
rumalesurnames = set(dfru[dfru['Gender'] == 'male']['Surname'])

rufemalenames = set(dfru[dfru['Gender'] == 'female']['GivenName'])
rufemalesurnames = set(dfru[dfru['Gender'] == 'female']['Surname'])

enmalenames = set(dfen[dfen['Gender'] == 'male']['GivenName'])
enmalesurnames = set(dfen[dfen['Gender'] == 'male']['Surname'])

enfemalenames = set(dfen[dfen['Gender'] == 'female']['GivenName'])
enfemalesurnames = set(dfen[dfen['Gender'] == 'female']['Surname'])

name = input('Name: ')
surname = input('Surname: ')

if name in rumalenames and surname in rumalesurnames:
    print(name, surname, 'is male')

elif name in rufemalenames and surname in rufemalesurnames:
    print(name, surname, 'is female')

elif name in enmalenames and surname in enmalesurnames:
    print(name, surname, 'is male')

elif name in enfemalenames and surname in enfemalesurnames:
    print(name, surname, 'is female')

else:
    print('Unkown data')