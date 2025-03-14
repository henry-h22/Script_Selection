import matplotlib.pyplot as plt
from helperFunctions import dictionaryIncrement as dI

def evaluateUtterance(utteranceList, udcm, overallDiphoneCounts, subplotThing = None):

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
            rawDiphonesList.append(hash(diphone))

    if subplotThing is not None:
        subplotThing.ecdf(rawDiphonesList)
    else:
        fig, ax = plt.subplots()
        # ax.hist(rawDiphonesList, bins = len(utterranceDiphoneCounts.keys()), linewidth = 0.022)
        ax.ecdf(rawDiphonesList)
        plt.show()

    # return utterranceDiphoneCounts


def visuallyEvaluateUtterances(utteranceListList, udcm, overallDiphoneCounts):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex=True, sharey=True)
    
    evaluateUtterance(utteranceListList[0], udcm.copy(), overallDiphoneCounts.copy(), ax1)
    evaluateUtterance(utteranceListList[1], udcm.copy(), overallDiphoneCounts.copy(), ax2)
    evaluateUtterance(utteranceListList[2], udcm.copy(), overallDiphoneCounts.copy(), ax3)
    evaluateUtterance(utteranceListList[3], udcm.copy(), overallDiphoneCounts.copy(), ax4)

    plt.show()
    