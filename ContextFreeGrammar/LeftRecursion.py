import copy

numRules = int(input('Enter the number of non-terminals'))

ProductionRules = []
for i in range(numRules):
    ProductionRules.append(input('Enter the production rule'))

Production = {}
for i in range(len(ProductionRules)):
    NT = ProductionRules[i].split('-->')[0]
    RightSide = ProductionRules[i].split('-->')[1].split('|')

    Production[NT] = RightSide

def Remove(pd):
    NewProduction = copy.deepcopy(pd)
    for NT in pd.keys():
        toChange = []
        for i in range(len(pd[NT])):
            if NT == pd[NT][i][0]:
                toChange.append(pd[NT][i])
            else:
                pass

        if len(toChange) != 0:
            NewProduction[NT + r"'"] = ['EPSILON']
            for i in toChange:
                NewProduction[NT].remove(i)
                NewProduction[NT + r"'"].append(i[1:] + NT + r"'")

            if len(NewProduction[NT]) == 0:
                NewProduction[NT].append(NT + r"'")
            else:
                for j in range(len(NewProduction[NT])):
                    if NewProduction[NT][j] == 'EPSILON':
                        NewProduction[NT][j] = NT + r"'"
                    else:
                        NewProduction[NT][j] = (NewProduction[NT][j] + NT + r"'")

    for key in NewProduction.keys():
        print(key, ' --> ', end = '')
        for i in range(len(NewProduction[key])):
            if not (i == len(NewProduction[key]) - 1):
                print(NewProduction[key][i], ' | ', end = '')
            else:
                print(NewProduction[key][i], end = '')
        print()

Remove(Production)
