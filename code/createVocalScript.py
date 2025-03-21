# THIS FILE IS A COPY OF exportScript made specifically to collect the script for PARTICULAR voices
# A task that, honestly, I thought was gonna be easier. Oops.

from readIn import readFile
from scriptSelection import scriptSelectionHybrid as hssh

def readUttDataLines(filename = "simonHutts.data"):
    phil = open(filename)
    lines = []
    for line in phil:
        lines.append(line)
    return lines


def createIndividualVoiceDatabase(mlfFile = 'allUTTSRenumbered.mlf', diphoneThreshold = 222222, outputFilename = 'newnewnewutts.data'):
    udcm, overallDiphoneCounts = readFile(mlfFile, scriptNameLength = 6)

    numberOfUtterances = len(udcm.keys()) #! we want EVERY utterance chosen, thanks

    # Perform Hybrid: Set script selection with the Ones cost function, cuz of the result of the experiments
    chosenUtterances = hssh(udcm.copy(), overallDiphoneCounts.copy(), 
                            selectionFunction = 'set', scoringFunction = 'ones', endConditionParameter=numberOfUtterances)

    utteranceDataLines = readUttDataLines("allUTTS.data") #! note that this is NOT the renumbered one. we dont wanna confuse festival!

    # What's interesting about this is that we want to choose a certain number of diphones, not utterances. So....
    diphonesChosen = 0
    newDataLines = []

    for i, utterance in enumerate(chosenUtterances):
        if diphonesChosen > diphoneThreshold: 
            print('Threshold reached!', diphonesChosen)
            break
        diphonesChosen += udcm[utterance]['total']
        newLine = utteranceDataLines[int(utterance) - 1]
        newDataLines.append(newLine) # note that we don't renumber. IMPORTANT destinction from exportScript.py

    print(f'We chose {diphonesChosen} diphones!!')
    newFile = open(outputFilename, "w")
    newFile.writelines(newDataLines)
    newFile.close()

# if __name__ == '__main__':
#     createIndividualVoiceDatabase(mlfFile='arcticUTTS.mlf', outputFilename='zzzacrcitfun.data', diphoneThreshold=9990)
#     createIndividualVoiceDatabase(mlfFile='henrySimonUTTS.mlf', outputFilename='zzzhenrySimFun.data', diphoneThreshold=9990)
#     createIndividualVoiceDatabase(outputFilename='zzzCOmbined.data', diphoneThreshold=9990)