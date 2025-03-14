# Script that takes the settings we end up choosing and actually builds an utts.data file from that.

# The way I see it is we could pop around and index those lines, and then at the very end redo the numbering. :)

from readIn import readFile
from scriptSelection import scriptSelection

def readUttDataLines(filename = "simonHutts.data"):
    phil = open(filename)
    lines = []
    for line in phil:
        lines.append(line)
    return lines

udcm, overallDiphoneCounts = readFile('simonH.txt')

numberOfUtterances = 2000

chosenUtterances = scriptSelection(udcm.copy(), overallDiphoneCounts.copy(), 
                                    selectionFunction = 'aware', scoringFunction = 'linear', endConditionParameter=numberOfUtterances)

utteranceDataLines = readUttDataLines("simonHutts.data")

# What's interesting about this is that we want to choose a certain number of diphones, not utterances. So....
diphonesChosen = 0
diphoneThreshold = 10000000000
newDataLines = []

for i, utterance in enumerate(chosenUtterances):
    if diphonesChosen > diphoneThreshold: 
        print('Threshold reached!', diphonesChosen)
        break
    diphonesChosen += udcm[utterance]['total']
    newLine = utteranceDataLines[int(utterance)]
    newDataLines.append(newLine[:13] + str(i+1).zfill(5) + newLine[18:]) #! relies on script names being the same length as each other, and being 10 characters!

newFile = open("utts.data", "w")
newFile.writelines(newDataLines)
newFile.close()
