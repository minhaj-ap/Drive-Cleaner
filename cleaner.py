import os
import shutil

def createSubFolder(folder,subFolder):
    subFolderPath= os.path.join(folder,subFolder)
    if not os.path.exists(subFolderPath):
        os.makedirs(subFolderPath)
    return subFolderPath


def cleanFolder(folder):
    for fileName in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,fileName)):
            fileExtesnion = fileName.split('.')[-1].lower()
            if fileExtesnion:
                subFolderName= f"{fileExtesnion.upper()} Files"
                subFolderPath= createSubFolder(folder,subFolderName)
                filePath = os.path.join(folder,fileName)
                shutil.move(filePath,subFolderPath)
                print(f"Moved:{fileName} to {subFolderName}")
            else:
                print(f"can't find the extension of {fileName}")
        else:
            print("no files exist")

if __name__=="__main__":
    print("Drive Cleaning Started.....")
    folderPath=input("Enter the folder path:").strip('"')
    if os.path.isdir(folderPath):
        cleanFolder(folderPath)
        print("Drive cleaning completed")
    else:
        print("Invalid Path")