import sys, multiprocessing, time
from ROOT import *

def read_xml(xmlFileDir):
    #try:
    xmlFile = open(str(xmlFileDir))
    rootFileStore = []
    comment =False
    for line in xmlFile:
        if '<!--' in line and not '-->':
            comment = True
            continue
        if '-->' in line:
            comment=False
            continue
        rootFileStore.append(line.split('"')[1])
    return rootFileStore


def read_treeFast(rootDir):
    fastentries =0
    try:
        ntuple = TFile(str(rootDir))
        AnalysisTree = ntuple.Get("AnalysisTree")
        fastentries =  AnalysisTree.GetEntries()
    except Exception as e:
        print 'unable to count events in root file',rootDir
        print e
    return fastentries


def CountEntries(xml):
    pool = multiprocessing.Pool(processes=int(10))
    print "open XML file:",xml
    rootFileStore = read_xml(xml)
    numberXMLFiles = len(rootFileStore)
    result = None
    if(fast):
        result = pool.map_async(read_treeFast,rootFileStore)
    else:
        result = pool.map_async(read_tree,rootFileStore)


    sum = 0
    for file in read_xml(xml):
        sum += read_treeFast(file)
    print xml, sum



python readaMCatNloEntries.py 20 /nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/BoostedHiggsToWW/config/xmlfile/HZ_HiggsToWWZToLL_Pythia8_TuneCP5.xml False

python readaMCatNloEntries.py 20 /nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/common/datasets/RunII_94X_v1_woHOTVR_woXCONE/MC_DY1JetsToLL_M-50.xml False
python readaMCatNloEntries.py 20 /nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/common/datasets/RunII_94X_v1_woHOTVR_woXCONE/MC_DY2JetsToLL_M-50.xml False
python readaMCatNloEntries.py 20 /nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/common/datasets/RunII_94X_v1_woHOTVR_woXCONE/MC_DY3JetsToLL_M-50.xml False
python readaMCatNloEntries.py 20 /nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/common/datasets/RunII_94X_v1_woHOTVR_woXCONE/MC_DY4JetsToLL_M-50.xml False

python readaMCatNloEntries.py 20 /nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/common/datasets/RunII_94X_v1_woHOTVR_woXCONE/MC_TTbarSemiLeptonic.xml False
python readaMCatNloEntries.py 20 /nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/common/datasets/RunII_94X_v1_woHOTVR_woXCONE/MC_TTTo2L2Nu.xml True
python readaMCatNloEntries.py 20 /nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/common/datasets/RunII_94X_v1_woHOTVR_woXCONE/MC_TTToHadronic.xml False

python readaMCatNloEntries.py 20 /nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/common/datasets/RunII_80X_v3_EGReg/WZ_EGReg.xml False
python readaMCatNloEntries.py 20 /nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/common/datasets/RunII_80X_v3_EGReg/ZZ_EGReg.xml False
