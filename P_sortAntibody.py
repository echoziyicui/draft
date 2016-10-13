#!/usr/bin/env python3
################################################################################
#
# program: P_sortAntibody.py
# Author:  (Echo) Ziyi Cui
# version: Version 1.2
# Date:    13/10/2016
#
# Function:
# ---------
# From the file with antibody sequence, collect the appearance of heavy chain,
# light chain, or any other uncommon chain. Then sort them to different groups
# according to this appearance.
#
# Usage:
# ------
# P_sortAntibody.py + PL.faa -> stdout
#
################################################################################
# constant about PL.faa
proposed = open(r'inndata\PL.faa', "r")
dict_proposed_appearance = {}
P_antibodyWithASetOfChain = []
P_heavyChainAntibody = []
P_lightChainAntibody = []
P_twoVersionAntibody = []
P_AntibodyWithFusion = []
P_specialAntibody = {}

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
# P_sortAntibody.py + PL.faa -> stdout(print)

for line in proposed.readlines():
    if line[0] == ">":
        line   = line.replace(">", "")  # delete the ">"
        line   = line.rstrip()

        if "|" in line:
            field        = line.split("|")
            antibodyName = field[0]
            chainType    = field[-1]
            dict_proposed_appearance.setdefault(antibodyName, [])

            if chainType   == "Heavy":
                dict_proposed_appearance[antibodyName].append('H')

            elif chainType == "Heavy2":
                dict_proposed_appearance[antibodyName].append('H2')

            elif chainType == "Light":
                dict_proposed_appearance[antibodyName].append('L')

            elif chainType == "Light2":
                dict_proposed_appearance[antibodyName].append('L2')

            elif chainType == "Fusion":
                dict_proposed_appearance[antibodyName].append('F')

#print('dict = ', dict_recommended_appearance)


# sort these antibodyNames into different groups, according to their chain appearance.
for antibodyName in dict_proposed_appearance:
    if dict_proposed_appearance[antibodyName]   == ['H', 'L']:
        P_antibodyWithASetOfChain.append(antibodyName)
    elif dict_proposed_appearance[antibodyName] == ['H']:
        P_heavyChainAntibody.append(antibodyName)
    elif dict_proposed_appearance[antibodyName] == ['L']:
        P_lightChainAntibody.append(antibodyName)
    elif 'H2' in dict_proposed_appearance[antibodyName] or 'L2' in dict_proposed_appearance[antibodyName]:
        P_twoVersionAntibody.append(antibodyName)
    elif 'F' in dict_proposed_appearance[antibodyName]:
        P_AntibodyWithFusion.append(antibodyName)
    else:
        value = dict_proposed_appearance[antibodyName]
        R_specialAntibody.setdefault(antibodyName, value)

print("program 1 results: ")
print("P_antibodyWithASetOfChain=", P_antibodyWithASetOfChain)
print("P_heavyChainAntibody =", P_heavyChainAntibody)
print("P_lightChainAntibody =", P_lightChainAntibody)
print("P_twoVersionAntibody=", P_twoVersionAntibody)
print("P_AntibodyWithFusion=", P_AntibodyWithFusion)
print("P_specialAntibody =", P_specialAntibody)
print('\n')

#for antibodyName in P_antibodyWithASetOfChain:
    #if antibodyName in R_antibodyWithASetOfChain:
       # pass
   # else:
       # print(antibodyName)