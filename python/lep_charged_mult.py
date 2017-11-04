#!/usr/bin/python
import ROOT as rt
import sys

import PoI #particles of interest

# W40incl1M	W60incl1M	Winc1M		WinclMatchBox

# open the file, read the TTree

fp4 = rt.TFile.Open("../files/LEP_output.root")
events4 = fp4.Get("events")

# set TDR style
rt.gROOT.LoadMacro("../C++/setTDRStyle.C")
from ROOT import setTDRStyle
setTDRStyle()

globalGoFast = False

### nominal mass 80.402999

selection = "nNu==0"
variable = "nCh+nNu"
mult4 = rt.TH1F("mult4","; stable charged particles; fraction",20, 0,20)
mult4.Sumw2() 


goFast = events4.GetEntries()
print "TTree has", goFast, "entries"
if globalGoFast: goFast = 10000
print "analyzing", goFast, "events4"
events4.Draw(variable+">>mult4",selection,"goff", goFast)
mult4.Scale(1.0/goFast)

mult4.SetLineWidth(2)
mult4.SetLineStyle(1)
mult4.SetLineColor(rt.kBlack)
mult4.SetMarkerColor(rt.kBlack)

### plot
rt.gStyle.SetOptTitle(0)
c1 = rt.TCanvas()
c1.cd()
#c1.SetLogy()
mult4.GetYaxis().SetTitleOffset(1.13)
mult4.Draw("hist")

paveText = rt.TPaveText( 0.32, 0.78, 0.52, 0.98,"blNDC")
paveText.SetBorderSize(0)
paveText.SetFillColor(0)
paveText.SetFillStyle(0)
paveText.SetTextSize(26)
paveText.SetTextFont(43)
paveText.SetTextColor(9)
paveText.AddText("Z^{0}/#gamma #rightarrow no-neutrals")
paveText.Draw("same")

c1.SaveAs("../plots/"+sys.argv[0][0:-3]+".pdf")
c1.SaveAs("../plots/"+sys.argv[0][0:-3]+".png")

print "rate for NN = ", mult4.GetEntries()


