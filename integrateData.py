#!/usr/bin/env python3
################################################################################
#
# program: integrateData.py
# Author:  (Echo) Ziyi Cui
# version: Version 1.2
# Date:    13/10/2016
#
# Function:
# ---------
# 1.From the file with antibody sequence, collect the appearance of heavy chain,
# light chain, or Fused chain.
# 2.Then sort them to different groups according to this appearance.
# 3.Extract sequence data from RL and add them to a new dict: antibodyName as key; sequence as value
#
# Usage:
# ------
# integrateData.py + RL.faa -> stdout(print)
#
################################################################################
import json
import sys

################################################################################
# constant about RL.faa
recommended                 = open(r'inndata\RL.faa', "r")
dict_recommended_appearance = {}
R_antibodyWithASetOfChain   = []
R_heavyChainAntibody        = []
R_lightChainAntibody        = []
R_twoVersionAntibody        = []
R_antibodyWithFusion        = []
R_specialAntibody           = {}

integratedSeqInfo = {}

currentSequence = ""

p_sequence = ""
warningList = []

antibodyWithASetOfChain   = []
heavyChainAntibody        = []
lightChainAntibody        = []
twoVersionAntibody        = []
antibodyWithFusion        = {}
specialAntibody           = {}

################################################################################
### main program 1
#
# 12.10.16
#
# 1.1 version By:(Echo) Ziyi Cui
#
# obtain all antibodyName in RL.faa and collect the information of their
# heavy/light chain appearance.
# Then sort them according to this appearance.
#
# Usage:
# ------
# integrateData.py + RL.faa -> stdout(print)

# add chain appearance info to each antibody.
for line in recommended.readlines():
    if line[0] == ">":
        line   = line.replace(">", "")  # delete the ">"
        line   = line.rstrip()

        if "|" in line:
            field        = line.split("|")
            antibodyName = field[0]
            chainType    = field[-1]
            dict_recommended_appearance.setdefault(antibodyName, [])

            if chainType   == "Heavy":
                dict_recommended_appearance[antibodyName].append('H')

            elif chainType == "Heavy2":
                dict_recommended_appearance[antibodyName].append('H2')

            elif chainType == "Light":
                dict_recommended_appearance[antibodyName].append('L')

            elif chainType == "Light2":
                dict_recommended_appearance[antibodyName].append('L2')

            elif chainType == "Fusion":
                dict_recommended_appearance[antibodyName].append('F')

#print('dict = ', dict_recommended_appearance)

# sort these antibodyNames into different groups, according to their chain appearance.
for antibodyName in dict_recommended_appearance:
    if dict_recommended_appearance[antibodyName]   == ['H', 'L']:
        R_antibodyWithASetOfChain.append(antibodyName)
    elif dict_recommended_appearance[antibodyName] == ['H']:
        R_heavyChainAntibody.append(antibodyName)
    elif dict_recommended_appearance[antibodyName] == ['L']:
        R_lightChainAntibody.append(antibodyName)
    elif 'H2' in dict_recommended_appearance[antibodyName] or 'L2' in dict_recommended_appearance[antibodyName]:
        R_twoVersionAntibody.append(antibodyName)
    elif 'F' in dict_recommended_appearance[antibodyName]:
        R_antibodyWithFusion.append(antibodyName)
    else:
        value = dict_recommended_appearance[antibodyName]
        R_specialAntibody.setdefault(antibodyName, value)

print("program 1 results: ")
print("R_antibodyWithASetOfChain=", R_antibodyWithASetOfChain)
print(len(R_antibodyWithASetOfChain))
print("R_heavyChainAntibody =", R_heavyChainAntibody)
print(len(R_heavyChainAntibody))
print("R_lightChainAntibody =", R_lightChainAntibody)
print(len(R_lightChainAntibody))
print("R_twoVersionAntibody=", R_twoVersionAntibody)
print(len(R_twoVersionAntibody))
print("R_antibodyWithFusion=", R_antibodyWithFusion)
print(len(R_antibodyWithASetOfChain))
print("R_specialAntibody =", R_specialAntibody)
print(len(R_specialAntibody))
print('\n')

