
import os
import shutil
import logger

# Write a script that moves all files in a folder into subfolders by type (images, docs,
# etc.)



class TransferFiles:      
    def __init__(self,source):
        self.source = source 
        self.dictionary =[]      
        self.imageType = [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic", ".svg"
        ]
        self.documentType =  [
        ".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt"
        ]
        
        pass
    
    def GetFiles(self,filePath="."):  
        self.dictionary =[]      
        for root, dirs, files in os.walk(filePath):
            for file in files:
                ext = os.path.splitext(file)[1]
                absPath =os.path.abspath(file)
                fileInfo = {
                    "fileName" : file,
                    "extension": ext,
                    "absolutePath" : absPath                    
                }
                self.dictionary.append(fileInfo)
        return self.dictionary
    
    def WholeExtensions(self):
        paths = self.GetFiles(self.source)
        return [x["extension"] for x in paths] 
    
    def GetImageFiles(self):
        files = self.GetFiles()

        image_files = [
            file for file in files
            if file["extension"] in self.imageType
        ]
        return image_files
    
    def GetDocsFiles(self):
        files = self.GetFiles()
        docFiles = [
            file for file in files
            if file["extension"] in self.documentType
        ]
        return docFiles
    
    def CategorizeByDocs(self):
        docs = self.GetDocsFiles()
        try:
            os.mkdir("Document")        
            absPath = os.path.abspath("Document")
            for item in docs:
                shutil.copy(item["absolutePath"], absPath)
        except FileExistsError as e:
            print("File exists")
            absPath = os.path.abspath("Document")
            for item in docs:
                shutil.copy(item["absolutePath"], absPath)
        except Exception as e:
            print(str(e))
            
            
            # here I set it this way if the file exist it would be deleted and then the new file will take its place in moving         
    def CategorizeByImage(self):
        docs = self.GetImageFiles()
        try:
            os.mkdir("Image")        
            absPath = os.path.abspath("Image")
            for item in docs:
                shutil.copy(item["absolutePath"], absPath)
        except FileExistsError as e:
            print("File exists")
            absPath = os.path.abspath("Image")
            for item in docs:
                if(os.path.exists(item["absolutePath"])): os.remove(item["absolutePath"])                
                shutil.copy(item["absolutePath"], absPath)
        except Exception as e:
            print(str(e))

    def __del__(self):
        print("Exit from File transfer")


def main():
    tf= TransferFiles('.')
    tf.CategorizeByDocs()
    del tf
    
    
if(__name__== "__main__"):
    main()






        
    
    