import sys
import os
import subprocess
import time
from ROOT import TFile, TCanvas, TH1F, TColor, TAxis
from ROOT import kWhite, kBlack, kGray, kRed, kGreen, kBlue, kYellow, kMagenta, kCyan, kOrange, kSpring, kTeal, kAzure, kViolet, kPink
from ROOT import *

colors = [kRed, kBlack, kBlue-7, kRed+1, kOrange, kMagenta+1, kAzure+7, kTeal, kSpring-6, kYellow+1, kPink+10, kViolet-3, kAzure+1, kRed+3, kGray, kOrange+1, kGreen+3, kBlack, kBlue-7, kRed+1, kOrange, kMagenta+1, kAzure+7,]

from tdrstyle_all import *


def newName(path = "/nfs/dust/cms/user/amalara/sframe_all/MC_PU_studies/",
            new_path="/nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/common/data/",
            to_remove="uhh2.AnalysisModuleRunner.MC."):
    for sample in sorted(os.listdir(path)):
        if to_remove in sample:
            newfilename = "MyMCPileupHistogram_"+ sample[len(to_remove):len(sample)-5]+".root"
            cmd = "mv %s %s" % (path+sample, path+newfilename)
            a = os.system(cmd)
            cmd = "cp %s %s" % (path+newfilename, new_path+newfilename)
            a = os.system(cmd)


def tdrCanvas(name="c"):
    c = TCanvas( name, name, 50, 50, 800, 600)
    c.SetLogy()
    c.SetLogx(0)
    h_draw = c.DrawFrame(0,0.00001,100,0.035);
    h_draw.GetYaxis().SetTitleOffset( 1.5)
    h_draw.GetXaxis().SetTitleOffset(1.0)
    h_draw.GetXaxis().SetTitle("N_TrueInteractions")
    h_draw.GetYaxis().SetTitle("A.U.")
    h_draw.Draw("AXIS")
    return c

def Plot_histo_MC_PU_studies(c_name= "All", samples=["QCD"]):
    files = []
    histos = []
    c = tdrCanvas(c_name)
    leg = tdrLeg(0.25, 0.25, 0.6, 0.7)
    tdrHeader(leg, c_name)
    for index, sample in enumerate(samples):
        filename = "MyMCPileupHistogram_"+sample+".root"
        file = TFile.Open(path+filename)
        h = file.Get("input_Event/N_TrueInteractions")
        files.append(file)
        histos.append(h)
        h.GetYaxis().SetRangeUser(0.00001, 1)
        h.Scale(1./h.Integral())
        h.SetLineColor(colors[index+1])
        h.SetLineWidth(2)
        h.Draw("same")
        leg.AddEntry(h,sample,"l");
    h_gen.Draw("same")
    leg.AddEntry(h_gen,"gen","l");
    leg.Draw("same")
    c.Print(path+c_name+".pdf")
    c.Print(path+c_name+".png")

    N_bins = histos[0].GetXaxis().GetNbins()
    h_bins_min = TH1F( 'h_bins_min', 'h_bins_min', N_bins, 0, 100)
    h_bins_max = TH1F( 'h_bins_max', 'h_bins_max', N_bins, 0, 100)

    for i in range(0,N_bins):
        min = 1.
        max = 0.
        for h in histos:
            temp = h.GetBinContent(i)
            if temp < min:
                min = temp
            if temp > max:
                max = temp
        h_bins_min.SetBinContent(i, min)
        h_bins_max.SetBinContent(i, max)


    c1 = tdrCanvas(c_name+"_extreme")
    leg_1 = tdrLeg(0.25, 0.4, 0.6, 0.7)
    tdrHeader(leg_1, c_name)
    leg_1.AddEntry(h_bins_min,"h_bins_min","l");
    leg_1.AddEntry(h_bins_max,"h_bins_max","l");
    leg_1.AddEntry(h_gen,"gen","l");
    leg_1.Draw("same")
    h_bins_min.SetLineColor(kGreen+3)
    h_bins_max.SetLineColor(kBlue-7)
    h_bins_min.SetLineWidth(3)
    h_bins_max.SetLineWidth(3)
    h_bins_min.Draw("hist same")
    h_bins_max.Draw("hist same")
    h_gen.Draw("same")
    c1.Print(path+c_name+"_extreme.pdf")
    c1.Print(path+c_name+"_extreme.png")
    time.sleep(10)




path = "/nfs/dust/cms/user/amalara/sframe_all/MC_PU_studies/"
new_path = "/nfs/dust/cms/user/amalara/WorkingArea/UHH2_94X_v2/CMSSW_9_4_1/src/UHH2/common/data/"
to_remove = "uhh2.AnalysisModuleRunner.MC."

newName(path,new_path,to_remove)

file_gen = TFile.Open(path+"PileupMC_gen.root")
file_QCD = TFile.Open(path+"QCD.root")
file_TTbar = TFile.Open(path+"TTbar.root")
file_QCD_TTbar = TFile.Open(path+"QCD_TTbar.root")
h_gen = file_gen.Get("input_Event/N_TrueInteractions")
h_QCD = file_QCD.Get("input_Event/N_TrueInteractions")
h_TTbar = file_TTbar.Get("input_Event/N_TrueInteractions")
h_QCD_TTbar = file_QCD_TTbar.Get("input_Event/N_TrueInteractions")


c = tdrCanvas("Add")
leg = tdrLeg(0.25, 0.3, 0.6, 0.7)
tdrHeader(leg, "Add")
h_gen.Scale(1./h_gen.Integral())
h_QCD.Scale(1./h_QCD.Integral())
h_QCD_TTbar.Scale(1./h_QCD_TTbar.Integral())
h_TTbar.Scale(1./h_TTbar.Integral())
h_gen.SetLineColor(kRed+1)
h_QCD.SetLineColor(kBlue)
h_QCD_TTbar.SetLineColor(kOrange)
h_TTbar.SetLineColor(kGreen+3)
h_gen.SetLineWidth(3)
h_QCD.SetLineWidth(3)
h_QCD_TTbar.SetLineWidth(3)
h_TTbar.SetLineWidth(3)
h_gen.Draw("same")
h_QCD.Draw("same")
h_QCD_TTbar.Draw("same")
h_TTbar.Draw("same")
leg.AddEntry(h_gen,"gen","l");
leg.AddEntry(h_QCD,"QCD","l");
leg.AddEntry(h_TTbar,"TTbar","l");
leg.AddEntry(h_QCD_TTbar,"QCD+TTbar","l");
leg.Draw("same")

c.Print(path+"Add.pdf")
c.Print(path+"Add.png")

time.sleep(10)


for condition in ["","QCD", "TT"]:
    samples = []
    for sample in sorted(os.listdir(path)):
        if "MyMCPileupHistogram_" in sample:
            if not condition in sample:
                continue
            samples.append(sample[len("MyMCPileupHistogram_"):len(sample)-5])
    Plot_histo_MC_PU_studies(c_name= "All_"+condition, samples=samples)
