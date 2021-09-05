from shutil import copyfile
import json

STARTING_LINE = 4
LINE_SKIP = 1
NEW_FILE_NAME = "text.json"
UPDATE_FILE_NAME = "REDGameUpdate.uexp"
OLD_FILE_NAME = "REDGame.uexp"

def ReadFileOffline(fileName):
    file = open(fileName, "r", encoding="utf-16 le", errors="ignore")
    lineList = file.read().splitlines()
    return lineList

def GetChangedJson(oldLineList, newLineList):
    oldLine = STARTING_LINE
    newLine = STARTING_LINE
    oldLineListLen = len(oldLineList)
    newLineListLen = len(newLineList)

    changedLineJson = {"Entries": []}
    while oldLine + LINE_SKIP * 2 < oldLineListLen and newLine + LINE_SKIP * 2 < newLineListLen:
        if oldLineList[oldLine] == newLineList[newLine]:
            oldLine += LINE_SKIP
            newLine += LINE_SKIP
            if oldLineList[oldLine] != newLineList[newLine]:
                changedLineJson["Entries"] += [{"header": oldLineList[oldLine - 1], "text": oldLineList[oldLine]}]
            oldLine += LINE_SKIP
            newLine += LINE_SKIP
        else:
            newLine += LINE_SKIP * 2

    return changedLineJson

def CreateJsonFile(changedLineJson):
    file = open(NEW_FILE_NAME, "w")

    file.write(json.dumps(changedLineJson, ensure_ascii=False, indent='   '))

    print("Donetes have fun luv")

#inputRegion = input("Enter region code of the uexp file to update: ").upper()
#newLineList = ReadFileOnline(inputRegion)
newLineList = ReadFileOffline(UPDATE_FILE_NAME)
if newLineList[0] != "Not Found":
    oldLineList = ReadFileOffline(OLD_FILE_NAME)

    changedLineJson = GetChangedJson(oldLineList, newLineList)

    CreateJsonFile(changedLineJson)
else:
    print(newLineList[0])

input()