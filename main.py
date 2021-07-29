import requests

# url = "github url"
# read_data = requests.get(url).content
# dataString = read_data.decode("utf-8")
# lineList = dataString.splitlines()
# print(lineList[2])

def ReadOldFile(fileName):
    file = open(fileName, "r")
    line = " "
    # Skip first lines, get to SYSTEM_CLOSE
    for i in range(8):
        file.readline()

    while(line != ""):
        # Header, what we want to compare
        line = file.readline()
        # Empty
        line = file.readline()
        # Content, what we want to overwrite
        line = file.readline()
        print(line)
        # Empty
        line = file.readline()




ReadOldFile("REDGame.uexp")

# Starting from line 9, odd numbers are the variable name, pair numbers the content
# Must read two consecutive lines, the second line doesnt have anything
# Python fucking sucks why am i using this i cant remember anything what the f
# Que para el numero de elementos de la lista tengo que poner list.count(variable) estoy hasta los cojones