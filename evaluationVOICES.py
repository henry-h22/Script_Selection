from readIn import readFile
from phonemeLevelInput import readFilePhoneme
from evaluationScoringFunctions import visuallyEvaluateUtterancesScoring as evalu

def getUtteranceListFromData(filename): # guys this is NOT reusable its gonna be so specific but dont even worry
    utteranceList = []
    fil = open(filename)
    for line in fil:
        if (line[2] == 'h'):
            strNum = int(line[14:19])
            breaks = [64, 135, 154, 214, 218]
            for b in breaks:
                if strNum > b:
                    strNum -= 1
            strNum += 400
            utteranceList.append(str(strNum).zfill(5))
        elif (line[2] == 'a'):
            utteranceList.append('0' + line[10:14])
    fil.close()
    return utteranceList


if __name__ == '__main__':
    upcm, overallPhoneCounts = readFilePhoneme('allUTTSRenumbered.mlf', scriptNameLength = 6)
    udcm, overallDiphoneCounts = readFile('allUTTSRenumbered.mlf', scriptNameLength = 6)
    arctic = getUtteranceListFromData('arcticOnly.data')
    combo = getUtteranceListFromData('combined.data')
    simon = [str(i).zfill(5) for i in range(401,651)] # lol
    blank = [str(i).zfill(5) for i in range(1,2)]

    
    utteranceListList = [arctic, combo, simon, blank]
    namesList = ['Arctic', 'Combo', 'Phoneticist', '']
    evalu(utteranceListList, upcm.copy(), overallPhoneCounts.copy(), namesList, verbose=True)
    evalu(utteranceListList, udcm.copy(), overallDiphoneCounts.copy(), namesList, verbose=True)
    