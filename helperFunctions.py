import random
from datetime import datetime


# --==+==-- Selection Algorithms --==+==--

# Takes in two dictionaries and a set, returns a sorted list of ('utterance', score) tuples
# First dictionary is nested, and goes utterance -> diphone -> count 
# Second dictionary is diphone -> score
# Does so in a way that completely ignores number of instances of each phone in an utterance, only cares about existence, hence "set"
# High score means rarer mix of units
def scorePossibleUtterancesSet(udcm, unitScores):
    uttScoresList = []
    for utterance in udcm.keys():
        utteranceScore = 0
        for diphone in udcm[utterance].keys():
            if diphone == 'total': continue
            utteranceScore += unitScores[diphone]
        uttScoresList.append((utterance, utteranceScore / udcm[utterance]['total'])) # normalize by number of phones
    
    uttScoresList = sorted(uttScoresList, key=lambda x: x[1])
    uttScoresList.reverse()
    return uttScoresList


# Takes in two dictionaries, returns a sorted list of ('utterance', score) tuples
# First dictionary is nested, and goes utterance -> diphone -> count 
# Second dictionary is diphone -> score
# Does so in a way that cares about number of instances of each phone in an utterance, hence "mult"
# High score means rarer mix of units
def scorePossibleUtterancesMult(udcm, unitScores):
    uttScoresList = []
    for utterance in udcm.keys():
        utteranceScore = 0
        for diphone in udcm[utterance].keys():
            if diphone == 'total': continue
            utteranceScore += unitScores[diphone] * udcm[utterance][diphone] # as opposed to just adding it once :)
        uttScoresList.append((utterance, utteranceScore / udcm[utterance]['total'])) # normalize by number of phones
    
    uttScoresList = sorted(uttScoresList, key=lambda x: x[1])
    uttScoresList.reverse()
    return uttScoresList


def scorePossibleUtterancesAware(udcm, unitScores, diphonesNeededSet):
    # a sPU variant that keeps track of which units we dont have yet and which we already have. lol.
    # uses the Set logic cuz that makes sense to me. ONLY counting each instance of the thing ONCE yk?
    uttScoresList = []
    for utterance in udcm.keys():
        utteranceScore = 0
        for diphone in udcm[utterance].keys():
            if diphone == 'total': continue
            if diphone in diphonesNeededSet: # THIS is the crucial line :)
                utteranceScore += unitScores[diphone]
        uttScoresList.append((utterance, utteranceScore / udcm[utterance]['total'])) # normalize by number of phones
    
    uttScoresList = sorted(uttScoresList, key=lambda x: x[1])
    uttScoresList.reverse()
    return uttScoresList


def scorePossibleUtterancesRandom(udcm):
    # a sPU variant that does things randomly, to compare our methods and see if they do better lol
    tempList = list(udcm.keys())

    random.seed(datetime.now().timestamp())
    random.shuffle(tempList)

    uttScoresList = []

    for utt in tempList:
        uttScoresList.append((utt, 22))

    return uttScoresList


# --==+==-- Scoring Functions --==+==--


def createUnitScoresProportional(unitAmounts):
    # We want it to maximize instead of minimize so that we can divide by number of diphones and stuff,
    # and so that we punish redundancy in a more-straightforward way (just not counting repeats)
    newScores = {}

    # Get max value of any diphone
    maxVal = max(unitAmounts.values())

    # Then we set the score to just ((maxVal+1) - number of occurences) (the plus 1 is cuz no phone should have score 0)
    for diphone in unitAmounts.keys():
        newScores[diphone] = (maxVal+1) - unitAmounts[diphone]

    return newScores


def createUnitScoresLinear(unitAmounts):
    # there's some idea here where instead of retaining the zipf distribution in scores we like straighten that out

    if ('total' in unitAmounts.keys()):
        unitAmounts.pop('total')

    diphonesList = []
    for diphone in unitAmounts.keys():
        diphonesList.append((diphone, unitAmounts[diphone]))
    
    diphonesList = sorted(diphonesList, key=lambda x: x[1])
    diphonesList.reverse()
    
    scores = {}
    for score in range(len(diphonesList)):
        scores[diphonesList[score][0]] = score + 1 # again, we don't want any diphone to have a score of 0

    return scores


def createUnitScoresOnes(unitAmounts):
    # For this algorithm, we give every diphone a score of 1
    scores = {}
    for diphone in unitAmounts.keys():
        scores[diphone] = 1
    return scores


# --==+==-- Other Helper Functions --==+==--


# takes in a dictionary and a key, increments the value of that key by 1
# this is safer and quicker than doing it in real time
# note the restraint I showed by not using try/except
def dictionaryIncrement(dictionary, key, amount = 1):
    existingKeys = dictionary.keys()
    if (key in existingKeys) :
        dictionary[key] += amount
    else:
        dictionary[key] = amount


def dictionaryToSortedTuplesList(dictionary):
    # Function takes in a dictionary that maps keys to numerical values
    # Returns a list of key, value tuples sorted by value, lowest first
    tuplesList = []
    for key in dictionary.keys():
        tuplesList.append((key, dictionary[key]))
    return(sorted(tuplesList, key=lambda x: x[1]))


def resetNumberedUtts(filename = 'utts.data', scriptNameLength = 10):
    # Given the file name for an utts.data-esque file, reset the numbering system (great after manual pruning!)
    fileRead = open(filename, "r")
    currentLines = fileRead.readlines()
    fileRead.close()

    fileWrite = open(filename, "w")
    lineNum = 1
    newLines = []
    for line in currentLines:
        newLines.append(line[:(3+scriptNameLength)] + str(lineNum).zfill(5) + line[8+scriptNameLength:])
        lineNum += 1
    fileWrite.writelines(newLines)


if __name__ == '__main__':
    # resetNumberedUtts()
    resetNumberedUtts('allUttsRenumbered', 6)