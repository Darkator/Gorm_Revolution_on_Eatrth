Dale's Combat Mod v2.4 for BTS 3.19

I have updated most components of DCM to 3.19. I did this by using the RevDCM source code and using Xenomorph's xml/art files. I have not incorporated Battle Effects. That proved a little tricker to convert, but I may try to incoporate them later with some help. This Mod combines Dale's combat related Mod Components, such as airbombing missions, stack attack, and ranged bombardment, and the WWII style atomic bomber. All source code is available for this mod, fully commented to easily signify what component code relates to. All components can be easily turned off or on in a single XML file which can be edited in any text editor.

------The Team------ 
-Stolenrays & Roamty

----Gameplay-----
-Airbomb Missions-The air-bombing missions which featured in the BtS Mod Road to War are now available separately! Bombers can now air-bomb city defenses, city buildings, port air-bomb mission to attempt to sink ships, factories, or factory production. 
-Fighter Missions -Fighters can air-bomb city defenses,port-air bomb, hangar airbomb, or participate in fighter engagment missions. 
-Ranged Bombardment-Ranged Bombardment allows siege units to bombard in the field. By selecting the bombard icon you can select whether to bombard units only, improvements or cities. 
-Combined Arms Stack Attack-Combined Arms Stack Attack allows a full stack of units to engage an enemy stack of units. It replaces the one-on-one combat concept and allows a full stack to work together to eliminate an enemy stack. 
-Opportunity Fire-Opportunity Fire allows fortified bombard capable units (such as artillery) to automatically barrage enemy units which close on the position. 
-Active Defense-Active Defense allows patrolling fighters to engage enemy troops closing on them. This includes fighters on patrol in any location (city, carrier, etc). 
-WW2 Atomic Bomber-his unit is a bomber that delivers a WW2 style A-Bomb payload. It has bomber graphics coupled with Nuke graphics. 

---Turning components on/off----
-Use Custom GameOptions 
-Route Bombing Checkbox

------Mod-Makers------
This Mod is provided for the benefit of the whole community. Please use all/any parts as required, but please give me credit for the work I've done. Thanks to Roamty for testing and fixes and Dacubz request for the Hangar Airbomb Mission.
A number of new XML tags have been added to certain files, please merge carefully into your own Mods. I suggest using WinMerge to help, as I will only provide "Best Effort" support of merging into your own Mods.
All source code is included in the folder \C++ Changed\  inside the Mod's folder. I have made comments to help you identify which parts of the code belong to which components:

-----Commented Code------
// Dale - DCM: DalesCombatMod specific code (not related to any component)
// Dale - AB: Airbombing missions
// Dale - BE: Battle Effects
// Dale - RB: Ranged Bombard
// Dale - SA: CASA, Opportunity Fire, Active Defense
"RevolutionDCM - ranged bombard"
"RevDCM"
"BETTER_BTS_AI_MOD"
"RevolutionDCM start" --> 
"Dale -" -->
Dale - DCM: Globals
Dale - DCM: Pedia Concepts
Dale - AB: Bombing
Hangar Airbomb
Dale - FE: Fighters
Dale - RB: Field Bombard
Dale - RB: Bug Fix
Dale - BE: Battle Effect
Dale - SA: Opp Fire
Dale - SA: Stack Attack
Dale - NB: A-Bomb 

---New Tags----
BuildingInfos:
iDCMAirbombMission		-Allows and sets odds of air bombing building (should be applied to all new buildings you wish to be bombable)

TechInfos:
bDCMAirBombTech1		-If enabled DCM air bombing chances increased
bDCMAirBombTech2		-If enabled DCM air bombing chances increased

UnitInfos:
iDCMBombRange			-If set the unit may bombard tiles up to the range defined
iDCMBombAccuracy		-Accuracy of DCM bombarding
bDCMAirBomb1			-Allows fighter support
bDCMAirBomb2			-Allows bombing of buildings
bDCMAirBomb3			-Allows bombing of factories
bDCMAirBomb4			-Allows bombing of port facilities to attach ships directly in cities
bDCMAirBomb5			-Allows bombing (destroying hammers) invested in city's current production
bDCMFighterEngage		-Allows unit to engage enemy air units directly