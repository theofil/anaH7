#!/usr/bin/python
import ROOT as rt
import sys

import PoI #particles of interest

# W40incl1M	W60incl1M	Winc1M		WinclMatchBox

# open the file, read the TTree
fp3 = rt.TFile.Open("../files/Wplus_qqbar_MatchBox_NCR_filtered.root") # 1.0 e+09 W->qqbar decays
events3 = fp3.Get("events")

fp4 = rt.TFile.Open("../files/Wplus_qqbar_MatchBox_NCR_output.root")   # 1.0 e+06 W->qqbar decays
events4 = fp4.Get("events")

# set TDR style
rt.gROOT.LoadMacro("../C++/setTDRStyle.C")
from ROOT import setTDRStyle
setTDRStyle()

globalGoFast = False

### nominal mass 80.402999

selection1 = "nNu==0"
selection2 = "nNu>0"
variable = "nCh"
mult3 = rt.TH1F("mult3"," ;charged particles ; events / million W #rightarrow q#bar{q} decays",40, 0, 40)
mult3.Sumw2() 
mult4 = rt.TH1F("mult4"," ;charged particles ; events / million W #rightarrow q#bar{q} decays",40, 0, 40)
mult4.Sumw2() 

goFast = events3.GetEntries()
print "TTree has", goFast, "entries"
if globalGoFast: goFast = 10000
print "analyzing", goFast, "events3"
events3.Draw(variable+">>mult3",selection1,"goff", goFast)
#mult3.Scale(goFast/10**3)
mult3.Scale(1./10**3)
mult3.SetLineWidth(2)

goFast = events4.GetEntries()
print "TTree has", goFast, "entries"
if globalGoFast: goFast = 10000
print "analyzing", goFast, "events4"
events4.Draw(variable+">>mult4",selection2,"goff", goFast)
#mult4.Scale(goFast)

mult4.SetLineWidth(2)
mult4.SetLineStyle(1)
mult4.SetLineColor(rt.kBlack)
mult4.SetMarkerColor(rt.kBlack)
mult3.SetLineWidth(2)
mult3.SetLineStyle(2)
mult3.SetLineColor(rt.kRed)
mult3.SetMarkerColor(rt.kRed)

### plot
rt.gStyle.SetOptTitle(0)
c1 = rt.TCanvas()
c1.cd()
c1.SetLogy()

mult4.GetYaxis().SetTitleOffset(1.13)
mult4.GetYaxis().SetRangeUser(0.001, 10000000)
mult4.Draw("hist ")
mult3.Draw("same e1 hist")


leg1 = rt.TLegend(0.45,0.8,0.73,0.93)
leg1.SetTextSize(26)
leg1.SetTextFont(43)
leg1.SetFillColor(rt.kWhite)
leg1.SetFillStyle(0)
leg1.SetBorderSize(0)
leg1.AddEntry(mult3, "W^{+} #rightarrow no-neutrals","p")
leg1.AddEntry(mult4, "W^{+} #rightarrow background","l")
leg1.Draw("same")


paveText = rt.TPaveText( 0.73, 0.66, 0.95, 0.87,"NDC")
paveText.SetBorderSize(0)
paveText.SetFillColor(0)
paveText.SetFillStyle(0)
paveText.SetTextSize(26)
paveText.SetTextFont(43)
paveText.SetTextColor(rt.kBlue)
#paveText.AddText("W^{+} #rightarrow no-neutrals")
paveText.Draw("same")

c1.SaveAs("../plots/PDFs/"+sys.argv[0][0:-3]+".pdf")
c1.SaveAs("../plots/"+sys.argv[0][0:-3]+".png")

print "1-NN events per 1M of W-> qqbar ", mult4.GetEntries()
print "NN events per 1M of W-> qqbar = ", mult3.Integral()

NN = mult3.GetEntries()
NNError = NN**0.5

print "branching ratio:", NN/1000., "+/-", NNError/1000.0
 