################################################################################
### main program 2
#
# 12.10.16
#
# 1.0 version By:(Echo) Ziyi Cui
#
# integratedSeqInfo = {antibodyName | Heavy/light :[]}
# build a new dictionary named as integratedSeqInfo, use the antibodyName as the
# key.
#
# Usage:
# ------
# integrateData.py + RL.faa -> stdout(print)

################################################################################
recommended       = open(r'inndata\RL.faa', 'r')


for line in recommended.readlines():
    if line[0]    == ">" and "|" in line:
        line      = line.replace(">", "")  # delete the ">"
        line      = line.rstrip()

        if line   == "placulumab|Heavy":
            pass
        elif line == "cergutuzumab amunaleukin|Heavy2|Fusion":
            pass

        elif line == "otlertuzumab|Heavy":
            integratedSeqInfo.setdefault(line, ""),
            integratedSeqInfo.setdefault("otlertuzumab|Light", "")

        else:
            integratedSeqInfo.setdefault(line, "" )

        #if "|" in line:


            #field = line.split("|")
            #antibodyName = field[0]
            #if antibodyName in R_antibodyWithASetOfChain:
            #    integratedSeqInfo.setdefault(antibodyName + '|' + 'Heavy', [])
            #    integratedSeqInfo.setdefault(antibodyName + '|' + 'Light', [])

            #if antibodyName in R_heavyChainAntibody:
            #    if antibodyName == 'placulumab' or antibodyName =='otlertuzumab':
            #        pass
            #    integratedSeqInfo.setdefault(antibodyName + '|' + 'Heavy', [])

            #if antibodyName in R_lightChainAntibody:
            #    integratedSeqInfo.setdefault(antibodyName + '|' + 'Light', [])

            #if antibodyName in R_twoVersionAntibody:
            #    if dict_recommended_appearance[antibodyName] == ['H', 'H2', 'L']:
            #        integratedSeqInfo.setdefault(antibodyName + '|' + 'Heavy', [])
            #        integratedSeqInfo.setdefault(antibodyName + '|' + 'Light', [])
            #        integratedSeqInfo.setdefault(antibodyName + '|' + 'Heavy2', [])
            #       integratedSeqInfo.setdefault(antibodyName + '|' + 'Light', [])

            #   if dict_recommended_appearance[antibodyName] == ['H', 'L', 'L2']:
            #        integratedSeqInfo.setdefault(antibodyName + '|' + 'Heavy', [])
            #        integratedSeqInfo.setdefault(antibodyName + '|' + 'Light', [])
            #        integratedSeqInfo.setdefault(antibodyName + '|' + 'Heavy', [])
            #        integratedSeqInfo.setdefault(antibodyName + '|' + 'Light2', [])

            #   else:
            #        antibodyName = field[0] + field[1]
            #        integratedSeqInfo.setdefault(antibodyName, [])

            #if antibodyName in R_antibodyWithFusion:
            #   antibodyName = field[0] + field[1] + field[2]
            #   integratedSeqInfo.setdefault(antibodyName, [])

print('program 2 result: ')
print(integratedSeqInfo)
print(len(integratedSeqInfo))
print('\n')
recommended.close()

################################################################################
### main program 3
#
# 13.10.16
#
# 1.1 version By:(Echo) Ziyi Cui
#
# integratedSeqInfo = {antibodyName | Heavy/light :[sequence]}
# add the corresponding sequence of antibody from list 'R_antibodyWithASetOfChain'
# as the value of dict 'integratedSeqInfo'.
# Usage:
# ------
# integrateData.py + RL.faa -> stdout(print)

recommended       = open(r'inndata\RL.faa', 'r')
isReadingSequence = False

for line in recommended.readlines():
    if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
        isReadingSequence         = False

        if antibodyName in integratedSeqInfo:

            if antibodyName                             == "otlertuzumab|Heavy":
                integratedSeqInfo[antibodyName]         = currentSequence[0:117] + "\n"
                currentSequence = currentSequence.rstrip()
                lightChainSequence = currentSequence[143:251]
                lightChainSequence = lightChainSequence.replace("\n", "")
                integratedSeqInfo["otlertuzumab|Light"] = lightChainSequence[0:49] + "\n" \
                                                          + lightChainSequence[50:99] + "\n" \
                                                          + lightChainSequence[100:105] + "\n"
                print(integratedSeqInfo["otlertuzumab|Light"])

            else:
                integratedSeqInfo[antibodyName] += currentSequence
                #print(antibodyName)

        currentSequence = ""

    if isReadingSequence:
        currentSequence += line

    if line[0] == ">":
        if "-" in line:
            isReadingSequence = False
            continue
        else:
            isReadingSequence = True
            line = line.replace(">", "")  # delete the ">"
            line = line.rstrip()
            antibodyName = line

            #if "|" in line:
                #field = line.split("|")
                #antibodyName = field[0]

