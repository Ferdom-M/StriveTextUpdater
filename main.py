import requests
import os

STARTING_LINE = 4
LINE_SKIP = 1

def ReadFileOnline(region):
    url = "https://gitcdn.link/repo/Ferdom-M/StriveTextUpdater/main/REDGame" + region + ".uexp"
    read_data = requests.get(url).content
    dataString = read_data.decode("utf-16 le", errors="replace")
    newLineList = dataString.splitlines()
    return newLineList


def ReadFileOffline(fileName):
    file = open(fileName, "r", encoding="utf-16 le", errors="replace")
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
    if os.path.exists("NewREDGame.uexp"):
        os.remove("NewREDGame.uexp")
    file = open("NewREDGame.uexp", "x", encoding="utf-16 le")

    for i in range(len(newLineList)):
        file.write(newLineList[i] + "\n")

    print("Donetes have fun luv")


newLineList = ReadFileOnline(input("Enter region code of the uexp file to update: ").upper())
#newLineList = ReadFileOffline("REDGameESN.uexp")
if newLineList[0] != "Not Found":
    oldLineList = ReadFileOffline("REDGame.uexp")

    newLineList = CompareFileString(oldLineList, newLineList)

    WriteNewFile(newLineList)
else:
    print(newLineList[0])
# Starting from line 9, odd numbers are the variable name, pair numbers the content
# Must read two consecutive lines, the second line doesnt have anything
# Python fucking sucks why am i using this i cant remember anything what the f
# Que para el numero de elementos de la lista tengo que poner len(variable) estoy hasta los cojones