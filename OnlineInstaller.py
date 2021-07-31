import requests
from shutil import copyfile

STARTING_LINE = 4
LINE_SKIP = 1
NEW_FILE_NAME = "NewREDGame.uexp"
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

def CompareFileString(oldLineList, newLineList):
    oldLine = STARTING_LINE
    newLine = STARTING_LINE
    oldLineListLen = len(oldLineList)
    newLineListLen = len(newLineList)
    while oldLine + LINE_SKIP * 2 < oldLineListLen and newLine + LINE_SKIP * 2 < newLineListLen:
        if oldLineList[oldLine] == newLineList[newLine]:
            oldLine += LINE_SKIP
            newLine += LINE_SKIP
            if oldLineList[oldLine] != newLineList[newLine]:
                newLineList[newLine] = oldLineList[oldLine]
            oldLine += LINE_SKIP
            newLine += LINE_SKIP
        else:
            newLine += LINE_SKIP * 2

    return newLineList

def WriteNewFile(newLineList):
    copyfile(UPDATE_FILE_NAME, NEW_FILE_NAME)

    file = open(NEW_FILE_NAME, "r+", encoding="utf-16 le", errors="replace")

    for i in range(STARTING_LINE):
        file.readline()

    size = file.tell()
    file.seek(0, 1)
    file.truncate(size)

    for i in range(STARTING_LINE, len(newLineList)):
        file.write(newLineList[i] + "\n")

    print("Donetes have fun luv")

inputRegion = input("Enter region code of the uexp file to update: ").upper()
newLineList = ReadFileOnline(inputRegion)
#newLineList = ReadFileOffline(UPDATE_FILE_NAME)
if len(newLineList) > 5:
    oldLineList = ReadFileOffline(OLD_FILE_NAME)

    newLineList = CompareFileString(oldLineList, newLineList)

    WriteNewFile(newLineList)
else:
    print("Region not found")

input()