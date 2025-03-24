from helperFunctions import dictionaryIncrement as dI

# Take in a the filename, return a tuple of (utterance diphone counts map, overall diphones count map)
def readFilePhoneme(filename = 'simonH.txt', scriptNameLength = 10):
    upcm = {} # utterance PHONE counts map, it maps utterance key strings to maps that map diphones to their counts within the utterance
    currentUtt = 'init' # e.g. 00000, 00001, etc...
    utteranceCounter = 0 # counts the number of diphones in an utterance so we can normalize for that!
    currentPhoneCounts = {} # stores number of diphone type within the current utterance in pairs e.g. ('sil_p', 3) 
    overallPhoneCounts = {} # same as above but continues for every single diphone over all utterances
    prevPhone = 'sil'
    currentPhone = ''
    phone = ''

    fil = open(filename)
    for line in fil:

        # When we hit a new utterance, reset for the next one:
        if '!MLF!' in line:
            # in this case we haven't done anything yet, so we just wanna pass through
            if currentUtt != 'init':
                # double check if this utterance actually has any utterances, and don't do anything if it doesn't!
                if (utteranceCounter == 0): continue

                # store the total number of diphones in the utterance
                currentPhoneCounts['total'] = utteranceCounter

                # store the current diphone counts map where it should go in the udcm
                newPair = {currentUtt : currentPhoneCounts.copy()}
                upcm.update(newPair)
                # reset the currentDiphoneCounts map
                currentPhoneCounts = {}
            continue
        
        # Set the current utterance number
        if '.lab' in line:
            currentUtt = line[4 + scriptNameLength : 9 + scriptNameLength]
            utteranceCounter = 0
            continue

        # We don't want to care about both the closures and the releases in the case of diphones
        # Nor do we really want to care about short pauses, nor the random period at the end
        if '_cl' in line or 'sp' in line or '.' in line:
            continue

        # if it's not one of those edge cases, we add the diphone to all of the various dictionaries and count it
        phone = line[:-1]
        if phone == 'sil': continue # we don't actually care about sil_sil
        dI(currentPhoneCounts, phone)
        dI(overallPhoneCounts, phone)
        utteranceCounter += 1
    # end loop
    fil.close()


    # add the last one in (oops!!)

    # double check if this utterance actually has any utterances, and don't do anything if it doesn't!
    if (not(utteranceCounter == 0)):
        # store the total number of diphones in the utterance
        currentPhoneCounts['total'] = utteranceCounter

        # store the current diphone counts map where it should go in the udcm
        newPair = {currentUtt : currentPhoneCounts.copy()}
        upcm.update(newPair)

    fil.close()

    return (upcm, overallPhoneCounts)