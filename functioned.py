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
chain_appearance = {}
noSeq = []
allInOne = []
pairChain = []
onlyHeavy =[]
onlyLight = []
pairWithFusion = []
multiPairWithFusion = []

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
    rl = open(sys.argv[1], "r")
    for line in rl.readlines():
        if line[0] == ">" and "|" in line:
            key = line.replace(">", "").rstrip()
            integratedSeqInfo.setdefault(key, "")
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

    warningList       = []
    antibodyInPLOnly  = []

    for line in pl.readlines():

        if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
            isReadingSequence = False

            if antibodyKey in integratedSeqInfo:
                if integratedSeqInfo[antibodyKey] != p_sequence:
                    if antibodyKey not in warningList:
                        warningList.append(antibodyKey)

                #elif antibodyKey == 'otlertuzumab|Heavy':
                    #pass
            else:
                integratedSeqInfo.setdefault(antibodyKey, "")
                integratedSeqInfo[antibodyKey] = p_sequence
                antibodyInPLOnly.append(antibodyKey)

            p_sequence            = ""

        if isReadingSequence:
            p_sequence       += line

        if line[0] == ">":
            if "- no sequence" in line:
                isReadingSequence = False
                continue
            else:
                isReadingSequence = True
                antibodyKey = line.replace(">", "").rstrip()

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
# 21.10.16
#
# 1.1 version By:(Echo) Ziyi Cui
#
# add those sequences that manually converted from the images to integratedSeqInfo
#
# Usage:
# ------
# integrateData.py + RLandPL115imagedSeq.faa -> stdout(print)

def add_imagedSeq():

    imagedSeq         = open(sys.argv[3], "r")
    isReadingSequence = False
    i_sequence        = ""
    seqImagedOnly     = []
    for line in imagedSeq.readlines():

        if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
            isReadingSequence = False

            integratedSeqInfo.setdefault(antibodyKey, "")
            integratedSeqInfo[antibodyKey] = i_sequence
            seqImagedOnly.append(antibodyKey)
            i_sequence = ""

        if isReadingSequence:
                i_sequence += line

        if line[0] == ">":
            if "-" in line:
                isReadingSequence = False
                continue
            else:
                isReadingSequence = True
                antibodyKey       = line.replace(">", "").rstrip()

    imagedSeq.close()

#print("main program 5 result:")
#print("integratedSeqInfo=", integratedSeqInfo)
#print(len(integratedSeqInfo))
#print("seqImagedOnly=", seqImagedOnly)
#print(len(seqImagedOnly))
#print("\n")

################################################################################
### Function 5
#
# 24.10.16
#
# 1.2 version By:(Echo) Ziyi Cui
#
# sort integratedSeqInfo according to chainType

def sort_seq():




    for key in integratedSeqInfo:
        if '-no sequence' in key:
            field = key.split('-')
            noSeq.append(field[0])
        elif ('-' in key ) and ('|' in key):
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


    for antibodyName in chain_appearance:
        if chain_appearance[antibodyName] == ['Heavy', 'Light'] \
            or chain_appearance[antibodyName] == ['Light' , 'Heavy'] :
            pairChain.append(antibodyName)
        elif chain_appearance[antibodyName] ==['Heavy']:
            onlyHeavy.append(antibodyName)
        elif chain_appearance[antibodyName] == ['Light']:
            onlyLight.append(antibodyName)

        else:
            if len(chain_appearance[antibodyName]) == 2:
                pairWithFusion.append(antibodyName)
            else:
                multiPairWithFusion.append(antibodyName)

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
        if '-no sequence' in key:
            formatData += '>' + key + '\n\n'

        else:
            field = key.split('|')
            antibodyName = field[0]
            chainType = field[1]
            correspondingH = antibodyName + '|Heavy'
            correspondingL = antibodyName + '|Light'

            if antibodyName in pairChain and chainType == 'Heavy':
                formatData += '>' + key + '\n' + integratedSeqInfo[key] + \
                              '>' + correspondingL + '\n' + integratedSeqInfo[correspondingL] + '\n\n'

            elif antibodyName in pairWithFusion and chainType == 'Heavy':
                formatData += '>' + key + '\n' + integratedSeqInfo[key] + '\n'
                if correspondingL in integratedSeqInfo:
                    formatData += '>' + correspondingL + '\n' + integratedSeqInfo[correspondingL] + '\n\n'
                else :
                    fusedL = correspondingL + '|Fusion'
                    formatData += '>' + fusedL + 'n' + integratedSeqInfo[fusedL] + '\n\n'

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

add_key()
add_seq()
check_pl()
add_imagedSeq()
sort_seq()
format_data()

print(noSeq)
print(allInOne)
print(pairChain)
print(onlyHeavy)
print(onlyLight)
print(pairWithFusion)
print(multiPairWithFusion)

# print(formatData


