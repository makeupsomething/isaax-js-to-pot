import os
import re

def searchFolder(path):
	files = []
	for file in os.listdir(path):
		if file.endswith(".po"):
			files.append(file)
	return files

def readMasterFile(path):
    masterList = []
    text_file = open(path, "r")
    tempList = text_file.readlines()
    for line in  tempList:
        masterList.append(line.strip())

    return masterList

def createTranlateObject(file, identifiers):
    objects = []
    id = 0
    l = 0
    if(os.path.exists(file)):
        for i, line in enumerate(open(file)):
            if len(line) > 0:
                if('msgid' in line):
                    id = parseLine(line)
                elif('msgstr' in line):
                    l = parseLine(line)
            if(id != 0 and l != 0 ):
                objects.append('\'' + id + '\': \'' + l + '\'')
                id = 0
                l = 0
    return objects

def parseLine(line):
    line = line.strip()
    splitLine = line.split('"')
    return splitLine[1]

def writeFile(identifiers, path):
    file = open(path,"w")
    file.write('/*eslint-disable*/\nexport default {\n')
    for id in identifiers:
        file.write(str(id) + '\n')
        #file.write('msgstr \"\"\n\n')
    file.write('}')
    file.close()

def main():
    masterFilePath = "/Users/daryl/Documents/react-intl-po-example/locales/en.js"
    importPath = "/Users/daryl/Documents/react-intl-po-example/locales/"
    exportPath = "/Users/daryl/Documents/react-intl-po-example/locales/ja_test.js"

    identifiers = readMasterFile(masterFilePath)
    files = searchFolder(importPath)

    for f in files:
        translatedLines = createTranlateObject(importPath + f, identifiers)

    #enIdentifiers = getIdentifiers(identifiersPath)
    writeFile(translatedLines, exportPath)

main()
