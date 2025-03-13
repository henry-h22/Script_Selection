from readIn import readFile
from scriptSelection import scriptSelection
from evaluation import evaluateUtterance

udcm, overallDiphoneCounts = readFile('simonH.txt')

setUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set')
multUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'mult')
awareUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware')

print(evaluateUtterance(setUtts, udcm.copy(), overallDiphoneCounts.copy()))
