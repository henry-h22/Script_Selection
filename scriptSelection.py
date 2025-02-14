# from sys import argv
from dictionaryIncrement import dictInc as dI

# TODO change this to in-real-time adding everything to a dictionary of lists for each utterance
# IDEALLY A LIST OF DIPHONES PLEASE !!!
# OOOOh and also keeping track of the most common diphones. That'd be good. Good luck !

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
    dI(currentDiphoneCounts, diphone)
    dI(overallDiphoneCounts, diphone)
    prevPhone = currentPhone
    utteranceCounter += 1

fil.close()

# print(udcm)
# print(overallDiphoneCounts)
print(udcm['00222'])
sortedDiCounts = dict(sorted(overallDiphoneCounts.items(), key=lambda item: item[1])).copy()
# print(sortedDiCounts)


#Sorted di counts gives us, essentially, the rarity scores and stuff
# probably divide all of those numbers by the max (2050) to get a score? Or do something w ordering? Idk I gotta watch that video

# After that we'll greedily select the best one, by adding up the scores of all the utterances and normalizing by length of utterance
# We're minimizing, (i.e. lower scores are better) so we SHOULD count repeat diphones in order to de-emphasize redundancy
# Then, crucially, we'll update the scores. How? Dunno exactly.
