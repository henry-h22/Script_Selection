from readIn import readFile
from scriptSelection import scriptSelection

udcm, overallDiphoneCounts = readFile('simonH.txt')

print(scriptSelection(udcm.copy(), overallDiphoneCounts, 'set'))
# print(udcm)
