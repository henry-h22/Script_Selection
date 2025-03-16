from readIn import readFile
from phonemeLevelInput import readFilePhoneme
from scriptSelection import scriptSelection
from evaluation import visuallyEvaluateUtterances
from evaluationScoringFunctions import visuallyEvaluateUtterancesScoring

upcm, overallPhoneCounts = readFilePhoneme('simonH.txt')
# print(upcm)

udcm, overallDiphoneCounts = readFile('simonH.txt')

numberOfUtterances = 400

utteranceListList = []

# EXPERIMENT ON SCRIPT SELECTION algs
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'mult', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'random', endConditionParameter=numberOfUtterances))

# namesList = ['Set', 'Mult', 'Aware', 'Random'] # DESCRIBE the four things


# visuallyEvaluateUtterances(utteranceListList, upcm.copy(), overallPhoneCounts.copy(), namesList, verbose=True)
# visuallyEvaluateUtterances(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), namesList, verbose=True)


# EXPERIMENT ON SCORING FUNCTIONS
utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'mult', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'mult', endConditionParameter=numberOfUtterances, scoringFunction='linear'))
utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'mult', endConditionParameter=numberOfUtterances, scoringFunction='ones'))
utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'random', endConditionParameter=numberOfUtterances))

namesList = ['Proportional', 'Linear', 'Ones', 'Random'] # DESCRIBE the four things

visuallyEvaluateUtterancesScoring(utteranceListList, upcm.copy(), overallPhoneCounts.copy(), namesList, verbose=True)
visuallyEvaluateUtterancesScoring(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), namesList, verbose=True)


# TODO write an exploration into whether length normalization matters? Maybe? the thing is it for sure does so we can just write that way later :)