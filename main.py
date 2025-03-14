from readIn import readFile
from scriptSelection import scriptSelection
from evaluation import evaluateUtterance
from evaluation import visuallyEvaluateUtterances

udcm, overallDiphoneCounts = readFile('simonH.txt')

setUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=400)
multUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'mult', endConditionParameter=400)
awareUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=400)
randUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'random', endConditionParameter=400)

utteranceListList = [setUtts, multUtts, awareUtts, randUtts]

# print(evaluateUtterance(randUtts, udcm.copy(), overallDiphoneCounts.copy()))
visuallyEvaluateUtterances(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), ['Set', 'Multiple', 'Aware', 'Random'])
