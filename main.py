#The program uses chrome, please make sure chrome is installed in the default location
from scrapInvestor import Scrape
from processWord import processWord
from negPosAnalysis import negPosAnalysis
from cloudPicture import cloudWord

if __name__ == "__main__":
    a=Scrape()
    a.test()
    processWord()
    negPosAnalysis()
    cloudWord()
