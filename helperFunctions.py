
# takes in a dictionary and a key, increments the value of that key by 1
# this is safer and quicker than doing it in real time
# note the restraint I showed by not using try/except
def dictionaryIncrement(dictionary, key):
    existingKeys = dictionary.keys()
    if (key in existingKeys) :
        dictionary[key] += 1
    else:
        dictionary[key] = 1


# Takes in two dictionaries and a set, returns a sorted list of ('utterance', score) tuples
# First dictionary is nested, and goes utterance -> diphone -> count 
# Second dictionary is diphone -> score
# Does so in a way that completely ignores number of instances of each phone in an utterance, only cares about existence, hence "set"
# Low score means rarer mix of units
def scorePossibleUtterancesSet(udcm, unitScores):
    uttScoresList = []
    for utterance in udcm.keys():
        utteranceScore = 0
        for diphone in udcm[utterance].keys(): # we're only iterating over this key set because we dont super care about number of instances
            if diphone == 'total': continue
            utteranceScore += unitScores[diphone]
        uttScoresList.append((utterance, utteranceScore * udcm[utterance]['total'])) # normalize by number of phones, higher score bad yes
    
    return sorted(uttScoresList, key=lambda x: x[1])

# Takes in two dictionaries, returns a sorted list of ('utterance', score) tuples
# First dictionary is nested, and goes utterance -> diphone -> count 
# Second dictionary is diphone -> score
# Does so in a way that cares about number of instances of each phone in an utterance, hence "mult"
# Low score means rarer mix of units
def scorePossibleUtterancesMult(udcm, unitScores):
    uttScoresList = []
    for utterance in udcm.keys():
        utteranceScore = 0
        for diphone in udcm[utterance].keys():
            if diphone == 'total': continue
            utteranceScore += unitScores[diphone] * udcm[utterance][diphone]
        uttScoresList.append((utterance, utteranceScore * udcm[utterance]['total'])) # normalize by number of phones
    
    return sorted(uttScoresList, key=lambda x: x[1])

# TODO implement a sPU variant that keeps track of which units we dont have yet and which we already have. lol.

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