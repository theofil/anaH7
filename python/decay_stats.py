#!/usr/bin/python
### https://root.cern/doc/master/group__tutorial__pyroot.html
import ROOT as rt
import sys

import PoI #particles of interest



fp4 = rt.TFile.Open("../files/Wplus_qqbar_MatchBox_NCR_output.root")
events = fp4.Get("events")

# set TDR style
rt.gROOT.LoadMacro("../C++/setTDRStyle.C")
from ROOT import setTDRStyle
setTDRStyle()



xMin = 0
xMax = 100
bins = 100

title = "; particles ; events / 1 million W #rightarrow q#bar{q} "

pID_all = rt.TH1F("pID_all",title, bins, xMin, xMax )
pID_all.Sumw2() 

pID_211 = rt.TH1F("pID_211",title, bins, xMin, xMax )
pID_211.Sumw2() 

pID_111 = rt.TH1F("pID_111",title, bins, xMin, xMax )
pID_111.Sumw2() 

pID_443 = rt.TH1F("pID_443",title, bins, xMin, xMax )
pID_443.Sumw2() 


globalGoFast = True
goFast = events.GetEntries()
print "TTree has", goFast, "entries"
if globalGoFast: goFast = 100000
print "analyzing", goFast, "events"

### Fill the mass histogram
events = events
totEntries = events.GetEntriesFast()
#for jentry in xrange(241,242):
for jentry in xrange(goFast):
    nb = events.GetEntry(jentry)
    if nb<=0:
        continue

    pID_all.Fill(events.nCh + events.nNu)

    ### count how many charged pions
    pID_211_sum = 0
    pID_111_sum = 0
    pID_443_sum = 0
    for particle in xrange(events.nTracks):
        is211 = False
        is111 = False

        if abs(events.ID[particle]) == 211 and events.isFromW[particle]: 
	    pID_211_sum = pID_211_sum + 1
            is211 = True

        if abs(events.ID[particle]) == 22 and events.isFromW[particle] and abs(events.MID[particle]) == 111 : 
	    pID_111_sum = pID_111_sum + 1
            is111 = True

        if abs(events.isFromW[particle]) and abs(events.MID[particle]) == 443 : 
	    pID_443_sum = pID_443_sum + 1
            is443 = True

    pID_211.Fill(pID_211_sum)
    if pID_111_sum%2==0: pID_111.Fill(int(pID_111_sum/2))  ### there are some sporadic single photons coming from a pi0 which I don't understand
    if pID_443_sum%2==0: pID_443.Fill(int(pID_443_sum/2))  



### plot pID_211
pID_211.SetLineWidth(2)
pID_211.SetLineStyle(1)
pID_211.SetLineColor(rt.kBlack)
pID_211.SetMarkerColor(rt.kBlack)
pID_211.GetYaxis().SetTitleOffset(1.13)
pID_211.GetXaxis().SetNdivisions(507)

rt.gStyle.SetOptTitle(0)
c_pID_211 = rt.TCanvas()
c_pID_211.cd()
pID_211.Draw("hist")

leg1 = rt.TLegend(0.75,0.8,0.93,0.93)
leg1.SetTextSize(24)
leg1.SetTextFont(43)
leg1.SetFillColor(rt.kWhite)
leg1.SetFillStyle(0)
leg1.SetBorderSize(0)
leg1.AddEntry(pID_211, "#pi^{#pm}","l")
leg1.Draw("same")
c_pID_211.SaveAs("../plots/PDFs/"+sys.argv[0][0:-3]+"_pID_211.pdf")
c_pID_211.SaveAs("../plots/"+sys.argv[0][0:-3]+"_pID_211.png")

print "pID_211.GetMean() = ", pID_211.GetMean()

### plot pID_111
pID_111.SetLineWidth(2)
pID_111.SetLineStyle(1)
pID_111.SetLineColor(rt.kBlack)
pID_111.SetMarkerColor(rt.kBlack)
pID_111.GetYaxis().SetTitleOffset(1.13)
pID_111.GetXaxis().SetNdivisions(507)

rt.gStyle.SetOptTitle(0)
c_pID_111 = rt.TCanvas()
c_pID_111.cd()
pID_111.Draw("hist")

leg1 = rt.TLegend(0.75,0.8,0.93,0.93)
leg1.SetTextSize(24)
leg1.SetTextFont(43)
leg1.SetFillColor(rt.kWhite)
leg1.SetFillStyle(0)
leg1.SetBorderSize(0)
leg1.AddEntry(pID_111, "#pi^{0}","l")
leg1.Draw("same")
c_pID_111.SaveAs("../plots/PDFs/"+sys.argv[0][0:-3]+"_pID_111.pdf")
c_pID_111.SaveAs("../plots/"+sys.argv[0][0:-3]+"_pID_111.png")

print "pID_111.GetMean() = ", pID_111.GetMean()


### plot pID_443
pID_443.SetLineWidth(2)
pID_443.SetLineStyle(1)
pID_443.SetLineColor(rt.kBlack)
pID_443.SetMarkerColor(rt.kBlack)
pID_443.GetYaxis().SetTitleOffset(1.13)
pID_443.GetXaxis().SetNdivisions(507)

rt.gStyle.SetOptTitle(0)
c_pID_443 = rt.TCanvas()
c_pID_443.cd()
pID_443.Draw("hist")

leg1 = rt.TLegend(0.75,0.8,0.93,0.93)
leg1.SetTextSize(24)
leg1.SetTextFont(43)
leg1.SetFillColor(rt.kWhite)
leg1.SetFillStyle(0)
leg1.SetBorderSize(0)
leg1.AddEntry(pID_443, "J/#psi","l")
leg1.Draw("same")
c_pID_443.SaveAs("../plots/PDFs/"+sys.argv[0][0:-3]+"_pID_443.pdf")
c_pID_443.SaveAs("../plots/"+sys.argv[0][0:-3]+"_pID_443.png")

print "pID_443.GetMean() = ", pID_443.GetMean()



