#! /usr/bin/python

# iTunesUnduplicator.py
# Ken M. Haggerty
# Created: 2012,03,17
# Update:  2012,03,17

# INSTRUCTIONS: Copy-paste this script into the iTunes director and run via Terminal.

import sys, os, subprocess, shutil
from os.path import expanduser

trashLocation = expanduser("~")+'/.Trash'
rootFolder = os.getcwd()
foldersToCheck = [os.getcwd()]
deleteCount = 0
trustModeOn = '2'

print('\n')
repeatPrompt = True
while (repeatPrompt):
    print('[UNDUPLICATOR] Turn Trust Mode On?  Trust Mode automatically deletes all duplicate files without user input.\n[1 = YES = Trust Mode ON]  [2 = NO = Trust Mode OFF]')
    trustModeOn = raw_input('>> ')
    if ((trustModeOn == '1') or (trustModeOn == '2')): repeatPrompt = False
    else: print('[UNDUPLICATOR] Invalid input. Please enter a valid input.\n')
trustModeOn = int(trustModeOn)
print('\n')

while (len(foldersToCheck) > 0):
    keepCheckingFolder = False
    folderToCheck = foldersToCheck[0]
    if (trustModeOn == 1): print('[UNDUPLICATOR] Checking folder : %s' % folderToCheck)
    filesToCheck = []
    for subfile in os.listdir(folderToCheck):
        subfilePath = folderToCheck+'/'+subfile
        if (os.path.isdir(subfilePath)):
            if (len(os.listdir(subfilePath)) > 0): foldersToCheck.append(subfilePath)
        else:
            filesToCheck.append(subfile)
    os.chdir(folderToCheck)
    while (len(filesToCheck) > 0):
        fileToCheck = filesToCheck[0]
        if (trustModeOn == 1): sys.stdout.write('.')
        fileToCheckExists = True
        for index in range(1,len(filesToCheck)):
            if (fileToCheckExists):
                if (index < len(filesToCheck)):
                    fileToCompare = filesToCheck[index]
                    filenameToCheck, extensionToCheck = os.path.splitext(fileToCheck)
                    filenameToCompare, extensionToCompare = os.path.splitext(fileToCompare)
                    if (extensionToCheck.lower() == extensionToCompare.lower()):
                        if ((os.path.getsize(fileToCheck)) == (os.path.getsize(fileToCompare))):
                            filenameToCheckCD = 0
                            if ((filenameToCheck[0].isdigit()) and (filenameToCheck[1] == '-') and (filenameToCheck[2:4].isdigit()) and (filenameToCheck[4] == ' ' )):
                                filenameToCheckCD = int(filenameToCheck[0])
                                filenameToCheck = filenameToCheck[2:]
                            filenameToCheckSuffix = 0
                            if ((filenameToCheck[-2] == ' ') and (filenameToCheck[-1].isdigit())):
                                filenameToCheckSuffix = int(filenameToCheck[-1])
                                filenameToCheck = filenameToCheck[:-2]
                            filenameToCompareCD = 0
                            if ((filenameToCompare[0].isdigit()) and (filenameToCompare[1] == '-') and (filenameToCompare[2:4].isdigit()) and (filenameToCompare[4] == ' ' )):
                                filenameToCompareCD = int(filenameToCompare[0])
                                filenameToCompare = filenameToCompare[2:]
                            filenameToCompareSuffix = 0
                            if ((filenameToCompare[-2] == ' ') and (filenameToCompare[-1].isdigit())):
                                filenameToCompareSuffix = int(filenameToCompare[-1])
                                filenameToCompare = filenameToCompare[:-2]
                            if (filenameToCheck == filenameToCompare):
                                fileToKeep = fileToCheck
                                fileToDelete = fileToCompare
                                didSwitch = False
                                if (((filenameToCheckCD != 0) and (filenameToCompareCD != 0) and (filenameToCompareSuffix < filenameToCheckSuffix))
                                    or ((filenameToCheckCD == 0) and (filenameToCompareCD == 0) and (filenameToCompareSuffix < filenameToCheckSuffix))
                                    or ((filenameToCheckCD != 0) and (filenameToCheckSuffix != 0) and (filenameToCompareSuffix == 0))
                                    or ((filenameToCheckCD == 0) and (filenameToCompareCD != 0) and (filenameToCheckSuffix != 0))
                                    or ((filenameToCheckCD == 0) and (filenameToCompareCD != 0) and (filenameToCheckSuffix == 0) and (filenameToCompareSuffix == 0))
                                    or ((filenameToCheckCD == 0) and (filenameToCompareCD == 0) and (filenameToCheckSuffix != 0) and (filenameToCompareSuffix == 0))):
                                    fileToKeep = fileToCompare
                                    fileToDelete = fileToCheck
                                    didSwitch = True
                                decisionHasNotBeenMade = True
                                while (decisionHasNotBeenMade):
                                    if (trustModeOn == 1): decision = '1'
                                    else:
                                        print('[UNDUPLICATOR] Delete File 1?\n> File 1 : %s\n> File 2 : %s\n\n[1 = Delete File 1]  [2 = Delete File 2]  [3 = Skip]  [4 = Open In Finder]  [5 = Quit]' % (fileToDelete, fileToKeep))
                                        decision = raw_input('>> ')
                                    if (decision == '1'):
                                        # Delete File 1
                                        shutil.move(fileToDelete, trashLocation)
                                        deleteCount += 1
                                        if (trustModeOn == 1): sys.stdout.write('X')
                                        if (not(didSwitch)):
                                            filesToCheck.remove(fileToDelete)
                                        else:
                                            fileToCheckExists = False
                                        keepCheckingFolder = True
                                        decisionHasNotBeenMade = False
                                    elif (decision == '2'):
                                        # Delete File 2
                                        shutil.move(fileToDelete, trashLocation)
                                        deleteCount += 1
                                        if (didSwitch):
                                            filesToCheck.remove(fileToDelete)
                                        else:
                                            fileToCheckExists = False
                                        keepCheckingFolder = True
                                        decisionHasNotBeenMade = False
                                    elif (decision == '3'):
                                        # Skip
                                        decisionHasNotBeenMade = False
                                    elif (decision == '4'):
                                        # Open In Finder
                                        subprocess.call(['open', '-R', fileToCheck])
                                        keepCheckingFolder = True
                                        decisionHasNotBeenMade = False
                                    elif (decision == '5'):
                                        # Quit
                                        decisionHasNotBeenMade = False
                                        print('\n')
                                        print('[UNDUPLICATOR] Process quit. Removed %d files' % deleteCount)
                                        print('\n')
                                        sys.exit()
                                    else:
                                        print('[UNDUPLICATOR] Invalid input. Please enter a valid input.')
                                    print('\n')
        filesToCheck.remove(fileToCheck)
    os.chdir(rootFolder)
    if (not(keepCheckingFolder)): foldersToCheck.remove(folderToCheck)
    if (trustModeOn == 1): sys.stdout.write('\n')
print('\n')
print('[UNDUPLICATOR] Process finished. Removed %d files' % deleteCount)
print('\n')