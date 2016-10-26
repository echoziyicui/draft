#!/usr/bin/env python3
################################################################################
#
# program: integrateData.py
# Author:  (Echo) Ziyi Cui
# version: Version 1.7
# Date:    26/10/2016
#
# Function:
# ---------
#.
#
# Usage:
# ------
# integrateData.py + RL.faa -> integratedData.txt
#
################################################################################
# import
import sys

################################################################################
# constant


abNoSeq      = []
abWithSeq    = []
seqDict      = {}

RabNoSeq     = []
RabWithSeq   = []
RseqDict     = {}

PabNoSeq     = []
PabWithSeq   = []
PseqDict     = {}

warningList  = []

integratedSeqInfo = {}

SeqInfo = {}

allInOne            = []

chain_appearance    = {}
pairChain           = []
onlyHeavy           = []
onlyLight           = []
multiPair           = {}
pairWithFusion      = {}
multiPairWithFusion = {}

formatData = ''
################################################################################
# UsageDie()
# ----------
# provide general information about the whole process.
#
# 20.10.16 Original version By: Echo
def UsageDie():

    print("""
    version:   1.5
    Usage:     integrateData.py + RL.faa + PL.faa + RLimagedSeq.faa +
    PL115imagedSeq.faa-> integratedData.txt
    Function:  integrate antibody sequence data from Proposed list(PL.faa and PL115
    imagedSeq.faa) and Recommended list(RL.faa and RLimagedSeq.faa).
    Date:      20.10.2016""")
    sys.exit()

################################################################################
# testOpen()
# ---------
# test whether the file can be opened
#
# 20.10.16 Original version By: Echo

def testOpen(filePath):
    try:
        open(filePath, "r")
    except:
        print("Unable to open file " + filepPth)
        sys.exit()
    return 1

################################################################################
### Function 1
#
# 26.10.16
#
# 1.2 version By:(Echo) Ziyi Cui
#
# add_key() --> SeqInfo = {antibodyName | Heavy/light :[]}
#----------------------------------------------------------
# extract antibodyName as the key of a new dict.


def add_key(InputFileHandle):

    antibodyData = open(InputFileHandle, "r")
    abNoSeq = []
    abWithSeq = []
    seqDict = {}

    for line in antibodyData.readlines():
        if line[0] == '>' in line:
            antibodyKey = line.replace('>', '').rstrip()
            seqDict.setdefault(antibodyKey, '')

            if '- no sequence' in antibodyKey:
                field = antibodyKey.split(' - ')
                antibodyName = field[0]
                abNoSeq.append(antibodyName)
            else:
                field = antibodyKey.split('|')
                antibodyName = field[0]
                abWithSeq.append(antibodyName)
    if InputFileHandle   == sys.argv[1]:
         RabNoSeq         = abNoSeq
         RabWithSeq       = abWithSeq
         RseqDict         = seqDict
    elif InputFileHandle == sys.argv[2]:
         PabNoSeq         = abNoSeq
         #PabWithSeq      = abWithSeq
         #seqDict         = seqDict



    antibodyData.close()


################################################################################
### Function 2
#
# 26.10.16
#
# 1.2 version By:(Echo) Ziyi Cui
#
# SeqInfo = {antibodyName | Heavy/light :[sequence]}
# ----------------------------------------------------------
# add the corresponding sequence of antibody

def add_seq(InputFileHandle):
        antibodyData      = open(InputFileHandle, 'r')
        isReadingSequence = False
        antibodyKey       = ''
        sequence          = ''

        for line in antibodyData.readlines():
            if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
                isReadingSequence = False

                if antibodyKey in integratedSeqInfo:
                    if InputFileHandle == sys.argv[1]:
                        RseqDict[antibodyKey] = sequence
                    else:
                        PseqDict[antibodyKey] = sequence
                    sequence = ''

            if isReadingSequence:
                sequence += line

            if line[0] == '>':
                if '- no sequence' in line:
                    isReadingSequence = False
                    continue
                else:
                    isReadingSequence = True
                    antibodyKey = line.replace('>', '').rstrip()

        antibodyData.close()

################################################################################
### Function 3
#
# 26.10.16
#
# 1.3 version By:(Echo) Ziyi Cui
#
# add those sequences that manually converted from the images to integratedSeqInfo
#

