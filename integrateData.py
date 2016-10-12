#!/usr/bin/env python3
################################################################################
#
# program: R_sortAntibody.py
# Author:  (Echo) Ziyi Cui
# version: Version 1.1
# Date:    12/10/2016
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
# sortAntibody.py + RL.faa -> stdout(print)
#
################################################################################
# step 1:sort antibody in RL.faa

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
R_AntibodyWithFusion        = []
R_specialAntibody           = {}

isReadingSequence = False
currentSequence = ""

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
# R_sortAntibody.py + RL.faa -> stdout(print)

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
        R_AntibodyWithFusion.append(antibodyName)
    else:
        value = dict_recommended_appearance[antibodyName]
        R_specialAntibody.setdefault(antibodyName, value)

print("program 1 results: ")
print("R_antibodyWithASetOfChain=", R_antibodyWithASetOfChain)
print("R_heavyChainAntibody =", R_heavyChainAntibody)
print("R_lightChainAntibody =", R_lightChainAntibody)
print("R_twoVersionAntibody=", R_twoVersionAntibody)
print("R_AntibodyWithFusion=", R_AntibodyWithFusion)
print("R_specialAntibody =", R_specialAntibody)
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
# R_sortAntibody.py + RL.faa -> stdout(print)

################################################################################
integratedSeqInfo = {}
recommended = open(r'inndata\RL.faa', 'r')

for line in recommended.readlines():
    if line[0] == ">" and  "|" in line:
        line = line.replace(">", "")  # delete the ">"
        line = line.rstrip()

        if line == "placulumab|Heavy" or line == "otlertuzumab|Heavy":
            pass
        else:
            integratedSeqInfo.setdefault(line, [])

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

            #if antibodyName in R_AntibodyWithFusion:
            #   antibodyName = field[0] + field[1] + field[2]
            #   integratedSeqInfo.setdefault(antibodyName, [])

print('program 2 result: ')
print(integratedSeqInfo)
print('\n')
recommended.close()

################################################################################
### main program 3
#
# 12.10.16
#
# 1.0 version By:(Echo) Ziyi Cui
#
# integratedSeqInfo = {antibodyName | Heavy/light :[sequence]}
# add the corresponding sequence of antibody from list 'R_antibodyWithASetOfChain'
# as the value of dict 'integratedSeqInfo'.
# Usage:
# ------
# R_sortAntibody.py + RL.faa -> stdout(print)

recommended = open(r'inndata\RL.faa', 'r')
for line in recommended.readlines():
    if line[0] == '>' or line[0] == '\n' and isReadingSequence:
        isReadingSequence = False

        if antibodyName in integratedSeqInfo:
            integratedSeqInfo[antibodyName].append(currentSequence)
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
print(integratedSeqInfo)
print('\n')

#savedStdout = sys.stdout
#with open(r'R_SeqDict.txt', 'w') as file:
#   sys.stdout = file
#  print(integratedSeqInfo)

recommended.close()

################################################################################
### main program 4
#
# 12.10.16
#
# 1.0 version By:(Echo) Ziyi Cui
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
# R_sortAntibody.py + PL.faa -> stdout(print)

proposed = open(r'inndata\PL.faa', "r")
p_sequence = ""
warningList =[]
for line in proposed.readlines():

    if line[0] == '>' or line[0] == '\n' and isReadingSequence:
        isReadingSequence = False

        if antibodyName in integratedSeqInfo:
            if integratedSeqInfo[antibodyName] == p_sequence:
                pass
            else:
                warningList.append(antibodyName)

        else:
            integratedSeqInfo.setdefault(antibodyName, p_sequence)

        p_sequence = ""

        if isReadingSequence:
            p_sequence += line

        if line[0] == ">":
            if "-" in line:
                isReadingSequence = False
                continue
            else:
                isReadingSequence = True
                line = line.replace(">", "")
                line = line.rstrip()
                antibodyName = line








