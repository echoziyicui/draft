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
# From the file with antibody sequence, collect the appearance of heavy chain,
# light chain, or any other uncommon chain. Then sort them to different groups
# according to this appearance.
#
# Usage:
# ------
# sortAntibody.py + RL.faa -> R_sortAntibody.txt
#
################################################################################
# step 1: Processing data in RL.faa
################################################################################
# constant about RL.faa
recommended = open(r'inndata\RL.faa', "r")
dict_recommended_appearance = {}
R_antibodyWithASetOfChain = []
R_heavyChainAntibody = []
R_lightChainAntibody = []
R_twoVersionAntibody = []
R_AntibodyWithFusion = []
R_specialAntibody = {}

################################################################################
### main program
#
# 12.10.16
#
# 1.1 version By:(Echo) Ziyi Cui
#
# obtain all antibodyName in recommended.faa and collect the information of their
# heavy/light chain appearance.
# Then sort them according to this appearance.
#
# Usage:
# ------
# R_sortAntibody.py + RL.faa -> stdout(print)

for line in recommended.readlines():
    if line[0] == ">":
        line = line.replace(">", "")  # delete the ">"
        line = line.rstrip()

        if "|" in line:
            field = line.split("|")
            antibodyName = field[0]
            chainType = field[-1]
            dict_recommended_appearance.setdefault(antibodyName, [])

            if chainType == "Heavy":
                dict_recommended_appearance[antibodyName].append('H')

            elif chainType == "Heavy2":
                dict_recommended_appearance[antibodyName].append('H2')

            elif chainType == "Light":
                dict_recommended_appearance[antibodyName].append('L')

            elif chainType == "Light2":
                dict_recommended_appearance[antibodyName].append('L2')

            elif chainType == "Fusion":
                dict_recommended_appearance[antibodyName].append('F')

print(dict_recommended_appearance)

for antibodyName in dict_recommended_appearance:
    if dict_recommended_appearance[antibodyName] == ['H', 'L']:
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

print("R_heavyChainAntibody =", R_heavyChainAntibody)
print("R_lightChainAntibody =", R_lightChainAntibody)
print("R_twoVersionAntibody=", R_twoVersionAntibody)
print("R_AntibodyWithFusion=", R_AntibodyWithFusion)
print("R_specialAntibody =", R_specialAntibody)
print('\n')
################################################################################
#
# add the sequences of normal antibody with a set of heavy chain and light to a
# new dictionary.
#
################################################################################
integratedSeqInfo = {}
recommended = open(r'inndata\RL.faa', "r")

for line in recommended.readlines():
    if line[0] == ">":
        line = line.replace(">", "")  # delete the ">"
        line = line.rstrip()

        if "|" in line:
            field = line.split("|")
            antibodyName = field[0]

        if antibodyName in R_antibodyWithASetOfChain:
            integratedSeqInfo.setdefault(antibodyName, [])

        if 
print(integratedSeqInfo)