def add_imagedSeq(InputFileHandle):

    imagedSeq       = open(InputFileHandle, 'r')
    isReadingSequence = False
    i_sequence        = ''

    for line in imagedSeq.readlines():

        if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
            isReadingSequence = False
            field = antibodyKey.split('|')
            antibodyName = field[0]

            if InputFileHandle == sys.argv[3]:
                RseqDict.setdefault(antibodyKey,'')
                RseqDict[antibodyKey] = i_sequence

                if (antibodyName + ' - no sequence') in RseqDict:
                    RseqDict.pop(antibodyName + ' - no sequence')
                    RabNoSeq.remove(antibodyName)
                if antibodyName not in RabWithSeq:
                    RabWithSeq.append(antibodyName)
            else:
                PseqDict.setdefault(antibodyKey, '')
                PseqDict[antibodyKey] = i_sequence

                if (antibodyName + ' - no sequence') in PseqDict:
                    PseqDict.pop(antibodyName + ' - no sequence')
                    PabNoSeq.remove(antibodyName)
                if antibodyName not in PabWithSeq:
                    PabWithSeq.append(antibodyName)

            i_sequence = ''

        if isReadingSequence:
                i_sequence += line

        if line[0] == ">":
            if "- no sequence" in line:
                isReadingSequence = False
                continue
            else:
                isReadingSequence = True
                antibodyKey       = line.replace(">", "").rstrip()

    imagedSeq.close()

################################################################################
### Function 4
#
# 26.10.16
#
# 1.3 version By:(Echo) Ziyi Cui
#
# integratedSeqInfo = {antibodyName | Heavy/light :[sequence]}
# add the corresponding sequence of antibody


def integrate_dicts():

    for antibodyKey in PseqDict:
        if antibodyKey in RseqDict:
            if RseqDict[antibodyKey] != PseqDict[antibodyKey]:
                warningList.append(antibodyKey)

        elif ' - no sequence' in antibodyKey:
            field = antibodyKey.split(' - ')
            antibodyName = field[0]
            if antibodyName not in RabWithSeq:
                RseqDict.setdefault(antibodyKey, '')

        else:
            field        = antibodyKey.split('|')
            antibodyName = field[0]
            RseqDict.setdefault(antibodyKey, PseqDict[antibodyKey])
            if antibodyName not in RabWithSeq:
                RabWithSeq.append(antibodyName)
            if (antibodyName + ' - no sequence') in RseqDict:
                RseqDict.pop(antibodyName + ' - no sequence')
                RabNoSeq.remove(antibodyName)

    integratedSeqInfo = RseqDict
    abNoSeq           = RabNoSeq
    abWithSeq         = RabWithSeq

    #print(integratedSeqInfo)
    #print('abWithSeq =', abWithSeq)

################################################################################
### Function 5
#
# 26.10.16
#
# 1.3 version By:(Echo) Ziyi Cui
#
# sort integratedSeqInfo according to chainType


def sort_seq():

    for key in integratedSeqInfo:
        if ' - no sequence' in key:
            pass
        elif ('-' in key) and ('|' in key):
            field = key.split('|')
            allInOne.append(field[0])

        else:
            field = key.split('|')
            antibodyName = field[0]
            if len(field) == 2:
                chainType = field[-1]
                chain_appearance.setdefault(antibodyName, [])
                chain_appearance[antibodyName].append(chainType)
            else:  # case when len(field) = 3
                chainType = field[1] + field[2]
                chain_appearance.setdefault(antibodyName, [])
                chain_appearance[antibodyName].append(chainType)


    #print(chain_appearance['citatuzumab bogatox']) #bug


    for antibodyName in chain_appearance:
        if chain_appearance[antibodyName] == ['Heavy', 'Light'] \
          or chain_appearance[antibodyName] == ['Light', 'Heavy']:
            pairChain.append(antibodyName)
        elif chain_appearance[antibodyName] ==['Heavy']:
            onlyHeavy.append(antibodyName)
        elif chain_appearance[antibodyName] == ['Light']:
            onlyLight.append(antibodyName)
        elif 'Heavy2' or 'Light2' in chain_appearance[antibodyName]:
            multiPair.setdefault(antibodyName, chain_appearance[antibodyName])

        else:
            if len(chain_appearance[antibodyName]) == 2:
                pairWithFusion.setdefault(antibodyName, chain_appearance[antibodyName])
            else:
                multiPairWithFusion.setdefault(antibodyName, chain_appearance[antibodyName])

    print('abnoSeq = ', abNoSeq)
    print('multiPair=', multiPair)
    print('pairWithFusion=',pairWithFusion)
    print('multiPairWithFusion',multiPairWithFusion)

