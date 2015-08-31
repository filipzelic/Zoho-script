import os
import shutil
import sys

def calculateFileSizes(sourcePath, destinationPath, maxSize):
	size = 0.0
	listOfFilesToMove = []
	directoryName = 1
	numberOfFilesAlreadyMoved = 0
	numberOfFilesToMove = len(os.listdir(sourcePath))
	
	for filename in os.listdir(sourcePath):
		numberOfFilesAlreadyMoved += 1
		listOfFilesToMove.append(filename)
		size += float(os.path.getsize(sourcePath + filename)) / 1048576

		if size > maxSize:
			printStatus("Moving files: ", numberOfFilesAlreadyMoved, numberOfFilesToMove)
			destinationName = os.path.join(destinationPath + str(directoryName), '')
			moveFilesToDirectory(sourcePath, listOfFilesToMove, destinationName)
			listOfFilesToMove[:] = []
			directoryName += 1
			size = 0.0
	
	printStatus("Moving files: ", numberOfFilesAlreadyMoved, numberOfFilesToMove)
	destinationName = os.path.join(destinationPath + str(directoryName), '')
	moveFilesToDirectory(sourcePath, listOfFilesToMove, destinationName)
	
	sys.stdout.write("\n")
	compressDirectories(destinationPath, directoryName)

def moveFilesToDirectory(sourcePath, listOfFilesToMove, destinationPath):
	os.makedirs(destinationPath)
	for filename in listOfFilesToMove:
		shutil.move(sourcePath + filename, destinationPath + filename)

def compressDirectories(destinationPath, directoryNumber):
	for directoryName in range(1, directoryNumber + 1):
		printStatus("Compressing directory: ", directoryName, directoryNumber)
		shutil.make_archive(destinationPath + str(directoryName), 'zip', destinationPath + str(directoryName))

def printStatus(text, value, total):
	sys.stdout.write("\r %s: %d/%d" % (text, value, total))
	sys.stdout.flush()

def main():
	maxSize = int(raw_input("Enter maximum size (MB): "))
	sourcePath = raw_input("Enter source path: ")
	destinationPath = raw_input("Enter destination path: ")
	sourcePath = os.path.join(sourcePath, '')
	destinationPath = os.path.join(destinationPath, '')

	calculateFileSizes(sourcePath, destinationPath, maxSize)

if __name__ == '__main__':
	main()