##WarNPeace
###MODDER READ THIS:
###You do not have to change anything in this file
###all changes have to be done in the CvEventManager.
###This file just has to be in the same folder like the CvEventManager.py.

from CvPythonExtensions import *
import sys
import Popup as PyPopup
import CvUtil
gc = CyGlobalContext()
lEvents = []

def triggerEvents(iTurn):
	iTurn += 1
	iYear = CyGame().getTurnYear(iTurn)
	lRemove = []
	for item in lEvents:
		if iYear < item[0]:
			break
		if item[1] <= iTurn:
			for iPlayer in item[2]:
				pPlayer = gc.getPlayer(iPlayer)
				for iUnit in item[3]:
					iUnitType = getUnitID(iUnit[0], iPlayer)
					if iUnitType == -1: continue
					iLeaderType = getUnitID(iUnit[1], iPlayer)
					iX = iUnit[4]
					iY = iUnit[5]
					if iUnit[3]:
						if pPlayer.getNumCities():
							pCapital = pPlayer.getCapitalCity()
							iX = pCapital.getX()
							iY = pCapital.getY()
					pPlot = CyMap().plot(iX, iY)
					if pPlot.isNone(): continue
					if pPlot.isImpassable(): continue
					UnitInfo = gc.getUnitInfo(iUnitType)
					bPlot = True
					if UnitInfo.getDomainType() == DomainTypes.DOMAIN_SEA:
						bPlot = False
						if pPlot.isCity():
							pCity = pPlot.getPlotCity()
							if pCity.isCoastal(gc.getDefineINT("MIN_WATER_SIZE_FOR_OCEAN")):
								bPlot = True
						if pPlot.isWater():
							bPlot = True
					if bPlot:
						for i in xrange(iUnit[2]):
							pNewUnit = pPlayer.initUnit(iUnitType, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.NO_DIRECTION)
							pNewUnit.finishMoves()
							pNewUnit.setLeaderUnitType(iLeaderType)
							if iUnit[6] != "NONE":
								pNewUnit.setName(CyTranslator().getText(iUnit[6], ()))
							if pNewUnit.getUnitCombatType() > -1:
								pNewUnit.setLevel(iUnit[7])
								pNewUnit.setExperience(iUnit[8], 9999999)
								pNewUnit.setDamage(iUnit[11], -1)
							for iPromotion in iUnit[9]:
								pNewUnit.setHasPromotion(iPromotion, True)
							pNewUnit.setImmobileTimer(iUnit[10])
						if item[4] != "NONE":
							doPopup(item[4], iPlayer)
			lRemove.append(item)
	for iRemove in lRemove:
		lEvents.remove(iRemove)

def doPopup(sText, iPlayer):
	pPlayer = gc.getPlayer(iPlayer)
	if pPlayer.isHuman():
		popupInfo = CyPopupInfo()
		popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_TEXT)
		szText = CyTranslator().getText(sText, ())                        
		popupInfo.setText(szText)
		popupInfo.addPopup(iPlayer)
                