################################################################################
### Function 6
#
# 26.10.16
#
# 1.4 version By:(Echo) Ziyi Cui
#
# format_data() --> string printed out
# format the integrated data and put it into a file.
#
# Usage:
# ------
# integrateData.py -> stdout(print)


def format_data():

    for key in integratedSeqInfo:
        if ' - no sequence' in key:
            formatData += '>' + key + '\n\n'

        else:
            field = key.split('|')
            antibodyName = field[0]
            chainType = field[1]
            correspondingH = antibodyName + '|Heavy'
            correspondingL = antibodyName + '|Light'
            correspondingH2 = antibodyName + '|Heavy2'
            correspondingL2 = antibodyName + '|Light2'

            if antibodyName in pairChain and chainType == 'Heavy':
                formatData += '>' + key + '\n' + integratedSeqInfo[key] + \
                              '>' + correspondingL + '\n' + integratedSeqInfo[correspondingL] + '\n\n'

            elif antibodyName in pairWithFusion and chainType == 'Heavy':
                formatData += '>' + key + '\n' + integratedSeqInfo[key] + '\n'
                if correspondingL in integratedSeqInfo:
                    formatData += '>' + correspondingL + '\n' + integratedSeqInfo[correspondingL] + '\n\n'
                else:
                    fusedL = correspondingL + '|Fusion'
                    formatData += '>' + fusedL + 'n' + integratedSeqInfo[fusedL] + '\n\n'

            elif (antibodyName in multiPair) and (chainType == 'Heavy'):
                formatData += '>' + key + '\n' + integratedSeqInfo[key] + '\n'
                if correspondingL in integratedSeqInfo:
                    formatData += '>' + correspondingL + '\n' + integratedSeqInfo[correspondingL] + '\n\n'

                if correspondingH2 in integratedSeqInfo:
                    formatData += '>' + correspondingH2 + '\n' + integratedSeqInfo[correspondingH2] + '\n'
                else:
                    formatData += '>' + key + '\n' + integratedSeqInfo[key] + '\n'

                if correspondingL2 in integratedSeqInfo:
                    formatData += '>' + correspondingL2 + '\n' + integratedSeqInfo[correspondingL2] + '\n\n'
                else:
                    formatData += '>' + correspondingL + '\n' + integratedSeqInfo[correspondingL] + '\n\n'

            elif antibodyName in multiPairWithFusion:
                    if chainType == 'Heavy2':
                        formatData = '>' + correspondingH + integratedSeqInfo[correspondingH] + '\n' + \
                                     '>' + correspondingL + integratedSeqInfo[correspondingL] + '\n\n' + \
                                     '>' + key + '\n' + integratedSeqInfo[key] + '\n' + \
                                     '>' + correspondingL + integratedSeqInfo[correspondingL] + '\n\n'
                    elif chainType == 'Light2':
                        formatData = '>' + correspondingH + integratedSeqInfo[correspondingH] + '\n' + \
                                     '>' + correspondingL + integratedSeqInfo[correspondingL] + '\n\n' + \
                                     '>' + correspondingH + integratedSeqInfo[correspondingH] + '\n' + \
                                     '>' + key + '\n' + integratedSeqInfo[key] + '\n\n'

            else:  # case when (antibodyName in allInOne) or (antibodyName in  onlyHeavy) or (antibodyName in onlyLight)
                formatData += '>' + key + '\n' + integratedSeqInfo[key] + '\n\n'

################################################################################
### main program
#
# 26.10.16 Original version By: Echo
#
# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()

testOpen(sys.argv[1])
testOpen(sys.argv[2])
testOpen(sys.argv[3])
testOpen(sys.argv[4])

add_key(sys.argv[1])
add_seq(sys.argv[1])
add_imagedSeq(sys.argv[3])
add_key(sys.argv[2])
add_seq(sys.argv[2])
add_imagedSeq(sys.argv[4])
integrate_dicts()
sort_seq()
format_data()
print(formatData)




