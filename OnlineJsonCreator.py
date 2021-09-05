import requests
import json
from shutil import copyfile

STARTING_LINE = 4
LINE_SKIP = 1
NEW_FILE_NAME = "text.json"
UPDATE_FILE_NAME = "REDGameUpdate.uexp"
OLD_FILE_NAME = "REDGame.uexp"

def ReadFileOnline(region):
    url = "https://raw.githubusercontent.com/Ferdom-M/StriveTextUpdater/main/REDGame" + region + ".uexp"
    request = requests.get(url)
    read_data = request.content

    file = open(UPDATE_FILE_NAME, 'wb')
    file.write(read_data)

    dataString = read_data.decode("utf-16 le", errors="ignore")
    newLineList = dataString.splitlines()
    return newLineList


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

inputRegion = input("Enter region code of the uexp file to update: ").upper()
newLineList = ReadFileOnline(inputRegion)
#newLineList = ReadFileOffline(UPDATE_FILE_NAME)
if len(newLineList) > 5:
    oldLineList = ReadFileOffline(OLD_FILE_NAME)

    changedLineJson = GetChangedJson(oldLineList, newLineList)

    CreateJsonFile(changedLineJson)
else:
    print("Region not found")

input()