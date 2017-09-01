import os
import re

def searchFolder(path):
	files = []
	for file in os.listdir(path):
		if file.endswith(".js"):
			files.append(file)
	return files

def getIdentifiers(file):
    identifiers = []
    if(os.path.exists(file)):
        for i, line in enumerate(open(file)):
            tempLine = parseLine(line)
            if tempLine not in identifiers:
                identifiers.append(tempLine)
            else:
                print "already in db " + str(tempLine)
    return identifiers

def parseLine(line):
    line = line.strip()
    splitLine = line.split(':')
    if len(splitLine) == 2:
        parsedLine = splitLine[1].split('\'')[1::2]
        return parsedLine[0]

def writeFile(identifiers, path):
    file = open(path,"w")

    for id in identifiers:
        file.write('#: ' + path + '\n')
        file.write('msgid \"' + str(id) + '\"\n')
        file.write('msgstr \"\"\n\n')

    file.close()

def main():
	importPath = "/Users/daryl/Documents/react-intl-po-example/locales/en.js"
    exportPath = "/Users/daryl/Documents/react-intl-po-example/locales/isaax-web-app-user.pot"

    enIdentifiers = getIdentifiers(identifiersPath)
    writeFile(enIdentifiers, exportPath)

main()
