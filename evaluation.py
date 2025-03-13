import matplotlib.pyplot as plt
from helperFunctions import dictionaryIncrement as dI

def evaluateUtterance(utteranceList, udcm, overallDiphoneCounts):

    # Create our diphone set, for later
    diphoneSet = set(overallDiphoneCounts.copy().keys())

    # Create our diphones -> counts map for this SPECIFIC list of utterances
    utterranceDiphoneCounts = {}

    # Then we wanna create the data that we want to graph, starting with a diphone->count map over the whole list
    # As we do so, we keep track of number of diphones that it could've grabbed but didn't, because that's also a metric!
    for utterance in utteranceList:
        for diphone in udcm[utterance].keys():
            if diphone == 'total': continue
            dI(utterranceDiphoneCounts, diphone, udcm[utterance][diphone])
    

    rawDiphonesList = []
    for diphone in utterranceDiphoneCounts.keys():
        for _ in range(utterranceDiphoneCounts[diphone]):
            rawDiphonesList.append(diphone)

    fig, ax = plt.subplots()
    # ax.hist(rawDiphonesList, bins = len(utterranceDiphoneCounts.keys()), linewidth = 0.022)
    ax.ecdf(rawDiphonesList)
    plt.show()

    # return utterranceDiphoneCounts