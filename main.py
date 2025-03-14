from readIn import readFile
from scriptSelection import scriptSelection
from evaluation import evaluateUtterance
from evaluation import visuallyEvaluateUtterances

udcm, overallDiphoneCounts = readFile('simonH.txt')

numberOfUtterances = 400

setUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances)
multUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'mult', endConditionParameter=numberOfUtterances)
awareUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=numberOfUtterances)
randUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'random', endConditionParameter=numberOfUtterances)

utteranceListList = [setUtts, multUtts, awareUtts, randUtts]

# print(evaluateUtterance(randUtts, udcm.copy(), overallDiphoneCounts.copy()))
visuallyEvaluateUtterances(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), ['Set', 'Multiple', 'Aware', 'Random'])
