from readIn import readFile
from scriptSelection import scriptSelection

udcm, overallDiphoneCounts = readFile('simonH.txt')
possibleDiphones = set(overallDiphoneCounts.copy())

setUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set')
multUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'mult')
awareUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware')