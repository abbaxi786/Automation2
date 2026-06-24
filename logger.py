import os
from datetime import datetime

class Logger:
    def __init__(self):
        self.absPath = os.path.abspath(".")  
        self.MakeAppLog()    
        pass
    
    def MakeAppLog(self):
        try:
            os.mkdir("logs")
            
            with open("logs/log.log","w") as file:
                file.write(f"[{datetime.now()}] Log app created\n")
            self.absPath = os.path.abspath("logs/log.log")
            pass
        except FileExistsError:
            with open("logs/log.log","a") as file:
                file.write(f"[{datetime.now()}] Log app created\n")
            self.absPath = os.path.abspath("logs/log.log")

        except Exception as e:
            print(e)
        pass
    
    def AdditionLog(self,taskType):
        with open(self.absPath,"a") as file:
            file.write(f"[{datetime.now()}] {taskType}\n")
    def __del__(self):
        print("Exit from loger")
        
    
def main():
    L= Logger()
    L.AdditionLog("Add the logs")
    del L
    
    
    
if(__name__== "__main__"):
    main()
