from readIn import readFile
from phonemeLevelInput import readFilePhoneme
from scriptSelection import scriptSelection, scriptSelectionHybrid
from evaluation import visuallyEvaluateUtterances
from evaluationScoringFunctions import visuallyEvaluateUtterancesScoring

upcm, overallPhoneCounts = readFilePhoneme('simonH.txt')
# print(upcm)

udcm, overallDiphoneCounts = readFile('simonH.txt')

numberOfUtterances = 700

utteranceListList = []

#! Experiment 1
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'mult', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'random', endConditionParameter=numberOfUtterances))

# namesList = ['Set', 'Mult', 'Aware', 'Random'] # DESCRIBE the four things


# visuallyEvaluateUtterances(utteranceListList, upcm.copy(), overallPhoneCounts.copy(), namesList, verbose=True)
# visuallyEvaluateUtterances(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), namesList, verbose=True)


# ! experiment 1.5
# MOTIVATING HYBRID

utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=250, scoringFunction='proportional'))
utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=250, scoringFunction='proportional'))
utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=750, scoringFunction='proportional'))
utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=750, scoringFunction='proportional'))

namesList = ['Set, over 250 Utterances', 'Aware, over 250 Utterances', 'Set, over 750 Utterances', 'Aware, over 750 Utterance'] # DESCRIBE the four things


visuallyEvaluateUtterances(utteranceListList, upcm.copy(), overallPhoneCounts.copy(), namesList, verbose=True)
visuallyEvaluateUtterances(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), namesList, verbose=True)




# EXPERIMENTS ON SCORING FUNCTIONS
# ! experiment 3.1
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='linear'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='ones'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'random', endConditionParameter=numberOfUtterances))

# namesList = ['Proportional', 'Linear', 'Ones', 'Random'] # DESCRIBE the four things

# visuallyEvaluateUtterancesScoring(utteranceListList, upcm.copy(), overallPhoneCounts.copy(), namesList, verbose=True)
# visuallyEvaluateUtterancesScoring(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), namesList, verbose=True)

# ! experiment 3.2
# utteranceListList.append(scriptSelectionHybrid(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelectionHybrid(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='linear'))
# utteranceListList.append(scriptSelectionHybrid(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='ones'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'random', endConditionParameter=numberOfUtterances))

# namesList = ['Proportional', 'Linear', 'Ones', 'Random'] # DESCRIBE the four things

# visuallyEvaluateUtterancesScoring(utteranceListList, upcm.copy(), overallPhoneCounts.copy(), namesList, verbose=True)
# visuallyEvaluateUtterancesScoring(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), namesList, verbose=True)


# ! experiment 3.3
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelectionHybrid(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='ones'))
# utteranceListList.append(scriptSelectionHybrid(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'random', endConditionParameter=numberOfUtterances))

# namesList = ['Set and Proportional', 'Hybrid: Set and Ones', 'Hybrid: Set and Proportional', 'fart'] # DESCRIBE the four things

# visuallyEvaluateUtterancesScoring(utteranceListList, upcm.copy(), overallPhoneCounts.copy(), namesList, verbose=True)
# visuallyEvaluateUtterancesScoring(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), namesList, verbose=True)




# ! experiment 2.2
# TODO write an exploration into whether length normalization matters? Maybe? the thing is it for sure does so we can just write that way later :)

# # EXPERIMENT ON SCORING FUNCTIONS WITHIN HYBRID
# ! experiment 2
# utteranceListList.append(scriptSelectionHybrid(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelectionHybrid(udcm.copy(), overallDiphoneCounts.copy(), 'mult', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'aware', endConditionParameter=numberOfUtterances, scoringFunction='proportional'))
# utteranceListList.append(scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 'set', endConditionParameter=numberOfUtterances))

# namesList = ['Hybrid: Set', 'Hybrid: Mult', 'Aware', 'Set'] # DESCRIBE the four things

# visuallyEvaluateUtterancesScoring(utteranceListList, upcm.copy(), overallPhoneCounts.copy(), namesList, verbose=True)
# visuallyEvaluateUtterancesScoring(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), namesList, verbose=True)