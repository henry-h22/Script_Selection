from readIn import readFile
from scriptSelection import scriptSelection
from evaluation import evaluateUtterance
from evaluation import visuallyEvaluateUtterances

udcm, overallDiphoneCounts = readFile('simonH.txt')

numberOfUtterances = 400

propUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=numberOfUtterances, scoringFunction='proportional')
linUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=numberOfUtterances, scoringFunction='linear')
onesUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=numberOfUtterances, scoringFunction='ones')
randUtts = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'random', endConditionParameter=numberOfUtterances)

utteranceListList = [propUtts, linUtts, onesUtts, randUtts]
costFunctionsList = ['Proportional', 'Linear', 'Ones', 'Random']

# print(evaluateUtterance(randUtts, udcm.copy(), overallDiphoneCounts.copy()))
visuallyEvaluateUtterances(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), costFunctionsList, verbose=True)
