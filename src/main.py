from fileParser import FileParser

parser = FileParser('./ressources/FL_insurance_sample.csv', ',', 1)
result = parser.getData()

for row in result:
    row.print()