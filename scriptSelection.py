from helperFunctions import dictionaryIncrement as dI
from helperFunctions import scorePossibleUtterancesSet as sPUs
from helperFunctions import scorePossibleUtterancesMult as sPUm
from helperFunctions import scorePossibleUtterancesAware as sPUa
from helperFunctions import createUnitScoresProportional as cUS

udcm = {} # utterance diphone counts map, it maps utterance key strings to maps that map diphones to their counts within the utterance
currentUtt = 'init' # e.g. 00000, 00001, etc...
utteranceCounter = 0 # counts the number of diphones in an utterance so we can normalize for that!
currentDiphoneCounts = {} # stores number of diphone type within the current utterance in pairs e.g. ('sil_p', 3) 
overallDiphoneCounts = {} # same as above but continues for every single diphone over all utterances
prevPhone = 'sil'
currentPhone = ''
diphone = ''

fil = open('simonH.txt')
for line in fil:

    # When we hit a new utterance, reset for the next one:
    if '!MLF!' in line:
        # in this case we haven't done anything yet, so we just wanna pass through
        if currentUtt != 'init':
            # double check if this utterance actually has any utterances, and don't do anything if it doesn't!
            if (utteranceCounter == 0): continue

            # store the total number of diphones in the utterance
            currentDiphoneCounts['total'] = utteranceCounter

            # store the current diphone counts map where it should go in the udcm
            newPair = {currentUtt : currentDiphoneCounts.copy()}
            udcm.update(newPair)
            # reset the currentDiphoneCounts map
            currentDiphoneCounts = {}
        continue
    
    # Set the current utterance number
    if '.lab' in line:
        currentUtt = line[14:19]
        utteranceCounter = 0
        continue

    # We don't want to care about both the closures and the releases in the case of diphones
    # Nor do we really want to care about short pauses, nor the random period at the end
    if '_cl' in line or 'sp' in line or '.' in line:
        continue

    # if it's not one of those edge cases, we add the diphone to all of the various dictionaries and count it
    currentPhone = line[:-1]
    diphone = f'{prevPhone}_{currentPhone}'
    if diphone == 'sil_sil': continue # we don't actually care about sil_sil
    dI(currentDiphoneCounts, diphone)
    dI(overallDiphoneCounts, diphone)
    prevPhone = currentPhone
    utteranceCounter += 1
# end loop
fil.close()

# store a set of all the diphones so that we can terminate once we have all of them, if we want!
diphoneSet = set(overallDiphoneCounts.copy().keys())

# store a copy of ucdm for evaluation later :)
udcmCOPY = udcm.copy()

# print(udcm)
# print(overallDiphoneCounts)
# print(udcm['00222'])

# so now overallDiphoneCounts can act as our scores dictionary because big scores are bad and little score are good

# After that we'll greedily select the best one, by adding up the scores of all the utterances and normalizing by length of utterance

# These lines test the difference between the two methods of scoring utteranceScore
# in sPUs, we only add the score of each diphone once, whereas in sPUm we add the score of each diphone once PER instance
# in both we normalize by number of diphones in the utterance!
# HYPOTHESIS: coverage is better in sPUs rather than sPUm, because sPUm rewards redundancy rather than punishing it!
# 
# print(sPUs(udcm, overallDiphoneCounts)[12:30])
# print(sPUm(udcm, overallDiphoneCounts)[12:30])

utterancesInOrder = []
# while (len(utterancesInOrder) < 22):
# while (len(diphoneSet) != 0):
while (len(udcm) != 0):
    # sortedUtterancesList = sPUs(udcm, cUS(overallDiphoneCounts))
    # sortedUtterancesList = sPUm(udcm, cUS(overallDiphoneCounts))
    # sortedUtterancesList = sPUa(udcm, cUS(overallDiphoneCounts), diphoneSet)
    
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

print(utterancesInOrder)