def loadEvents(sFilePath):
	del lEvents[:]
	MyFile=open(sFilePath)
	CurEvent = []
	for sCurrent in MyFile.readlines():
		if "#" in sCurrent:
			continue
		if "Owner" in sCurrent:
			lUnits = []
			lOwner = getPlayerID(CutString(sCurrent))
			if len(lOwner) == 0:
				CurEvent = []
			else:
			##	iDate, iTurn, lOwner, lUnits, sMessage]
				CurEvent = [-999999, -1, lOwner, lUnits, ""]
		if len(CurEvent) == 0:
			continue
		if "iDate" in sCurrent:
			sDate = CutString(sCurrent)
			if sDate != "NONE":
				iDate = int(sDate)
				if iDate >= CyGame().getGameTurnYear():
					CurEvent[0] = iDate
		elif "iTurn" in sCurrent:
			iTurn = int(CutString(sCurrent))
			if iTurn > -1:
				if iTurn < CyGame().getGameTurn():
					CurEvent = []
					continue
				else:
					CurEvent[1] = iTurn
					CurEvent[0] = CyGame().getTurnYear(iTurn)
		if CurEvent[0] < CyGame().getGameTurnYear():
			continue
		if "sTriggerMap" in sCurrent:
			sMap = CutString(sCurrent)
			if not bMapCheck(sMap, True):
				CurEvent = []
		elif "sIgnoreMap" in sCurrent:
			sMap = CutString(sCurrent)
			if not bMapCheck(sMap, False):
				CurEvent = []
		elif "<Unit>" in sCurrent:
			lPromotions = []
			## Unit, Leader Unit, Quantity, Capital, PlotX, PlotY, Name, Level, Experience, Promotions, Immobile, iDamage
			CurUnit = ["NONE", "NONE", 1, 0, -1, -1, "NONE", 0, 0, lPromotions, 0, 0]
		elif "<Type>" in sCurrent:
			CurUnit[0] = CutString(sCurrent)
		elif "<LeaderUnit>" in sCurrent:
			CurUnit[1] = CutString(sCurrent)
		elif "<iQuantity>" in sCurrent:
			CurUnit[2] = int(CutString(sCurrent))
		elif "<bCapital>" in sCurrent:
			CurUnit[3] = int(CutString(sCurrent))
		elif "<iPlotX>" in sCurrent:
			CurUnit[4] = int(CutString(sCurrent))
		elif "<iPlotY>" in sCurrent:
			CurUnit[5] = int(CutString(sCurrent))
		elif "<sName>" in sCurrent:
			CurUnit[6] = CutString(sCurrent)
		elif "<iLevel>" in sCurrent:
			CurUnit[7] = max(0, int(CutString(sCurrent)))
		elif "<iExperience>" in sCurrent:
			CurUnit[8] = max(0, int(CutString(sCurrent)))
		elif "<Promotion>" in sCurrent:
			iPromotion = gc.getInfoTypeForString(CutString(sCurrent))
			if iPromotion > -1:
				CurUnit[9].append(iPromotion)
		elif "<iImmobile>" in sCurrent:
			CurUnit[10] = max(0, int(CutString(sCurrent)))
		elif "<iDamage>" in sCurrent:
			CurUnit[11] = max(0, int(CutString(sCurrent)))
		elif "</Unit>" in sCurrent:
			CurEvent[3].append(CurUnit)
		elif "Message" in sCurrent:
			CurEvent[4] = CutString(sCurrent)
			lEvents.append(CurEvent)
	lEvents.sort()
	MyFile.close()

def bMapCheck(sMap, bTrigger):
	if sMap == "NONE":
		return True
	MapName = CyMap().getMapScriptName ()
	if ".civ" in MapName:
		MapName = MapName[:MapName.find(".civ")]
	if ".Civ" in MapName:
		MapName = MapName[:MapName.find(".Civ")]
	if bTrigger:
		return sMap == MapName
	return sMap != MapName

def getPlayerID(sName):
	lPlayers = []
	if gc.getInfoTypeForString(sName) == -1:
		return lPlayers
	for iPlayer in xrange(gc.getMAX_PLAYERS()):	
		pPlayer = gc.getPlayer(iPlayer)
		if pPlayer.isAlive():
			if "CIVILIZATION" in sName and pPlayer.getCivilizationType() == gc.getInfoTypeForString(sName):
				lPlayers.append(iPlayer)
			elif "LEADER" in sName and pPlayer.getLeaderType() == gc.getInfoTypeForString(sName):
				lPlayers.append(iPlayer)
	return lPlayers

def getUnitID(sName, iPlayer):
	iUnit = -1
	if "UNIT_" in sName:
		iUnit = gc.getInfoTypeForString(sName)
	elif "UNITCLASS_" in sName:
		iUnitClass = gc.getInfoTypeForString(sName)
		if iUnitClass == -1:
			return -1
		pPlayer = gc.getPlayer(iPlayer)
		iUnit = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getCivilizationUnits(iUnitClass)
	return iUnit

def CutString(string):   
	string = string[string.find(">") + 1:]
	string = string[:string.find("<")]
	return string