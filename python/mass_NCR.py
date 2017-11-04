#!/usr/bin/python
import ROOT as rt

import PoI #particles of interest

# W40incl1M	W60incl1M	Winc1M		WinclMatchBox

# open the file, read the TTree
fp3 = rt.TFile.Open("../files/Wplus_qqbar_MatchBox_output.root")
events3 = fp3.Get("events")

fp4 = rt.TFile.Open("../files/Wplus_qqbar_MatchBox_NCR_output.root")
events4 = fp4.Get("events")

# set TDR style
rt.gROOT.LoadMacro("../C++/setTDRStyle.C")
from ROOT import setTDRStyle
setTDRStyle()

globalGoFast = False

### nominal mass 80.402999

selection = ""
variable = "invM"
mult3 = rt.TH1F("mult3","M_W = nominal; particles; fraction",200, 50, 120)
mult3.Sumw2() 
mult4 = rt.TH1F("mult4","M_W = nominal [MatchBox]; particles; fraction",200, 50,120)
mult4.Sumw2() 

goFast = events3.GetEntries()
print "TTree has", goFast, "entries"
if globalGoFast: goFast = 10000
print "analyzing", goFast, "events3"
events3.Draw(variable+">>mult3",selection,"goff", goFast)
mult3.Scale(1.0/goFast)
mult3.SetLineWidth(2)
mult3.SetLineColor(rt.kBlue)
mult3.SetMarkerColor(rt.kBlue)

goFast = events4.GetEntries()
print "TTree has", goFast, "entries"
if globalGoFast: goFast = 10000
print "analyzing", goFast, "events4"
events4.Draw(variable+">>mult4",selection,"goff", goFast)
mult4.Scale(1.0/goFast)
mult4.SetLineWidth(2)
mult4.SetLineColor(rt.kBlack)



### plot
rt.gStyle.SetOptTitle(0)
c1 = rt.TCanvas()
c1.cd()
#c1.SetLogy()
#mult1.Draw("hist")
#mult2.Draw("hist same")
mult4.Draw("hist")
mult3.Draw("hist same")


c1.SaveAs("../plots/mult.pdf")
c1.SaveAs("../plots/mult.png")



