from model import Model

inputDirectory = 'ressources/'
outputFile = 'target/'

inputFiles = []
outputFiles = []

inputFiles.append(inputDirectory + 'a_example.txt')
outputFiles.append(outputFile + 'A.txt')

inputFiles.append(inputDirectory + 'b_read_on.txt')
outputFiles.append(outputFile + 'B.txt')

inputFiles.append(inputDirectory + 'c_incunabula.txt')
outputFiles.append(outputFile + 'C.txt')

inputFiles.append(inputDirectory + 'd_tough_choices.txt')
outputFiles.append(outputFile + 'D.txt')

inputFiles.append(inputDirectory + 'e_so_many_books.txt')
outputFiles.append(outputFile + 'E.txt')

inputFiles.append(inputDirectory + 'f_libraries_of_the_world.txt')
outputFiles.append(outputFile + 'F.txt')

for i in range(len(inputFiles)):
    print(inputFiles[i])
    myGame = Model()
    myGame.loadData(inputFiles[i])
    myGame.goodOne()
    # myGame.printModel()
    myGame.outSolution(outputFiles[i])

print('ended')