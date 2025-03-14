from readIn import readFile
from helperFunctions import scorePossibleUtterancesSet as sPUs
from helperFunctions import scorePossibleUtterancesMult as sPUm
from helperFunctions import scorePossibleUtterancesAware as sPUa
from helperFunctions import scorePossibleUtterancesRandom as sPUr
from helperFunctions import createUnitScoresProportional as cUS

# Possible values for parameters
# @param selectionFunction: set, mult, aware, random
# I'm not gonna have any of the other ones work sorry. Cool idea though!
# TODO possibly implement different scoring functions, e.g. linear or a new one i just thought of called "just ones". lol
# @return a list of utterances, in order :)
def scriptSelection(udcm, overallDiphoneCounts, selectionFunction = 'set', endCondition = 'numberChosen', endConditionParameter = 22, scoringFunction = 'proportional'):

    # # store a set of all the diphones so that we can terminate once we have all of them, if we want!
    diphoneSet = set(overallDiphoneCounts.copy().keys())

    # Now we'll continuously greedily select the best utterance, by adding up the scores of all the utterances and normalizing by length of utterance

    # These lines test the difference between the two methods of scoring utteranceScore
    # in sPUs, we only add the score of each diphone once, whereas in sPUm we add the score of each diphone once PER instance
    # in both we normalize by number of diphones in the utterance!
    # HYPOTHESIS: coverage is better in sPUs rather than sPUm, because sPUm rewards redundancy rather than punishing it!
    # 
    # print(sPUs(udcm, overallDiphoneCounts)[12:30])
    # print(sPUm(udcm, overallDiphoneCounts)[12:30])

    utterancesInOrder = []
    while (len(utterancesInOrder) < endConditionParameter):
    # while (len(diphoneSet) != 0):
    # while (len(udcm) != 0):
        match selectionFunction:
            case 'set':
                sortedUtterancesList = sPUs(udcm, cUS(overallDiphoneCounts))
            case 'mult':
                sortedUtterancesList = sPUm(udcm, cUS(overallDiphoneCounts))
            case 'aware':
                sortedUtterancesList = sPUa(udcm, cUS(overallDiphoneCounts), diphoneSet)
            case 'random':
                sortedUtterancesList = sPUr(udcm)
            case _:
                print('uhhhhH just using set idk man')
                sortedUtterancesList = sPUs(udcm, cUS(overallDiphoneCounts))
        
        chosenUtt = sortedUtterancesList[0][0]
        utterancesInOrder.append(chosenUtt)
        currentUttCountsMap = udcm.pop(chosenUtt)
        newOverallDiphoneCounts = overallDiphoneCounts.copy()
        for diphone in currentUttCountsMap.keys():
            if diphone == 'total' : continue
            newOverallDiphoneCounts[diphone] -= currentUttCountsMap[diphone]
            if diphone in diphoneSet:
                diphoneSet.remove(diphone)
        overallDiphoneCounts = newOverallDiphoneCounts

    return utterancesInOrder