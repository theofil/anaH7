#!/usr/bin/python
import ROOT as rt
import sys

import PoI #particles of interest

# W40incl1M	W60incl1M	Winc1M		WinclMatchBox

# open the file, read the TTree
fp3 = rt.TFile.Open("../files/LEP_output.root")
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
variable = "nCh+nNu"
bins = 100
xMin = 0
xMax = 100
hist3 = rt.TH1F("hist3","; particles; fraction", bins, xMin, xMax )
hist3.Sumw2() 
hist4 = rt.TH1F("hist4","; particles ; fraction",bins, xMin, xMax)
hist4.Sumw2() 

goFast = events3.GetEntries()
print "TTree has", goFast, "entries"
if globalGoFast: goFast = 10000
print "analyzing", goFast, "events3"
events3.Draw(variable+">>hist3",selection,"goff", goFast)
hist3.Scale(1.0/goFast)
hist3.SetLineWidth(2)

goFast = events4.GetEntries()
print "TTree has", goFast, "entries"
if globalGoFast: goFast = 10000
print "analyzing", goFast, "events4"
events4.Draw(variable+">>hist4",selection,"goff", goFast)
hist4.Scale(1.0/goFast)

hist4.SetLineWidth(2)
hist4.SetLineStyle(1)
hist4.SetLineColor(rt.kBlack)
hist4.SetMarkerColor(rt.kBlack)
hist3.SetLineWidth(2)
hist3.SetLineStyle(2)
hist3.SetLineColor(rt.kRed)

### plot
rt.gStyle.SetOptTitle(0)
c1 = rt.TCanvas()
c1.cd()
c1.SetLogy()
hist4.GetYaxis().SetTitleOffset(1.13)

hist4.Draw("hist")
hist3.Draw("hist same")

leg1 = rt.TLegend(0.65,0.8,0.93,0.93)
leg1.SetTextSize(30)
leg1.SetTextFont(43)
leg1.SetFillColor(rt.kWhite)
leg1.SetFillStyle(0)
leg1.SetBorderSize(0)
leg1.AddEntry(hist3, "Z #rightarrow q#bar{q}","l")
leg1.AddEntry(hist4, "W #rightarrow q#bar{q}","l")
leg1.Draw("same")


c1.SaveAs("../plots/PDFs"+sys.argv[0][0:-3]+".pdf")
c1.SaveAs("../plots/"+sys.argv[0][0:-3]+".png")



