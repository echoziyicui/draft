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
# step 1: Processing data in PL.faa
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

R_antibodyWithASetOfChain= ['daratumumab', 'bococizumab', 'lorvotuzumab mertansin', 'gantenerumab', 'tildrakizumab', 'milatuzumab', 'bavituximab', 'lenzilumab', 'tenatumomab', 'patritumab', 'concizumab', 'anifrolumab', 'rilotumumab', 'urelumab', 'alacizumab pegol', 'inclacumab', 'indatuximab ravtansin', 'sarilumab', 'suvizumab', 'pidilizumab', 'fresolimumab', 'vadastuximab talirin', 'mirvetuximab soravtansin', 'vandortuzumab vedotin', 'benralizumab', 'samalizumab', 'alirocumab', 'veltuzumab', 'brodalumab', 'amatuximab', 'brentuximab vedotin', 'evinacumab', 'idarucizumab', 'ralpancizumab', 'drozitumab', 'ontuxizumab', 'firivumab', 'lokivetmab', 'ulocuplumab', 'modotuximab', 'risankizumab', 'sacituzumab govitecan', 'imalumab', 'lirilumab', 'seribantumab', 'olokizumab', 'tezepelumab', 'simtuzumab', 'obiltoxaximab', 'dinutuximab', 'racotumomab', 'narnatumab', 'begelomab', 'tarextumab', 'denintuzumab mafodotin', 'enfortumab vedotin', 'romosozumab', 'perakizumab', 'sifalimumab', 'orticumab', 'dacetuzumab', 'emibetuzumab', 'brontictuzumab', 'sofituzumab vedotin', 'rinucumab', 'olaratumab', 'teplizumab', 'farletuzumab', 'flanvotumab', 'ocaratuzumab', 'enokizumab', 'afasevikumab', 'eldelumab', 'bezlotoxumab', 'evolocumab', 'lodelcizumab', 'trevogrumab', 'anetumab ravtansin', 'bimekizumab', 'cantuzumab ravtansin', 'vedolizumab', 'pateclizumab', 'navivumab', 'pamrevlumab', 'vatelizumab', 'landogrozumab', 'dupilumab', 'atezolizumab', 'margetuximab', 'solanezumab', 'glembatumumab vedotin', 'atinumab', 'secukinumab', 'pritoxaximab', 'tabalumab', 'nivolumab', 'namilumab', 'onartuzumab', 'ibalizumab', 'girentuximab', 'ponezumab', 'abrilumab', 'opicinumab', 'bleselumab', 'dapirolizumab pegol', 'imgatuzumab', 'lifastuzumab vedotin', 'fasinumab', 'rivabazumab pegol', 'durvalumab', 'rafivirumab', 'fulranumab', 'elotuzumab', 'enavatuzumab', 'pinatuzumab vedotin', 'figitumumab', 'monalizumab', 'pembrolizumab', 'varlilumab', 'rontalizumab', 'isatuximab', 'fezakinumab', 'blosozumab', 'lampalizumab', 'indusatumab', 'dectrekumab', 'icrucumab', 'indusatumab vedotin', 'ramucirumab', 'tregalizumab', 'lilotomab', 'vesencumab', 'tosatoxumab', 'tralokinumab', 'oxelumab', 'otelixizumab', 'ficlatuzumab', 'tisotumab vedotin', 'vorsetuzumab mafodotin', 'quilizumab', 'duligotuzumab', 'nemolizumab', 'lucatumumab', 'fletikumab', 'tesidolumab', 'siltuximab', 'itolizumab', 'enoticumab', 'actoxumab', 'ozanezumab', 'emactuzumab', 'mavrilimumab', 'polatuzumab vedotin', 'ganitumab', 'lebrikizumab', 'bimagrumab', 'ligelizumab', 'vantictumab', 'briakinumab', 'avelumab', 'nesvacumab', 'foralumab', 'aducanumab', 'rovalpituzumab tesirin', 'crenezumab', 'coltuximab ravtansin', 'mogamulizumab', 'vorsetuzumab', 'rovalpituzumab', 'parsatuzumab', 'cixutumumab', 'setoxaximab', 'roledumab', 'tisotumab', 'sirukumab', 'trastuzumab emtansin', 'lumretuzumab', 'panobacumab', 'foravirumab', 'carlumab', 'demcizumab', 'guselkumab', 'futuximab', 'ublituximab', 'tovetumab', 'elgemtumab', 'codrituzumab', 'dalotuzumab', 'diridavumab', 'plozalizumab', 'etaracizumab', 'obinutuzumab', 'necitumumab', 'tigatuzumab', 'glembatumumab', 'ensituximab', 'robatumumab', 'intetumumab', 'labetuzumab govitecan', 'etrolizumab', 'dusigitumab', 'abituzumab', 'gevokizumab', 'ixekizumab', 'teprotumumab', 'abagovomab', 'clazakizumab']

for antibodyName in P_antibodyWithASetOfChain:
    if antibodyName in R_antibodyWithASetOfChain:
        pass
    else:
        print(antibodyName)