print('program 3 result: ')
print("integratedSeqInfo=", integratedSeqInfo)
print(len(integratedSeqInfo))
print('\n')

#savedStdout = sys.stdout
#with open(r'R_SeqDict.txt', 'w') as file:
#   sys.stdout = file
#  print(integratedSeqInfo)

recommended.close()

################################################################################
### main program 4
#
# 13.10.16
#
# 1.1 version By:(Echo) Ziyi Cui
#
# check the PL.daa with integratedseqInfo.
# 1.For the same antibody, if the sequence is different between the PL.faa and
# integratedInfo constructed from RL.faa, then print a warning message and retain
# the sequence in integratedseqInfo.
# 2.If antibody from PL.faa is not already in integratedseqInfo, then add its info
# into integratedseqInfo.
# 3.If antibody from PL.faa is is in integratedseqInfo and the sequences from two
# source are the same, then pass.
#
# Usage:
# ------
# integrateData.py + PL.faa -> stdout(print)

proposed = open(r'inndata\PL.faa', "r")
isReadingSequence = False

for line in proposed.readlines():

    if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
        isReadingSequence = False

        if antibodyName in integratedSeqInfo:
            if integratedSeqInfo[antibodyName] == p_sequence:
                pass

            else:
                if antibodyName in warningList:
                    pass

                else:
                    warningList.append(antibodyName)
                    #print(antibodyName)

        elif (antibodyName == "placulumab|Heavy") or (antibodyName == "cergutuzumab amunaleukin|Heavy2|Fusion"):
            pass

        elif antibodyName == 'otlertuzumab|Heavy':
            pass

        else:
            integratedSeqInfo.setdefault(antibodyName, None)
            integratedSeqInfo[antibodyName] = p_sequence
                #print(antibodyName)

        p_sequence = ""

    if isReadingSequence:
            p_sequence += line

    if line[0] == ">":
        if "-" in line:
            isReadingSequence = False
            continue
        else:
            isReadingSequence = True
            line              = line.replace(">", "")
            line              = line.rstrip()
            antibodyName      = line

print("main program 4 result:")
print("integratedSeqInfo=", integratedSeqInfo)
print(len(integratedSeqInfo))
print("warningList=", warningList)
print(len(warningList))
print("\n")

proposed.close()

################################################################################
### main program 5
#
# 13.10.16
#
# 1.0 version By:(Echo) Ziyi Cui
#
# sort integrateDataInfo.
#
# Usage:
# ------
# integrateData.py -> stdout(print)

dict_integratedSeqInfo_appearance = {}
for key in integratedSeqInfo:
    field = key.split("|")
    antibodyName = field[0]
    chainType = field[-1]
    dict_integratedSeqInfo_appearance.setdefault(antibodyName, [])

    if chainType   == "Heavy":
        dict_integratedSeqInfo_appearance[antibodyName].append('H')

    elif chainType == "Heavy2":
        dict_integratedSeqInfo_appearance[antibodyName].append('H2')

    elif chainType == "Light":
        dict_integratedSeqInfo_appearance[antibodyName].append('L')

    elif chainType == "Light2":
        dict_integratedSeqInfo_appearance[antibodyName].append('L2')

    elif chainType == "Fusion":
        chainType = field[1]+ 'F'
        dict_integratedSeqInfo_appearance[antibodyName].append(chainType)



#print('dict_integratedSeqInfo_appearance = ', dict_integratedSeqInfo_appearance)

