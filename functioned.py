#!/usr/bin/env python3
################################################################################
#
# program: integrateData.py
# Author:  (Echo) Ziyi Cui
# version: Version 1.5
# Date:    20/10/2016
#
# Function:
# ---------
# 1.From the file with antibody sequence, collect the appearance of heavy chain,
# light chain, or Fused chain.
# 2.Then sort them to different groups according to this appearance.
# 3.Extract sequence data from RL and add them to a new dict: antibodyName as key; sequence as value
# 4.add those antibodies that are only in PL.faa
# 5.add sequences manually converted from images.
# 6.write the final integrated results in to a file.
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

integratedSeqInfo = {}
antibodyInRL = []
antibodyNoSeqInRL = []
pendingList =[]
chain_appearance = {}
noSeq = []
allInOne = []
pairChain = []
onlyHeavy =[]
onlyLight = []
pairWithFusion = []
multiPair = []
multiPairWithFusion = []

warningList       = []
antibodyInPLOnly  = []

################################################################################
# UsageDie()
# ----------
# provide general information about the whole process.
#
# 20.10.16 Original version By: Echo
def UsageDie():
    print("""
    version:   1.5
    Usage:     integrateData.py + RL.faa + PL.faa + RLandPL115imagedSeq.faa -> integratedData.txt
    Function:  add those antibodies that only occur in PL.faa and RLandPL115imagedSeq.faa into
               RL.faa, resulting in a integrated data of antibody sequence.
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
# 20.10.16
#
# 1.1 version By:(Echo) Ziyi Cui
#
# add_key() --> integratedSeqInfo = {antibodyName | Heavy/light :[]}
# build a new dictionary named as integratedSeqInfo, use the antibodyName as the
# key
#
# Usage:
# ------
# integrateData.py + RL.faa -> stdout(print)




def add_key():
    antibodyInRL = []
    rl = open(sys.argv[1], "r")
    for line in rl.readlines():
        if line[0] == ">" in line:
            key = line.replace(">", "").rstrip()
            integratedSeqInfo.setdefault(key, "")
            if '- no sequence ' in key:
                field = key.split(' - ')
                antibodyName = field[0]
                antibodyNoSeqInRL.append(antibodyName)
            else:
                field = key.split('|')
                antibodyName = field[0]
                antibodyInRL.append(antibodyName) # only contain those antibody names with sequences.
    #print('1:', integratedSeqInfo )
    rl.close()

################################################################################
### Function 2
#
# 20.10.16
#
# 1.2 version By:(Echo) Ziyi Cui
#
# integratedSeqInfo = {antibodyName | Heavy/light :[sequence]}
# add the corresponding sequence of antibody
# Usage:
# ------
# integrateData.py + RL.faa -> stdout(print)


def add_seq():
        rl = open(sys.argv[1], "r")
        isReadingSequence = False
        antibodyKey       = ""
        r_sequence        = ""

        for line in rl.readlines():
            if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
                isReadingSequence = False

                if antibodyKey in integratedSeqInfo:
                    integratedSeqInfo[antibodyKey] = r_sequence
                    r_sequence = ""

            if isReadingSequence:
                r_sequence += line

            if line[0] == ">":
                if "- no sequence" in line:
                    isReadingSequence = False
                    continue
                else:
                    isReadingSequence = True
                    antibodyKey = line.replace(">", "").rstrip()

        rl.close()

################################################################################
### Function 3
#
# 21.10.16
#
# 1.2 version By:(Echo) Ziyi Cui
#
# integratedSeqInfo = {antibodyName | Heavy/light :[sequence]}
# check the PL.daa with integratedseqInfo.
# 1.For the same antibody, if sequence in PL.faa is different from that in
# integratedInfo constructed from RL.faa, then add to a warning list and retain
# the sequence in integratedseqInfo.
# 2.If antibody from PL.faa is not already in integratedseqInfo, then add its
# sequence into integratedseqInfo.
# 3.If antibody from PL.faa is in integratedseqInfo and the sequences from two
# source are the same, then pass.
#
# Usage:
# ------
# integrateData.py + PL.faa -> stdout(print)


def check_pl():
    pl          = open(sys.argv[2], "r")
    isReadingSequence = False
    antibodyKey       = ""
    p_sequence        = ""

    for line in pl.readlines():

        if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
            isReadingSequence = False

            if antibodyKey in integratedSeqInfo:
                if integratedSeqInfo[antibodyKey] == p_sequence:
                    pass
                elif antibodyKey not in warningList:
                    warningList.append(antibodyKey)

                #elif antibodyKey == 'otlertuzumab|Heavy':
                    #pass
            else:
                integratedSeqInfo.setdefault(antibodyKey, "")
                integratedSeqInfo[antibodyKey] = p_sequence

                if (antibodyName + ' - no sequence') in integratedSeqInfo:
                    integratedSeqInfo.pop(antibodyName + ' - no sequence')
                    pendingList.append(antibodyName)
                else:
                    antibodyInPLOnly.append(antibodyKey)

            p_sequence            = ""


        if isReadingSequence:
            p_sequence       += line

        if line[0] == ">":
            if "- no sequence" in line:
                isReadingSequence = False
                antibodyKey = line.replace(">", "").rstrip()
                field = antibodyKey.split(" - ")
                antibodyName = field[0]

                if antibodyKey in integratedSeqInfo: # In R'mab - no seq' already in integratedSeqInfo
                    pass
                elif antibodyName in antibodyInRL: # In R: mab|Heavy; mab|Light
                    pass
                else:
                    integratedSeqInfo.setdefault(antibodyKey, "")
                continue

            else:
                isReadingSequence = True
                antibodyKey = line.replace(">", "").rstrip()

    #print('warningList=', warningList)
    pl.close()

#print("main program 4 result:")
#print("integratedSeqInfo=", integratedSeqInfo)
#print(len(integratedSeqInfo))
#print("warningList=", warningList)
#print(len(warningList))
#print("antibodyInPLOnly=", antibodyInPLOnly)
#print(len(antibodyInPLOnly))
#print("\n")

################################################################################
### Function 4
#
# 25.10.16
#
# 1.2 version By:(Echo) Ziyi Cui
#
# add those sequences that manually converted from the images to integratedSeqInfo
#
# Usage:
# ------
# integrateData.py + imagedSeqR.faa + imagedSeqP.faa -> stdout(print)

def add_imagedSeqR():

    imagedSeqR       = open(sys.argv[3], "r")
    imagedSeqP       = open(sys.argv[4], "r")

    isReadingSequence = False
    ir_sequence        = ""
    ip_sequence       =""
    seqImagedOnly     = []

    for line in imagedSeqR.readlines():

        if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
            isReadingSequence = False
            field = antibodyKey.split('|')
            antibodyName = field[0]

            if antibodyKey in integratedSeqInfo:
                if integratedSeqInfo[antibodyKey] != ir_sequence:
                    integratedSeqInfo[antibodyKey] = ir_sequence
                    warningList.append(antibodyKey)
                else:
                    pass

            elif (antibodyName + ' - no sequence') in integratedSeqInfo:

                if antibodyKey in imagedSeqP:
                    isReadingSequence = False

                    for line in imagedSeqP.readlines():
                        if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
                            isReadingSequence = False

                            if ir_sequence != ip_sequence:
                                warningList.append(antibodyKey)
                            ip_sequence = ""

                        if isReadingSequence:
                            ip_sequence += line

                        if line[0] == (">" + antibodyKey):
                            isReadingSequence = True

                integratedSeqInfo.pop(antibodyName + ' - no sequence')
                seqImagedOnly.append(antibodyKey)

            integratedSeqInfo.setdefault(antibodyKey, "")
            integratedSeqInfo[antibodyKey] = ir_sequence
            ir_sequence = ""

        if isReadingSequence:
                ir_sequence += line

        if line[0] == ">":
            if "- no sequence" in line:
                isReadingSequence = False
                continue
            else:
                isReadingSequence = True
                antibodyKey       = line.replace(">", "").rstrip()

    imagedSeqR.close()
    imagedSeqP.close()

################################################################################
### Function 5
#
# 25.10.16
#
# 1.0 version By:(Echo) Ziyi Cui
#
# add imaged sequence from PL

def add_imagedSeqP():

    imagedSeqP = open(sys.argv[4], "r")
    isReadingSequence = False
    ip_sequence = ""
    for line in imagedSeqP.readlines():

        if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
            isReadingSequence = False
            field = antibodyKey.split('|')
            antibodyName = field[0]

            if antibodyKey in integratedSeqInfo:
                if integratedSeqInfo[antibodyKey] != ip_sequence:
                    warningList.append(antibodykey)

            elif (antibodyName + ' - sequence') in integratedSeqInfo:
                integratedSeqInfo.setdefault(antibodyKey, "")
                integratedSeqInfo[antibodyKey] = ip_sequence
                seqImagedOnly.append(antibodyKey)
                integratedSeqInfo.pop(antibodyName + ' - no sequence')
            ip_sequence = ""

        if isReadingSequence:
            ip_sequence += line

        if line[0] == ">":
            if "- no sequence" in line:
                isReadingSequence = False
                continue
            else:
                isReadingSequence = True
                antibodyKey = line.replace(">", "").rstrip()

    imagedSeqP.close()


#print("main program 5 result:")
#print("integratedSeqInfo=", integratedSeqInfo)
#print(len(integratedSeqInfo))
#print("seqImagedOnly=", seqImagedOnly)
#print(len(seqImagedOnly))
#print("\n")

################################################################################
### Function 6
#
# 24.10.16
#
# 1.2 version By:(Echo) Ziyi Cui
#
# sort integratedSeqInfo according to chainType


def sort_seq():

    for key in integratedSeqInfo:
        if '- no sequence' in key:
            field = key.split('-')
            noSeq.append(field[0])
        elif ('-' in key) and ('|' in key):
            field = key.split('|')
            allInOne.append(field[0])

        else:
            field = key.split('|')
            if len(field) == 2:
                antibodyName = field[0]
                chainType = field[-1]
                chain_appearance.setdefault(antibodyName, [])
                chain_appearance[antibodyName].append(chainType)
            else:    #case when len(field) = 3
                antibodyName =field[0]
                chainType =  field[1] + field [2]
                chain_appearance.setdefault(antibodyName, [])
                chain_appearance[antibodyName].append(chainType)


    print(noSeq) #bug
    print(chain_appearance['citatuzumab bogatox']) #bug


    for antibodyName in chain_appearance:
        if chain_appearance[antibodyName] == ['Heavy', 'Light'] \
          or chain_appearance[antibodyName] == ['Light' , 'Heavy'] :
            pairChain.append(antibodyName)
        elif chain_appearance[antibodyName] ==['Heavy']:
            onlyHeavy.append(antibodyName)
        elif chain_appearance[antibodyName] == ['Light']:
            onlyLight.append(antibodyName)
        elif 'Heavy2' or 'Light2' in chain_appearance[antibodyName]:
            multiPair.append(antibodyName)

        else:
            if len(chain_appearance[antibodyName]) == 2:
                pairWithFusion.append(antibodyName)
            else:
                multiPairWithFusion.append(antibodyName)

    print('multiPair=', multiPair)

################################################################################
### Function 6
#
# 24.10.16
#
# 1.3 version By:(Echo) Ziyi Cui
#
# format_data() --> string printed out
# format the integrated data and put it into a file.
#
# Usage:
# ------
# integrateData.py -> stdout(print)


def format_data():

    formatData = ''

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
# 24.10.16 Original version By: Echo
#
# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()

testOpen(sys.argv[1])
testOpen(sys.argv[2])
testOpen(sys.argv[3])
testOpen(sys.argv[4])

add_key()
add_seq()
check_pl()
add_imagedSeqR()
add_imagedSeqP()
sort_seq()
format_data()

print('noSeq=', noSeq)
print('allInOne=', allInOne)
print('pairChain=', pairChain)
print('onlyHeavy=', onlyHeavy)
print('onlyLight=', onlyLight)
print('multiPair=', multiPair)
print('pairWithFusion=', pairWithFusion)
print('multiPairWithFusion=', multiPairWithFusion)

#print(formatData)


