from readIn import readFile
from scriptSelection import scriptSelection
from evaluation import visuallyEvaluateUtterances
from evaluationScoringFunctions import visuallyEvaluateUtterancesScoring

udcm, overallDiphoneCounts = readFile('simonH.txt')

numberOfUtterances = 400

utteranceListList = []

utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=numberOfUtterances, scoringFunction='linear'))
utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=numberOfUtterances, scoringFunction='ones'))
utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'random', endConditionParameter=numberOfUtterances))

namesList = ['Proportional', 'Linear', 'Ones', 'Butts'] # DESCRIBE the four things

# print(evaluateUtterance(randUtts, udcm.copy(), overallDiphoneCounts.copy()))
visuallyEvaluateUtterancesScoring(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), namesList, verbose=True)
