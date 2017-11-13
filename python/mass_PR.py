#!/usr/bin/python
### https://root.cern/doc/master/group__tutorial__pyroot.html
import ROOT as rt
import sys

import PoI #particles of interest


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


selection = ""
variable = "invM"
bins = 100
xMin = 80.4-0.1
xMax = 80.4+0.1
binwidth = (xMax-xMin)/bins
print "bin width = "+str(1000*(xMax-xMin)/bins)+" MeV"
hist3 = rt.TH1F("hist3","; mass [GeV]; fraction / "+str(1000*(xMax-xMin)/bins)+" MeV", bins, xMin, xMax )
hist3.Sumw2() 
hist4 = rt.TH1F("hist4","; mass [GeV]; fraction / "+str(1000*(xMax-xMin)/bins)+" MeV",bins, xMin, xMax)
hist4.Sumw2() 

#goFast = events3.GetEntries()
#print "TTree has", goFast, "entries"
#if globalGoFast: goFast = 10000
#print "analyzing", goFast, "events3"
#events3.Draw(variable+">>hist3",selection,"goff", goFast)
#hist3.Scale(1.0/goFast)
#hist3.SetLineWidth(2)

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
#hist3.SetLineWidth(2)
#hist3.SetLineStyle(2)
#hist3.SetLineColor(rt.kRed)

### Fit BW
class BW_func:
    def __call__( self, x, par ): 
	return  (par[1]/((x[0]-par[0])*(x[0]-par[0]) + par[1]*par[1]/4.))/(2*3.1415)


f_bw = rt.TF1("f_bw",BW_func(), xMin, xMax, 2)
f_bw.FixParameter(0, 80.403) ### Hardcoded values in Herwig
f_bw.FixParameter(1, 2.141 ) ### Hardcoded width
#hist4.Fit(f_bw)




### plot
rt.gStyle.SetOptTitle(0)
c1 = rt.TCanvas()
c1.cd()
c1.SetLogy()
hist4.GetYaxis().SetTitleOffset(1.13)
hist4.GetXaxis().SetNdivisions(509)
hist4.Draw("hist")
#f_bw.Draw("same")
#hist3.Draw("hist same")

leg1 = rt.TLegend(0.65,0.8,0.93,0.93)
leg1.SetTextSize(24)
leg1.SetTextFont(43)
leg1.SetFillColor(rt.kWhite)
leg1.SetFillStyle(0)
leg1.SetBorderSize(0)
#leg1.AddEntry(hist3, "with CR","l")
leg1.AddEntry(hist4, "m_{W} 80.403 GeV","")
#leg1.Draw("same")

print "mean =", hist4.GetMean(), " +/- ", hist4.GetMeanError()  ### undefined for a Cauchy distribution
print "mode =", hist4.GetMaximumBin()*binwidth + xMin


c1.SaveAs("../plots/"+sys.argv[0][0:-3]+".pdf")
c1.SaveAs("../plots/"+sys.argv[0][0:-3]+".png")



