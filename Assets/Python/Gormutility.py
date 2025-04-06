##
###
###
###
###
from CvPythonExtensions import *
from CvScreenEnums import *
from PyHelpers import PyPlayer
import CvEventManager
import CvUtil
import Popup as PyPopup
import pickle
import sys
from CustomScriptData import csd
gc = CyGlobalContext()
localText = CyTranslator()
game = CyGame()
# globals



#################### Cold War Events ##################

    
#################### GORM Events ##################




#################### GORM CW STAFF ##################
def JomKippurWar():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Jom Kippur War", ())
    szText = localText.getText("Jom Kippur War", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def sixdaywar():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Six day war", ())
    szText = localText.getText("Six day war", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def SynajWar():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Israel army attacking Synai", ())
    szText = localText.getText("Israel army attacking Synai", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def ANOLGAmozbiqueIndependent():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Angola and Mozabique", ())
    szText = localText.getText("Angola and Mozabique be independent", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def KoreaWar():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Korea War", ())
    szText = localText.getText("Korea War", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def SovietAghanWar():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Soviet–Afghan War", ())
    szText = localText.getText("Soviet–Afghan War", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def WarofFaklands():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Falklands War", ())
    szText = localText.getText("Falklands War", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def VietnamWarEND():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Vietnam War End", ())
    szText = localText.getText("Vietnam War End", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def PkisIndiII():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Indo Paskistan war II", ())
    szText = localText.getText("Indo–Pakistani war of 1965", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def PkisIndiI():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Indo Paskistan war I", ())
    szText = localText.getText("Indo-Pakistani war of 1947", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def EWGstart():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Born of European Economic Community/European Community", ())
    szText = localText.getText("Born of European Economic Community/European Community", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def VietnamWar():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Vietnam War", ())
    szText = localText.getText("Vietnam War", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def WARinIndoChina():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("War in Indochina", ())
    szText = localText.getText("War in Indochina", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def czechSpring():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Prague Spring", ())
    szText = localText.getText("Prague Spring", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def decoloniztion():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Decolonization of Africa", ())
    szText = localText.getText("Decolonization of Africa", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def LandinginCuba():
    popup = PyPopup.PyPopup(-1)
    szTitle = localText.getText("Bay of Pigs Invasion", ())
    szText = localText.getText("Bay of Pigs Invasion", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.launch()

def Escalation(self, argsList):
    popup = PyPopup.PyPopup(CvUtil.EventCWstartPopup, contextType = EventContextTypes.EVENTCONTEXT_ALL)
    szTitle = localText.getText("Cold War Begin", ())
    szText = localText.getText("After defeat German, Germany was divided into GDR and GRF", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.addSeparator()
    popup.addButton(localText.getText("Escalation 1 level", ()))
    popup.addButton(localText.getText("Escalation 2 level", ()))
    popup.addButton(localText.getText("Excalation 3 level", ()))
    popup.launch(False)

def EscalationCLICKED(self, playerID, netUserData, popupReturn):
    autoIdx = popupReturn.getButtonClicked()
    if(autoIdx == 0):
            self.EscalationLEVEL = 0 # True events
            csd.set(game, "self.EscalationLEVEL", 0)
    elif(autoIdx == 1):
            self.EscalationLEVEL = 1 # Rand events
            csd.set(game, "self.EscalationLEVEL", 1)
    elif(autoIdx == 2):
            self.EscalationLEVEL = 2 # No events
            csd.set(game, "self.EscalationLEVEL", 2)
                
                
def WarYear(self, argsList):
    popup = PyPopup.PyPopup(CvUtil.EventCWwarYearPopup, contextType = EventContextTypes.EVENTCONTEXT_ALL)
    szTitle = localText.getText("select war Year", ())
    szText = localText.getText("Select War Year", ())
    popup.setHeaderString(szTitle)
    popup.addSeparator()
    popup.setBodyString(szText)
    popup.addSeparator()
    popup.addButton(localText.getText("50s", ()))
    popup.addButton(localText.getText("60s", ()))
    popup.addButton(localText.getText("70s", ()))
    popup.launch(False)

def WarYearCLICKED(self, playerID, netUserData, popupReturn):
    autoIdx = popupReturn.getButtonClicked()
    if(autoIdx == 0):
            self.WarYear = 0 # 50s
            csd.set(game, "self.WarYear", 0)
    elif(autoIdx == 1):
            self.WarYear = 1 # 60s
            csd.set(game, "self.WarYear", 1)
    elif(autoIdx == 2):
            self.WarYear = 2 # 70s
            csd.set(game, "self.WarYear", 2)
                
                
def Country(pCountry):
    iMaxCiv = gc.getMAX_PLAYERS()
    
    if (pCountry == 1):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_CW_USSR")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 2):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WARSAW_PACT")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 3):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_AMERICA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 4):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_GERMANY")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 5):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_SOUTH_AFRICA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 6):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_CW_DEMOKONGO")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 7):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_CW_KONGOGABON")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 8):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_CW_MOZAMBIK")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 9):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_CZAD")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 10):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_CW_SUDAN")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 11):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_ETHIOPIA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 12):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_INDIA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 13):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_IBERIA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 14):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_IRAN_PAKISTAN")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 15):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_MEXICO")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 16):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_GREECE")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 17):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_CANADA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 18):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_YUGOSLAVIA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 19):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_ANGOLA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 20):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_TANGANIKA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 21):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_ALGIERMAROCO")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 22):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_INDONESIA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 23):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_VIETNAM")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 24):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_CHINA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 25):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_ARABIA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 26):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_CW_LIBYA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 27):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_CW_EGYPT")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 28):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_TURKEY")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 29):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_NIGER_MALI")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 30):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_JAPAN")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 31):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_SCANDINAVIA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 32):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_AUSTRALIA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 33):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_BRAZIL")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 34):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_CW_PERUCOLUMBIA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 35):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_ARABIA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 36):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_ITALY")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 37):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_ENGLAND")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 38):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_FRANCE")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 39):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_CENTRAL_AMERICA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 40):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_SWEDEN")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 41):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_WW2_SOUTH_AMERICA")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    if (pCountry == 42):
        for iCivs in range(iMaxCiv):
            pPlayer = gc.getPlayer(iCivs)
            iTCountry = gc.getInfoTypeForString("CIVILIZATION_CW_IZRAEL")
            if pPlayer.getCivilizationType ()==iTCountry:
                return iCivs
    
