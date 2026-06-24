import os

class CheckNewFile:
    def __init__(self,oldFile=[], source='.'):
        self.source = source
        self.OldFile = oldFile

    def CheckFile(self):
        newFiles = []

        for root, dirs, files in os.walk(self.source):
            for file in files:
                ext = os.path.splitext(file)[1]

                absPath = os.path.abspath(
                    os.path.join(root, file)
                )

                fileInfo = {
                    "fileName": file,
                    "extension": ext,
                    "absolutePath": absPath
                }

                newFiles.append(fileInfo)

        newFile = [
            file
            for file in newFiles
            if file not in self.OldFile
        ]

        self.OldFile = newFiles.copy()

        return newFile
    
    def __del__():
        print("Exit from new file check")