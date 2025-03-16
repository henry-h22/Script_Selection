from readIn import readFile
from helperFunctions import scorePossibleUtterancesSet as sPUs
from helperFunctions import scorePossibleUtterancesMult as sPUm
from helperFunctions import scorePossibleUtterancesAware as sPUa
from helperFunctions import scorePossibleUtterancesRandom as sPUr
from helperFunctions import createUnitScoresProportional as cUSp
from helperFunctions import createUnitScoresLinear as cUSl
from helperFunctions import createUnitScoresOnes as cUSo

# Possible values for parameters
# @param selectionFunction: set, mult, aware, random
# @param scoringFunction: proportional, linear, ones
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
    while (len(utterancesInOrder) < endConditionParameter and len(diphoneSet) != 0):
    # while (len(diphoneSet) != 0):
    # while (len(udcm) != 0):

        match scoringFunction:
            case 'proportional':
                scores = cUSp(overallDiphoneCounts.copy())
            case 'linear':
                scores = cUSl(overallDiphoneCounts.copy())
            case 'ones':
                scores = cUSo(overallDiphoneCounts.copy())
            case _:
                print('uuHHH just using proportional')
                scores = cUSp(overallDiphoneCounts)

        match selectionFunction:
            case 'set':
                sortedUtterancesList = sPUs(udcm, scores)
            case 'mult':
                sortedUtterancesList = sPUm(udcm, scores)
            case 'aware':
                sortedUtterancesList = sPUa(udcm, scores, diphoneSet)
            case 'random':
                sortedUtterancesList = sPUr(udcm)
            case _:
                print('uhhhhH just using set idk man')
                sortedUtterancesList = sPUs(udcm, scores)
        
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