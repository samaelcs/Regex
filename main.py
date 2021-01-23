from RegularExpressionGen.ParseTree import ParseTree
from RegularExpressionGen.Evaluate import evaluate

Ptree = ParseTree('( ( A * ) . ( C | B ) )')

Outputs = []
for i in range(10):
    while True:
        out = evaluate(Ptree)
        if out not in Outputs:
            Outputs.append(out)
            break

for i in range(len(Outputs)):
    print(i + 1, ' : ', Outputs[i])