import random
from datetime import datetime

# takes in a dictionary and a key, increments the value of that key by 1
# this is safer and quicker than doing it in real time
# note the restraint I showed by not using try/except
def dictionaryIncrement(dictionary, key, amount = 1):
    existingKeys = dictionary.keys()
    if (key in existingKeys) :
        dictionary[key] += amount
    else:
        dictionary[key] = amount

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
            utteranceScore += unitScores[diphone] * udcm[utterance][diphone]
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


def createUnitScoresProportional(unitAmounts):
    # We want it to maximize instead of minimize so that we can divide by number of diphones and stuff,
    # and so that we punish redundancy in a more-straightforward way (just not counting repeats)
    newScores = {}

    # Get max value of any diphone
    maxVal = max(unitAmounts.values())

    # Then we set the score to just (maxVal - number of occurences)
    for diphone in unitAmounts.keys():
        newScores[diphone] = maxVal - unitAmounts[diphone]

    return newScores

def createUnitScoresLinear():
    # there's some idea here where instead of retaining the zipf distribution in scores we like straighten that out
    pass


if __name__ == '__main__':
    u = {
        '00001' : {
            'dh_@' : 2,
            'ii_t' : 1,
            'total' : 3
        },
        '00002' : {
            'dh_@' : 9,
            'b_u' : 2,
            'j_uu' : 1,
            'total' : 12
        }
    }

    # random idc
    sc = {
        'dh_@' : 0.1,
        'ii_t' : 1,
        'b_u' : 0.5,
        'j_uu' : 0.001
    }

    # print(u)
    # print(u['00001']['total'])
    # print(sc)

    # TODO two design decisions:
        # do we count/score repeats. we wanna have them make an utterance less good, which leads us to...
        # do we minimize or maximize score? do we give rare units (diphones) a high or low score?
        # lets WRITE ABOUT THIS when we do it? or just take notes idrc.

    print(scorePossibleUtterancesSet(u, sc))