# sort these antibodyNames into different groups, according to their chain appearance.
for antibodyName in dict_integratedSeqInfo_appearance:
    if (dict_integratedSeqInfo_appearance[antibodyName]   == ['H', 'L']) or (dict_integratedSeqInfo_appearance[antibodyName]   == ['L', 'H']):
        antibodyWithASetOfChain.append(antibodyName)

    elif dict_integratedSeqInfo_appearance[antibodyName] == ['H']:
        heavyChainAntibody.append(antibodyName)

    elif dict_integratedSeqInfo_appearance[antibodyName] == ['L']:
        lightChainAntibody.append(antibodyName)

    #elif dict_integratedSeqInfo_appearance[antibodyName] ==['']:
     #   twoVersionAntibody.append(antibodyName)

    #elif ('HeavyF' or 'LightF' or 'Heavy2F' or 'Light2F')in dict_integratedSeqInfo_appearance[antibodyName]:
     #   value = dict_integratedSeqInfo_appearance[antibodyName]
     #   antibodyWithFusion.setdefault(antibodyName, value)

    else:
        value = dict_integratedSeqInfo_appearance[antibodyName]
        specialAntibody.setdefault(antibodyName, value)

print("program 5 results: ")
print("antibodyWithASetOfChain=", antibodyWithASetOfChain)
print(len(antibodyWithASetOfChain))
print("heavyChainAntibody =", heavyChainAntibody)
print(len(heavyChainAntibody))
print("lightChainAntibody =", lightChainAntibody)
print(len(lightChainAntibody))
print("twoVersionAntibody=", twoVersionAntibody)
print(len(twoVersionAntibody))
#print("antibodyWithFusion=", antibodyWithFusion)
#print(len(antibodyWithFusion))
print("specialAntibody =", specialAntibody)
print(len(specialAntibody))
print('\n')

################################################################################
### main program 6
#
# 13.10.16
#
# 1.0 version By:(Echo) Ziyi Cui
#
# format the integrated data and put it into a file.
#
# Usage:
# ------
# R_sortAntibody.py + PL.faa -> stdout(print)

formatData = ""
for key in integratedSeqInfo:
    field = key.split("|")
    antibodyName = field[0]
    chainType = field[1]
    appearance = dict_integratedSeqInfo_appearance[antibodyName]

    if (antibodyName in antibodyWithASetOfChain) and chainType == 'Heavy':
        formatData += ">" + key + '\n' + integratedSeqInfo[key]
        correspondingL = antibodyName + '|Light'
        formatData += ">" + correspondingL + '\n' + integratedSeqInfo[correspondingL] + '\n\n'

    elif (antibodyName in heavyChainAntibody) or(antibodyName in lightChainAntibody):
        formatData += ">" + key + "\n" + integratedSeqInfo[key] + '\n\n'

    elif (appearance == ['H', 'LightF']) and chainType == 'Heavy':
        formatData += ">" + key + '\n' + integratedSeqInfo[key]
        correspondingL = antibodyName + '|Light|Fusion'
        formatData += ">" + correspondingL + '\n' + integratedSeqInfo[correspondingL] + '\n\n'

    elif appearance == ['H2', 'L', 'H'] and chainType == 'Heavy':
        formatData += ">" + key + '\n' + integratedSeqInfo[key]
        correspondingL = antibodyName + '|Light'
        formatData += ">" + correspondingL + '\n' + integratedSeqInfo[correspondingL] + '\n\n'

        correspondingH2 = antibodyName + '|Heavy2'
        formatData += ">" + correspondingH2 + '\n' + integratedSeqInfo[correspondingH2] \
                      + ">" + correspondingL + '\n' + integratedSeqInfo[correspondingL] + '\n\n'

    elif ((appearance == ['H', 'L', 'H2', 'L2']) or (appearance == ['L', 'H', 'L2', 'H2'])) and chainType == 'Heavy':
        formatData += ">" + key + '\n' + integratedSeqInfo[key]
        correspondingL = antibodyName + '|Light'
        formatData += ">" + correspondingL + '\n' + integratedSeqInfo[correspondingL] + '\n\n'

        correspondingH2 = antibodyName + '|Heavy2'
        correspondingL2 = antibodyName + '|Light2'
        formatData += ">" + correspondingH2 + '\n' + integratedSeqInfo[correspondingH2] \
                      + ">" + correspondingL2 + '\n' + integratedSeqInfo[correspondingL2] + '\n\n'


savedStdout = sys.stdout
with open('integratedData.txt', 'w+') as file:
    sys.stdout = file
    print(formatData)

sys.stdout = savedStdout
