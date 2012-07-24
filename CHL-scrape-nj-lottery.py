#   acquire N.J. lottery numbers from state website
#
#   the main lottery site is visual and includes links to 
#   individual games.
#
#   following the link to an individual game,
#   then following the link for 'recent winning numbers'
#   then following the link for 'printer-friendly version'
#   gives a pretty uncluttered view, but 'recent' in tbis case
#   refers to numbers in the past year.
#
#   here, we call up each printer-friendly page and extract
#   only the table rows with today's date.
#   we wrap that combo table in bare-bones HTML.
#   The HTML goes to standard output so it can be redirected
#   to a Web directory.

def dateFourString():
    import time
    theString = time.strftime("%m/%d/%Y")
    return theString

#class AppURLopener(urllib.FancyURLopener):
#    version = "John's Bargain Browser 0.0"

def grabLines(date,URLsnip):
    import urllib
    import re
    grabbedLines = ''
    prefixURL = 'http://www.state.nj.us/lottery/games/'
    URL = prefixURL + URLsnip 
    numbersLink=urllib.urlopen(URL)
    rawNumbers = numbersLink.read()
    rawNumbers = re.sub(r'(?ms)<tr>',r'<splitter><tr>',rawNumbers)
    rawLines = re.split('<splitter>',rawNumbers)
    for aLine in rawLines:
        if (re.search(date,aLine)):
            grabbedLines = grabbedLines + aLine
    return grabbedLines

thisdate=dateFourString()
print '<html><title>Selected New Jersey Lottery numbers</title><body><table cellspacing=16>'
print grabLines(thisdate,'1-6_pick3_history.shtml')
print grabLines(thisdate,'1-5_pick4_history.shtml')
print grabLines(thisdate,'1-4_jersey_cash5_history.shtml')
print grabLines(thisdate,'1-3_pick6_history.shtml')
print '</table></body></html>'
