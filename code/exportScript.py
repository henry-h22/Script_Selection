# Script that takes the settings we end up choosing and actually builds an utts.data file from that.

# The way I see it is we could pop around and index those lines, and then at the very end redo the numbering. :)

from readIn import readFile
from scriptSelection import scriptSelectionHybrid as hssh

def readUttDataLines(filename = "simonHutts.data"):
    phil = open(filename)
    lines = []
    for line in phil:
        lines.append(line)
    return lines


if __name__ == '__main__':
    
    udcm, overallDiphoneCounts = readFile('simonH.txt')

    numberOfUtterances = 700 #! because ARCTIC A chooses about 700 :)

    # Perform Hybrid: Set script selection with the Ones cost function, cuz of the result of the experiments
    chosenUtterances = hssh(udcm.copy(), overallDiphoneCounts.copy(), 
                            selectionFunction = 'set', scoringFunction = 'ones', endConditionParameter=numberOfUtterances)

    utteranceDataLines = readUttDataLines("simonHutts.data")

    # What's interesting about this is that we want to choose a certain number of diphones, not utterances. So....
    diphonesChosen = 0
    diphoneThreshold = 1000000000000000 # this is a tool we'll use when deciding what utterances to BUILD scripts with. different thing dont even worry
    newDataLines = []

    for i, utterance in enumerate(chosenUtterances):
        if diphonesChosen > diphoneThreshold: 
            print('Threshold reached!', diphonesChosen)
            break
        diphonesChosen += udcm[utterance]['total']
        newLine = utteranceDataLines[int(utterance) - 1]
        newDataLines.append(newLine[:13] + str(i+1).zfill(5) + newLine[18:]) #! relies on script names being the same length as each other, and being 10 characters!

    newFile = open("utts.data", "w")
    newFile.writelines(newDataLines)
    newFile.close()
