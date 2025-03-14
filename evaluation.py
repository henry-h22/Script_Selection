import matplotlib.pyplot as plt
from helperFunctions import dictionaryIncrement as dI
from helperFunctions import dictionaryToSortedTuplesList as sortDict

def evaluateUtterance(utteranceList, udcm, overallDiphoneCounts, subplotThing = None, scriptSelectionAlgorithm = '__', verbose = False):

    # Create our variables
    totalDiphoneSet = set(overallDiphoneCounts.copy().keys())
    selectedDiphonesSet = set([])
    utteranceDiphoneCounts = {}
    rawDiphonesList = []

    # Then we wanna create the data that we want to graph, which is a list of every diphone in the whole utterance list
    # As we do so, we keep track of number of diphone types that it could've grabbed but didn't, because that's also a metric!
    for utterance in utteranceList:
        for diphone in udcm[utterance].keys():
            selectedDiphonesSet.add(diphone) # we add the diphone to the set of selected units
            if diphone == 'total': continue
            dI(utteranceDiphoneCounts, diphone, udcm[utterance][diphone])

    diphoneCountsList = sortDict(utteranceDiphoneCounts)
    diphoneCountsList.reverse()

    for diphoneRank in range(len(diphoneCountsList)):
        diphone, count = diphoneCountsList[diphoneRank]
        if diphone == 'total': continue
        for _ in range(count):
            rawDiphonesList.append(diphoneRank) # we append the hashcode here because pyplot's ecdf function can't take strings

    missedDiphones = totalDiphoneSet - selectedDiphonesSet

    
    print('Script selection algorithm {} failed to select {} of {} possible diphones.'.format(scriptSelectionAlgorithm, len(missedDiphones), len(totalDiphoneSet)))
    print(len(missedDiphones)/len(totalDiphoneSet))
    if verbose:
        print('Those diphones that are missing are:\n')
        print(missedDiphones)
        print('Diphones and their counts:\n')
        print(diphoneCountsList)

    if subplotThing is not None:
        # in this case, we called the function from visuallyEvaluateUtterances, and we want to do something very specific
        subplotThing.set_title(scriptSelectionAlgorithm)
        # subplotThing.ecdf(rawDiphonesList)
        subplotThing.hist(rawDiphonesList, bins=len(overallDiphoneCounts.keys()), histtype = 'stepfilled')
    else:
        # here we just wanna plot it :)
        fig, ax = plt.subplots()
        # ax.hist(rawDiphonesList, bins = len(utteranceDiphoneCounts.keys()), linewidth = 0.022)
        ax.ecdf(rawDiphonesList)
        plt.show()

    # return utteranceDiphoneCounts


def visuallyEvaluateUtterances(utteranceListList, udcm, overallDiphoneCounts, selectionAlgorithms, verbose = False):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex=True, sharey=True)
    
    fig.suptitle('Diphone Distribution over Script Selection Algorithms')

    evaluateUtterance(utteranceListList[0], udcm.copy(), overallDiphoneCounts.copy(), ax1, selectionAlgorithms[0], verbose)
    evaluateUtterance(utteranceListList[1], udcm.copy(), overallDiphoneCounts.copy(), ax2, selectionAlgorithms[1], verbose)
    evaluateUtterance(utteranceListList[2], udcm.copy(), overallDiphoneCounts.copy(), ax3, selectionAlgorithms[2], verbose)
    evaluateUtterance(utteranceListList[3], udcm.copy(), overallDiphoneCounts.copy(), ax4, selectionAlgorithms[3], verbose)

    plt.show()
